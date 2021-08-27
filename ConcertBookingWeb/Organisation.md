# Organisation

## Individual Branch Making and Master Branch Commits
We made branches for us to commit our works done in our local machines:  

* Vadim Reger (vreg113)  
* Theresa Lan (tlan121)  
* Charmaine Wu (twu268)  

After trying to do our parts and commit them to our separate branches, we looked at each others' codes to see which are the most suitable to be merged into the
master branch. In the end, we came up with the decisions:  

* Charmaine Wu committed Domain Model, Mapper files and basic codes for ConcertResource file.  
* Theresa Lan further added, implemented and made changes to the missing Domain Model, Mapper and DTO files.  
* Vadim Reger further implemented ConcertResource file, made slight changes to Domain Model and Mapper files.  

## Data Management for Concurrency Error Prevention
The strategy we use to prevent concurrency error is ***OPTIMISTIC*** locking. The reason is optimistic locking still allows other users to access and view the seats for booking, however upon commmitting/confirming the chosen seat(s), if a case where another user has booked the same seat and confirms it first, the other user will not be able to book the same seat(s) and gives OptimisticLockException and will need to select another available seat(s). Meanwhile using pessimistic lock will block other users from even viewing the available seats which is not how it is working in reality in a booking system. In order to meet the realistic and common booking systems criteria, we decided to use Optimictic locking for our program. 

Note: We try to add *.setLockMode(LockModeType.OPTIMISTIC)* to the function *public Response booking(BookingRequestDTO bReq, @CookieParam("auth") Cookie cookie)* in the ConcertResource.java file to prevent double bookings to occur, however we kept getting NullPointerException and TestSubscribe Future took too long to return everytime this lock is added.

## Domain Model Implementation Description
The domain models we added into the project are the following:  
* Booking.java
  - @OneToMany mapping between one booking can have many seats   
      FetchType: LAZY  
      CascadeType: REFRESH
      
      Lazy fetch is the default fetch strategy for one-to-many associations. Lazy fetch had been applied here to account for better scalability of the web service. We don't need to load all information about the all the seats associated unless necessary.
      
      CascadeType.REFRESH had been specified here because we want the seats to be re-read from the database if the booking refreshes, as we would have a different state for our seats.
      
  - @ManyToOne mapping between each bookings are associated to one user  
      FetchType: LAZY  
      
      Lazy fetch had been specified here to ensure scalability of the web service.
      
      No cascade type specified as none of the changes made to the booking need to be cascaded to the User database.
      
* Concert.java
  - @ManyToMany mapping between one concert can have many performers, at the same time one performer can be in multiple concerts  
    FetchType: LAZY  
    
    Lazy fetch is the default fetch strategy for many-to-many associations. Lazy fetch had been applied here as a performer can be in multiple concert. We don't want to fetch all information about all other concerts that the performer is involved in unless necessary. Eager fetch would result in an excess amount of data being loaded into memeory, which would negatively affect the scalability of the web service.
    
    No cascade type specified as none of the changes made to the concert need to be cascaded to the Performer database.
    
* ConcertInfoSubscription.java
* ConcertSummary.java
* Performer.java
* Seat.java
* User.java  
