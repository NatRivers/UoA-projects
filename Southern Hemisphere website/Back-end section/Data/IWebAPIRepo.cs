using System;
using System.Collections.Generic;
using _ass1.model;

namespace _ass1.Data
{
    public interface IWebAPIRepo
    {
        IEnumerable<Staff> GetAllStaffs();
        Staff GetStaffByID(int id);

        IEnumerable<Item> GetItems();
        IEnumerable<Item> GetItems(string Name);

        string GetVersion();

        Comment WriteComment(Comment comment);
        IEnumerable<Comment> GetComments();

        Staff GetCard(int id);

        string RegisterUser(User user);
        bool ValidLogin(string UserName, string Password);

        Order newOrder(Order order);
    }
}
