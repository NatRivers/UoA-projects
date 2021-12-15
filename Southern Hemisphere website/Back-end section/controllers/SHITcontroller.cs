using System;
using System.Linq;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Authorization;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Drawing.Imaging;
using System.Drawing;
using System.Security.Claims;

using _ass1.Helper;
using _ass1.Data;
using _ass1.dto;
using _ass1.model;

namespace _ass1.controllers
{
    [Route("api")]
    [ApiController]
    public class SHITcontroller : Controller //apologies for the class name :)
    {
        private readonly IWebAPIRepo _repository;
        public SHITcontroller(IWebAPIRepo repository)
        {
            _repository = repository;

        }


        [HttpGet("GetLogo")]
        public ActionResult GetLogo()
        {
            string path = Directory.GetCurrentDirectory();
            string shitDir = Path.Combine(path, "SHITdataXY-569504563");
            string imgPath = Path.Combine(shitDir, "StaffPhotos");
            string logofile = Path.Combine(imgPath, "logo.png");
            return PhysicalFile(logofile, "image/png");
        }


        [HttpGet("GetVersion")]
        public ActionResult<string> GetVersion()
        {
            return _repository.GetVersion();
        }


        [Authorize(AuthenticationSchemes = "MyAuthentication")]
        [Authorize(Policy = "UserOnly")]
        [HttpGet("GetVersionA")]
        public ActionResult<string> GetVersionA()
        {
            return _repository.GetVersion();
        }


        [HttpGet("GetAllStaff")]
        public ActionResult<IEnumerable<StaffOutputDTO>> GetAllStaffs()
        {
            IEnumerable<Staff> staffs = _repository.GetAllStaffs();
            IEnumerable<StaffOutputDTO> c = staffs.Select(e => new StaffOutputDTO
            { Id = e.Id, FirstName = e.FirstName, LastName = e.LastName, Title = e.Title, Email = e.Email,
                Tel = e.Tel, url = e.url, Research = e.Research});
            return Ok(c);
        }


        [HttpGet("GetStaffPhoto/{name}")]
        public ActionResult GetStaffPhoto(string name)
        {
            string path = Directory.GetCurrentDirectory();
            string shitDir = Path.Combine(path, "SHITdataXY-569504563");
            string imgPath = Path.Combine(shitDir, "StaffPhotos");
            string fileName1 = Path.Combine(imgPath, name + ".png");
            string fileName2 = Path.Combine(imgPath, name + ".jpg");
            string fileName3 = Path.Combine(imgPath, name + ".gif");
            string notfoundimg = Path.Combine(imgPath, "default.png"); ;
            string respHeader = "";
            string fileName = "";
            if (System.IO.File.Exists(fileName1))
            {
                respHeader = "image/png";
                fileName = fileName1;
            }
            else if (System.IO.File.Exists(fileName2))
            {
                respHeader = "image/jpeg";
                fileName = fileName2;
            }
            else if (System.IO.File.Exists(fileName3))
            {
                respHeader = "image/gif";
                fileName = fileName3;
            }
            else
                return PhysicalFile(notfoundimg, "image/png");
            return PhysicalFile(fileName, respHeader);
        }


        [HttpGet("GetItems")]
        [HttpGet("GetItems/{name}")]
        public ActionResult<IEnumerable<ItemOutputDTO>> GetItems(string name)
        {
            IEnumerable<Item> items = _repository.GetItems();

            if (name != null)
            {
                IEnumerable<Item> items_filter = items.Where(e => e.Name.ToLower().Contains(name.ToLower()));
                if (items_filter == null)
                {
                    return NotFound();
                }
                items = items_filter;
            }
            
            IEnumerable<ItemOutputDTO> c = items.Select(e => new ItemOutputDTO
            { Id = e.Id, Name = e.Name, description = e.description, price = e.price });
            return Ok(c);
            
        }


