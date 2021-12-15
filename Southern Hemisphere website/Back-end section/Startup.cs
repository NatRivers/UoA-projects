using System;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.HttpOverrides;

using _ass1.Data;
using _ass1.Helper;
using _ass1.Handler;

namespace _ass1
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddControllers();
            services.AddDbContext<WebAPIDBContext>(options =>
                     options.UseSqlite(Configuration.GetConnectionString("WebAPIConnection")));
            services.AddScoped<IWebAPIRepo, DBWebAPIRepo>();

            services.AddMvc(options => options.OutputFormatters
                                          .Add(new vCardOutputFormatter()));

            services.AddAuthentication().
            AddScheme<AuthenticationSchemeOptions, AuthHandler>
            ("MyAuthentication", null);

            services.AddAuthorization(options =>
            {
                options.AddPolicy("UserOnly", policy => policy.RequireClaim("UserName"));
            });

        }

        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }
            else
            {
                app.UseExceptionHandler("/Error");
                app.UseHsts();
            }

            app.UseHttpsRedirection();
            app.UseHsts();
            app.UseRouting();
            app.UseAuthentication();
            app.UseAuthorization();
            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });

            app.UseForwardedHeaders(new ForwardedHeadersOptions
            {
                ForwardedHeaders = ForwardedHeaders.XForwardedFor |
                ForwardedHeaders.XForwardedProto
            });
        }   
    }
}
