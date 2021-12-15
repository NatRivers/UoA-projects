using System;
using Microsoft.EntityFrameworkCore;
using _ass1.model;

namespace _ass1.Data
{
    public class WebAPIDBContext: DbContext
    {
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlite("Data Source=MyDatabase.sqlite");
        }

        public WebAPIDBContext(DbContextOptions<WebAPIDBContext> options) : base(options) { }
        public DbSet<Staff> Staffs { get; set; }
        public DbSet<Item> Items { get; set; }
        public DbSet<Comment> Comments { get; set; }
        public DbSet<User> Users { get; set; }
        public DbSet<Order> Orders { get; set; }
    }
}
