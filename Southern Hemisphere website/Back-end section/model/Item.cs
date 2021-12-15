using System;
using System.ComponentModel.DataAnnotations;

namespace _ass1.model
{
    public class Item
    {
        [Key]
        public int Id { get; set; }

        [Required]
        public string Name { get; set; }

        [Required]
        public string description { get; set; }

        [Required]
        public double price { get; set; }
    }
}
