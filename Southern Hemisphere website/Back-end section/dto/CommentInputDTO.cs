using System;
using System.ComponentModel.DataAnnotations;

namespace _ass1.dto
{
    public class CommentInputDTO
    {
        [Required]
        public string Comment { get; set; }

        public string Name { get; set; }
    }
}
