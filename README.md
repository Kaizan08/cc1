<h1>Development Environment</h1>

At the bare minimum you'll need the following for your development environment:

<ol><li>Python</li></ol>

It is strongly recommended to also install and use the following tool:

<ol><li>virtualenv</li></ol>


The following assumes you have all of the recommended tools listed above installed.

1. Clone the project:

<blockquote>$ git clone git@github.com:kaizan08/cc1.git</blockquote>

2. Create and initialize virtualenv for the project:

<blockquote>$ python3 -m venv cc1</blockquote>
<blockquote>$ cd cc1</blockquote>
<blockquote>$ source bin/activate</blockquote>
<blockquote>$ pip install -r requirements.txt</blockquote>

<h3>Tests</h3>
To run tests use the following command:

<blockquote>$ pytest</blockquote>

