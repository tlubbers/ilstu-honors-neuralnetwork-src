#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgi
import cgitb
cgitb.enable()


# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
county = form.getvalue('county')
state  = form.getvalue('state')
if form.getvalue('county'):
  county_name = form.getvalue('county')
else:
  county_name = "No County"
if form.getvalue('state'):
  state_name  = form.getvalue('state')
else:
  state_name = "No State"
if form.getvalue('party'):
  party = form.getvalue('party')
else:
  party = "No Party"

print ('''Content-Type: text/html\n

<html>
  <head>
    <title>Political Primary County Result Predictions Using Neural Networks</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <!--[if lte IE 8]><script src="assets/js/ie/html5shiv.js"></script><![endif]-->
    <link rel="stylesheet" href="assets/css/main.css" />
    <!--[if lte IE 9]><link rel="stylesheet" href="assets/css/ie9.css" /><![endif]-->
    <!--[if lte IE 8]><link rel="stylesheet" href="assets/css/ie8.css" /><![endif]-->
  </head>
  <body>''')

print "<p>%s %s %s<p>" %(county, state, party)

print('''
    <!-- Wrapper -->
      <div id="wrapper">
        <!-- Header -->
          <header id="header">
            <div class="inner">
              <a href="index.html" class="logo">
                <span class="symbol"><img src="images/isu.png" alt="" /></span><span class="title">Ilstu Honors</span>
              </a>
              <!-- Nav -->
                <nav>
                  <ul>
                    <li><a href="#menu">Menu</a></li>
                  </ul>
                </nav>
            </div>
          </header>
        <!-- Menu -->
          <nav id="menu">
            <h2>Menu</h2>
            <ul>
              <li><a href="index.py">Home</a></li>
              <li><a href="#">E-Report</a></li>
              <li><a href="#">Illinois State University</a></li>
            </ul>
          </nav>
        <!-- Main -->
          <div id="main">
            <div class="inner">
              <header>
                <h1>Political Primary Predictions By County</h1>
                <p>This is the web interface for a polictical primary predicition tool built by three honors students from Illinois State University. PPP uses a Neural Network trained with county demographics from the US Census and the available 2016 primary results. If you're interested in the nerdy specifics, check out the <a href="#">e-report</a>.</p>
              </header>
              <section name = "form">
                <h2>Check your county!</h2>
                <form method="post" action="index.py" target="_blank">
                <div class = "row-uniform">
                  <div class="6u 12u$(small)">
                    <input type="radio" id="dem_id" name="party" value ="Democrat">
                    <label for="dem_id">Democrat</label>
                    <input type="radio" id="rep_id" name="party" value ="Republican">
                    <label for="rep_id">Republican</label>
                  </div>
                  <div class="12u$">
                    <input type="text" name="county" id="county_id" placeholder="County Name" />
                  </div>
                  <div class="12u$">
                        <div class="select-wrapper">
                          <select name="state" id="state_id" placeholder="Choose a State">
                            <option selected = "selected" value='XX'>Choose a state</option>
                            <option value="AL">Alabama</option>
                            <option value="AK">Alaska</option>
                            <option value="AZ">Arizona</option>
                            <option value="AR">Arkansas</option>
                            <option value="CA">California</option>
                            <option value="CO">Colorado</option>
                            <option value="CT">Connecticut</option>
                            <option value="DE">Delaware</option>
                            <option value="DC">District Of Columbia</option>
                            <option value="FL">Florida</option>
                            <option value="GA">Georgia</option>
                            <option value="HI">Hawaii</option>
                            <option value="ID">Idaho</option>
                            <option value="IL">Illinois</option>
                            <option value="IN">Indiana</option>
                            <option value="IA">Iowa</option>
                            <option value="KS">Kansas</option>
                            <option value="KY">Kentucky</option>
                            <option value="LA">Louisiana</option>
                            <option value="ME">Maine</option>
                            <option value="MD">Maryland</option>
                            <option value="MA">Massachusetts</option>
                            <option value="MI">Michigan</option>
                            <option value="MN">Minnesota</option>
                            <option value="MS">Mississippi</option>
                            <option value="MO">Missouri</option>
                            <option value="MT">Montana</option>
                            <option value="NE">Nebraska</option>
                            <option value="NV">Nevada</option>
                            <option value="NH">New Hampshire</option>
                            <option value="NJ">New Jersey</option>
                            <option value="NM">New Mexico</option>
                            <option value="NY">New York</option>
                            <option value="NC">North Carolina</option>
                            <option value="ND">North Dakota</option>
                            <option value="OH">Ohio</option>
                            <option value="OK">Oklahoma</option>
                            <option value="OR">Oregon</option>
                            <option value="PA">Pennsylvania</option>
                            <option value="RI">Rhode Island</option>
                            <option value="SC">South Carolina</option>
                            <option value="SD">South Dakota</option>
                            <option value="TN">Tennessee</option>
                            <option value="TX">Texas</option>
                            <option value="UT">Utah</option>
                            <option value="VT">Vermont</option>
                            <option value="VA">Virginia</option>
                            <option value="WA">Washington</option>
                            <option value="WV">West Virginia</option>
                            <option value="WI">Wisconsin</option>
                            <option value="WY">Wyoming</option>
                          </select>
                        </div>
                      </div>
                  <ul class="actions">
                    <li><input type="submit" value="Predict" class="special" /></li>
                  </ul>
                </div>
                </form>
              </section>
            </div>
          </div>
          <footer id="footer">
            <div class="inner">
              <section>
                <h2>Get in touch with the creators</h2>
                <form method="post" action="#">
                  <div class="field half first">
                    <input type="text" name="name" id="name" placeholder="Name" />
                  </div>
                  <div class="field half">
                    <input type="email" name="email" id="email" placeholder="Email" />
                  </div>
                  <div class="field">
                    <textarea name="message" id="message" placeholder="Message"></textarea>
                  </div>
                  <ul class="actions">
                    <li><input type="submit" value="Send" class="special" /></li>
                  </ul>
                </form>
              </section>
              <section>
                <h2>Elsewhere</h2>
                <ul class="icons">
                  <li><a href="#" class="icon style2 fa-github"><span class="label">GitHub</span></a></li>
                  <li><a href="#" class="icon style2 fa-phone"><span class="label">Phone</span></a></li>
                  <li><a href="#" class="icon style2 fa-envelope-o"><span class="label">Email</span></a></li>
                </ul>
              </section>
              <ul class="copyright">
                <li>&copy; Illinois State University</li>
              </ul>
            </div>
          </footer>
      </div>
    <!-- Scripts -->
      <script src="assets/js/jquery.min.js"></script>
      <script src="assets/js/skel.min.js"></script>
      <script src="assets/js/util.js"></script>
      <!--[if lte IE 8]><script src="assets/js/ie/respond.min.js"></script><![endif]-->
      <script src="assets/js/main.js"></script>

  </body>
</html>
''')


