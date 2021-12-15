using System;
using Microsoft.AspNetCore.Authentication;

using Microsoft.Extensions.Options;
using Microsoft.Extensions.Logging;
using System.Text.Encodings.Web;
using System.Threading.Tasks;
using System.Net.Http.Headers;
using System.Text;

using _ass1.Data;
using System.Security.Claims;

namespace _ass1.Handler
{
    public class AuthHandler : AuthenticationHandler<AuthenticationSchemeOptions>
    {
        private readonly IWebAPIRepo _repo;

        public AuthHandler(
            IWebAPIRepo repo,
            IOptionsMonitor<AuthenticationSchemeOptions> options,
            ILoggerFactory logger,
            UrlEncoder encoder,
            ISystemClock clock)
            : base(options, logger, encoder, clock)

        {
            _repo = repo;
        }

        protected override async Task<AuthenticateResult> HandleAuthenticateAsync()
        {
            //check if user exist
            if (!Request.Headers.ContainsKey("Authorization")) 
            {
                Response.Headers.Add("WWW-Authenticate", "Basic");
                return AuthenticateResult.Fail("Authorization header not found.");
            }
            else
            {
                var authHeader = AuthenticationHeaderValue.Parse(Request.Headers["Authorization"]);
                var utfBytes = Convert.FromBase64String(authHeader.Parameter);
                var credential = Encoding.UTF8.GetString(utfBytes).Split(":");
                var username = credential[0];
                var password = credential[1];

                //user exist and gives correct username & pw
                if (_repo.ValidLogin(username, password))
                {
                    var claims = new[] { new Claim("userName", username) };
                    ClaimsIdentity identity = new ClaimsIdentity(claims, "Basic");
                    ClaimsPrincipal principal = new ClaimsPrincipal(identity);
                    AuthenticationTicket ticket = new AuthenticationTicket(principal, Scheme.Name);
                    return AuthenticateResult.Success(ticket);
                }
                else //user exist but diff username or pw
                {
                    return AuthenticateResult.Fail("userName and password do not match");
                }
            }
        }

    }
}
