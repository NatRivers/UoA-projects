using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.EntityFrameworkCore.ChangeTracking;

using _ass1.model;

namespace _ass1.Data
{
    public class DBWebAPIRepo : IWebAPIRepo
    {
        private readonly WebAPIDBContext _dbContext;

        public DBWebAPIRepo(WebAPIDBContext dbContext)
        {
            _dbContext = dbContext;
        }

        public IEnumerable<Staff> GetAllStaffs()
        {
            IEnumerable<Staff> staffs = _dbContext.Staffs.ToList<Staff>();
            return staffs;
        }

        public IEnumerable<Item> GetItems()
        {
            IEnumerable<Item> items = _dbContext.Items.ToList<Item>();
            return items;
        }

        public IEnumerable<Item> GetItems(string name)
        {
            IEnumerable<Item> all_items = GetItems();
            IEnumerable<Item> items = _dbContext.Items.Where(e => e.Name.IndexOf(name) != -1);

            return items;
        }

        public Staff GetStaffByID(int id)
        {
            Staff staff = _dbContext.Staffs.FirstOrDefault(e => e.Id == id);
            return staff;
        }

        public string GetVersion()
        {
            return "v1";
        }

        public Comment WriteComment(Comment comment)
        {
            //my Id is always giving a NULL or doesnt increment, so I hope you don't mind if i do it manually
            //Xinfeng says it's probably caused by my system error so I dont know how to fix it in this case
            IEnumerable<Comment> last_c = _dbContext.Comments.OrderByDescending(c => c.Id).Take(1);
            int last_id = 0;
            foreach (Comment i in last_c)
            {
                last_id = i.Id;
            }
            comment.Id = last_id + 1;

            EntityEntry<Comment> e = _dbContext.Comments.Add(comment);
            Comment c = e.Entity;
            _dbContext.SaveChanges();
            return c;
        }

        public IEnumerable<Comment> GetComments()
        {
            IEnumerable<Comment> comment = _dbContext.Comments.OrderByDescending(c => c.Id).Take(5).ToList<Comment>();
            return comment;
        }
        public Staff GetCard(int id)
        {
            Staff staff = _dbContext.Staffs.FirstOrDefault(e => e.Id == id);
            return staff;
        }

        public string RegisterUser (User user)
        {
            IEnumerable<User> users = _dbContext.Users.Where(e => e.UserName == user.UserName);
            if (users.Count() == 0)
            {
                EntityEntry<User> e = _dbContext.Users.Add(user);
                _dbContext.SaveChanges();
                return "User successfully registered.";
            }
            else
            {
                return "Username not available.";
            }

        }

        public bool ValidLogin(string UserName, string Password)
        {
            User u = _dbContext.Users.FirstOrDefault
                     (e => e.UserName == UserName && e.Password == Password);
            if (u == null)
                return false;
            else
                return true;
        }

        public Order newOrder(Order order)
        {
            //Same issue as A1 like line52, have to manually enter the Id
            IEnumerable<Order> last_o = _dbContext.Orders.OrderByDescending(o => o.Id).Take(1);
            int last_id = 0;
            foreach (Order i in last_o)
            {
                last_id = i.Id;
            }
            order.Id = last_id + 1;

            EntityEntry<Order> e = _dbContext.Orders.Add(order);
            Order o = e.Entity;
            _dbContext.SaveChanges();
            return o;
        }
    }
}
