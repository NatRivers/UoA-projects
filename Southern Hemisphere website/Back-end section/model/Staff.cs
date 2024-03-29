﻿using System;
using System.ComponentModel.DataAnnotations;

namespace _ass1.model
{
    public class Staff
    {
        [Key]
        public int Id { get; set; }

        [Required]
        public string FirstName { get; set; }

        [Required]
        public string LastName { get; set; }

        [Required]
        public string Title { get; set; }

        [Required]
        public string Email { get; set; }

        [Required]
        public string Tel { get; set; }

        [Required]
        public string url { get; set; }

        [Required]
        public string Research { get; set; }
    }
}
