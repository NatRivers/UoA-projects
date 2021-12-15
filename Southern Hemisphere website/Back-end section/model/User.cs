using System;
using System.ComponentModel.DataAnnotations;

namespace _ass1.model
{
    public class User
    {
        [Key]
        public string UserName { get; set; }

        [Required]
        public string Password { get; set; }

        public string Address { get; set; }
    }
}