        [HttpGet("GetItemPhoto/{name}")]
        public ActionResult GetItemPhoto(string name)
        {
            string path = Directory.GetCurrentDirectory();
            string shitDir = Path.Combine(path, "SHITdataXY-569504563");
            string imgPath = Path.Combine(shitDir, "ItemImages");
            string fileName1 = Path.Combine(imgPath, name + ".png");
            string fileName2 = Path.Combine(imgPath, name + ".jpg");
            string fileName3 = Path.Combine(imgPath, name + ".gif");
            string notfoundimg = Path.Combine(imgPath, "default.png"); ;
            string respHeader = "";
            string fileName = "";
            if (System.IO.File.Exists(fileName1))
            {
                respHeader = "image/png";
                fileName = fileName1;
            }
            else if (System.IO.File.Exists(fileName2))
            {
                respHeader = "image/jpeg";
                fileName = fileName2;
            }
            else if (System.IO.File.Exists(fileName3))
            {
                respHeader = "image/gif";
                fileName = fileName3;
            }
            else
                return PhysicalFile(notfoundimg, "image/png");
            return PhysicalFile(fileName, respHeader);
        }


        [HttpPost("WriteComment")]
        public ActionResult<CommentOutputDTO> WriteComment(CommentInputDTO comment)
        {
            DateTime d = DateTime.Now;
            var IP = Request.HttpContext.Connection.RemoteIpAddress;
            Comment c = new Comment { Time = d, CommentText = comment.Comment, Name = comment.Name, IPAddr = IP.ToString() };
            Comment newComment = _repository.WriteComment(c);
            CommentOutputDTO co = new CommentOutputDTO {CommentText = newComment.CommentText, Name = newComment.Name }; 
            return CreatedAtAction(nameof(GetComments), co);
        }


        [HttpGet("GetComments")]
        public ContentResult GetComments()
        {
            IEnumerable<Comment> lastFiveComments = _repository.GetComments();
            string openhtml = "<html><head><title></title></head><body>\n";
            string closehtml = "</body></html>";

            List<string> temp = new List<string>();
            foreach (Comment c in lastFiveComments)
            {
                string CommentText = c.CommentText;
                string Name = c.Name;
                if (Name == null)
                {
                    Name = "";
                }
                string output = "<p>" + CommentText + "&mdash;" + Name + "</p>\n";
                temp.Add(output);
            }

            foreach (string s in temp)
            {
                openhtml += s;
            }

            ContentResult content = new ContentResult
            {
                Content = openhtml + closehtml,
                ContentType = "text/html",
                StatusCode = (int)HttpStatusCode.OK,
            };
            return content;
        }


