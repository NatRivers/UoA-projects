using System;
using System.ComponentModel.DataAnnotations;

namespace _ass1.dto
{
    public class UserInputDTO
    {
        [Required]
        public string UserName { get; set; }

        [Required]
        public string Password { get; set; }

        public string Address { get; set; }
    }
}
