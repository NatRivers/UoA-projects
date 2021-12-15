using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace _ass1.model
{
    public class Comment
    {
        [Key]
        //[DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }

        public DateTime Time { get; set; }

        [Required]
        public string CommentText { get; set; }

        public string Name { get; set; }

        public string IPAddr { get; set; }
        
    }
}
