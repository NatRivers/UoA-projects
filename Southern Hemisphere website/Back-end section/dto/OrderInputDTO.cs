using System;
using System.ComponentModel.DataAnnotations;

namespace _ass1.dto
{
    public class OrderInputDTO
    {
        [Required]
        public int ProductID { get; set; }

        [Required]
        public int Quantity { get; set; }
    }
}