        [HttpGet("GetCard/{id}")]
        public ActionResult GetCard(int id)
        {
            Staff staff = _repository.GetCard(id);
            string path = Directory.GetCurrentDirectory();
            string shitDir = Path.Combine(path, "SHITdataXY-569504563");
            string imgPath = Path.Combine(shitDir, "StaffPhotos");
            if (staff != null)
            {
                string fileName1 = Path.Combine(imgPath, id + ".png");
                string fileName2 = Path.Combine(imgPath, id + ".jpg");
                string fileName3 = Path.Combine(imgPath, id + ".gif");
                string fileName = "";
                string photoString, photoType;
                ImageFormat imageFormat;
                if (System.IO.File.Exists(fileName1))
                {
                    fileName = fileName1;
                }
                else if (System.IO.File.Exists(fileName2))
                {
                    fileName = fileName2;
                }
                else if (System.IO.File.Exists(fileName3))
                {
                    fileName = fileName3;
                }
                else { return NotFound(); }

                Image image = Image.FromFile(fileName);
                imageFormat = image.RawFormat;
                image = ImgHelper.Resize(image, new Size(100, 100), out photoType);
                photoString = ImgHelper.ImageToString(image, imageFormat);

                CardOutput cardOut = new CardOutput();
                cardOut.N = staff.LastName + ";" + staff.FirstName + ";;" + staff.Title + ";";
                cardOut.Name = staff.Title + " " + staff.FirstName + " " + staff.LastName;
                cardOut.Uid = staff.Id;
                cardOut.Email = staff.Email;
                cardOut.Tel = staff.Tel;
                cardOut.url = staff.url;
                cardOut.Photo = photoString;
                cardOut.PhotoType = photoType;

                string logoString, logoType;
                ImageFormat logoFormat;
                string logofile = Path.Combine(imgPath, "logo.png");
                Image logoimg = Image.FromFile(logofile);
                logoFormat = logoimg.RawFormat;
                logoimg = ImgHelper.Resize(logoimg, new Size(100, 100), out logoType);
                logoString = ImgHelper.ImageToString(logoimg, logoFormat);
                cardOut.LogoImg = logoString;
                cardOut.LogoType = logoType;

                cardOut.Categories = Helper.CategoryHelper.Filter(staff.Research);
                Response.Headers.Add("Content-Type", "text/vcard");
                return Ok(cardOut);
            }
            else
            {
                CardOutput cardOut = new CardOutput();
                cardOut.N = ";" + ";;" + ";";
                cardOut.Name = "";
                cardOut.Uid = 0;
                cardOut.Email = "";
                cardOut.Tel = "";
                cardOut.url = "";
                cardOut.Photo = "";
                cardOut.PhotoType = "UNKNOWN";

                string logoString, logoType;
                ImageFormat logoFormat;
                string logofile = Path.Combine(imgPath, "logo.png");
                Image logoimg = Image.FromFile(logofile);
                logoFormat = logoimg.RawFormat;
                logoimg = ImgHelper.Resize(logoimg, new Size(100, 100), out logoType);
                logoString = ImgHelper.ImageToString(logoimg, logoFormat);
                cardOut.LogoImg = logoString;
                cardOut.LogoType = logoType;

                cardOut.Categories = "";
                Response.Headers.Add("Content-Type", "text/vcard");
                return Ok(cardOut);
            }
        }


        [HttpPost("Register")]
        public ActionResult RegisterUser(UserInputDTO user)
        {
            User u = new User { UserName = user.UserName, Password = user.Password, Address = user.Address};
            string msgOut = _repository.RegisterUser(u);
            return Ok(msgOut);
        }


        [Authorize(AuthenticationSchemes = "MyAuthentication")]
        [Authorize(Policy = "UserOnly")]
        [HttpPost("PurchaseItem")]
        public ActionResult<OrderOutputDTO> PurchaseItem(OrderInputDTO itemPurchased)
        {
            ClaimsIdentity ci = HttpContext.User.Identities.FirstOrDefault();
            Claim c = ci.FindFirst("UserName");
            string username = c.Value;
            Order o = new Order { UserName = username, ProductID = itemPurchased.ProductID, Quantity = itemPurchased.Quantity };
            Order newOrder = _repository.newOrder(o); //ProductID is always valid in A2
            OrderOutputDTO orderOut = new OrderOutputDTO {
                Id = newOrder.Id,
                UserName = newOrder.UserName,
                ProductID = newOrder.ProductID,
                Quantity = newOrder.Quantity};
            return Ok(orderOut);
        }

        [Authorize(AuthenticationSchemes = "MyAuthentication")]
        [Authorize(Policy = "UserOnly")]
        [HttpGet("PurchaseSingleItem/{ProductID}")]
        public ActionResult<OrderOutputDTO> PurchaseSingleItem(int ProductID)
        {
            ClaimsIdentity ci = HttpContext.User.Identities.FirstOrDefault();
            Claim c = ci.FindFirst("UserName");
            string username = c.Value;
            Order o = new Order { UserName = username, ProductID = ProductID, Quantity = 1 }; //default quantity is 1
            Order newOrder = _repository.newOrder(o); //ProductID is always valid in A2
            OrderOutputDTO orderOut = new OrderOutputDTO
            {
                Id = newOrder.Id,
                UserName = newOrder.UserName,
                ProductID = newOrder.ProductID,
                Quantity = newOrder.Quantity
            };
            return Ok(orderOut);
        }
    }
}
