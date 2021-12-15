using System;
using System.Text;
using System.Threading.Tasks;
using _ass1.dto;
using Microsoft.AspNetCore.Mvc.Formatters;
using Microsoft.Net.Http.Headers;

namespace _ass1.Helper
{
    public class vCardOutputFormatter : TextOutputFormatter
    {
        public vCardOutputFormatter()
        {
            SupportedMediaTypes.Add(MediaTypeHeaderValue.Parse("text/vcard"));
            SupportedEncodings.Add(Encoding.UTF8);
        }

        public override Task WriteResponseBodyAsync(OutputFormatterWriteContext context,
                                Encoding selectedEncoding)
        {
            CardOutput card = (CardOutput)context.Object;
            StringBuilder builder = new StringBuilder();
            builder.AppendLine("BEGIN:VCARD");
            builder.AppendLine("VERSION:4.0");
            builder.Append("N:").AppendLine(card.N);
            builder.Append("FN:").AppendLine(card.Name);
            if (card.Uid != 0) {
                builder.Append("UID:").AppendLine(card.Uid + "");
                builder.Append("ORG:").AppendLine("Southern Hemisphere Institute of Technology");
            }
            else {
                builder.Append("UID:").AppendLine("");
                builder.Append("ORG:").AppendLine("");
            }
            
            builder.Append("EMAIL;TYPE=work:").AppendLine(card.Email);
            builder.Append("TEL:").AppendLine(card.Tel);
            builder.Append("URL:").AppendLine(card.url);
            builder.Append("CATEGORIES:").AppendLine(card.Categories);
            builder.Append("PHOTO;ENCODING=BASE64;TYPE=").Append(card.PhotoType)
                                          .Append(":").AppendLine(card.Photo);
            builder.Append("LOGO;ENCODING=BASE64;TYPE=").Append(card.LogoType)
                                          .Append(":").AppendLine(card.LogoImg);
            builder.AppendLine("END:VCARD");
            string outString = builder.ToString();
            byte[] outBytes = selectedEncoding.GetBytes(outString);
            var response = context.HttpContext.Response.Body;
            return response.WriteAsync(outBytes, 0, outBytes.Length);
        }

    }
}
