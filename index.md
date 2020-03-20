---
layout: page
title: IDEAlab
title_image: "/assets/logo_3_2_100_plain.svg"
description: Integrating Design, Engineering, and Analysis
---
{% comment %}
<style type="text/css">
  .carousel-caption {bottom:30px;}
</style>

<div class="row">
  <div class="col-sm-12">
    <div id="carousel-example-generic" class="carousel slide"  data-ride="carousel">
      <!-- Indicators -->
      <ol class="carousel-indicators">
      {% for item in page.carousel-images %}
      {% capture ii %}{{ forloop.index0 }}{% endcapture %}
        <li data-target="#carousel-example-generic" data-slide-to="{{ii}}"{% if ii == '0' %} class="active"{% endif %}></li>
      {%endfor%}
      </ol>

      <!-- Wrapper for slides -->
      <div class="carousel-inner" role="listbox">
        {% for item in page.carousel-images %}
          {% capture ii %}{{ forloop.index0 }}{% endcapture %}
          <div class="item{% if ii == '0' %} active{% endif %}">
            <img src="{{site.base_path}}{{page.carousel-folder}}{{item.file}}" alt="...">
            <div class="carousel-caption">
              {{item.caption}}
            </div>
          </div>
        {%endfor%}
      </div>
      <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
        <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
        <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
  </div>
</div>
{% endcomment %}


<!--
<div class="row">
	<div class="col-sm-2"></div>
	<div class="col-sm-8">
		<img src="{{site.base_path}}/assets/logo_3_2_100_plain.svg" class="img-responsive" alt="IDEAlab Logo">
	</div>
	<div class="col-sm-2"></div>
</div>
-->

<h2>Research Areas</h2>



<div class="row">
<div class="col-sm-4">
  <h3>Design</h3>
  <p>We make new tools surrounding design.</p>
<!--  
  <p class="text-center"><a class="btn btn-primary" href="/design-tools" role="button">Learn More...</a></p>
-->
</div>
<div class="col-sm-4">
  <h3>Manufacturing</h3>
  <p>We pioneer new manufacturing technologies to build dynamic, affordable, ultra-capable robots.</p>
<!--  
<p class="text-center"><a class="btn btn-primary" href="/manufacturing" role="button">Learn More...</a></p>
-->
</div>
<div class="col-sm-4">
  <h3>Analysis</h3>
  <p> We embed analysis into the design process, so you know what will happen <em>before</em> you make it</p>
<!--  
  <p class="text-center"><a class="btn btn-primary" href="/analysis" role="button">Learn More...</a></p>
-->
</div>
</div>

<div class="row">
<div class="col-sm-12">
  <p class="text-center"><a class="btn btn-primary" href="/projects" role="button">Learn More...</a></p>
</div>
</div>


<div class="panel panel-default">
  <div class="panel-heading">
	<h3>News</h3>
  </div>
  <div class="panel-body">
<div class="row">
  {% for post in site.posts limit:3 %}
  <div class="col-sm-3">
    <p><a href="{{site.base_path}}{{ post.url }}">{{ post.title }}</a><br>
    <em>{{ post.date | date: '%B %d, %Y' }}</em><br>
	{% assign item = post %}{% include tweet.html %}
	</p>
    {% if post.description %}
      <p>{{ post.description }}</p>
    {% else %}
      <p>{{ post.excerpt }}</p>
    {% endif %}
  </div>
  {% endfor %}
  <div class="col-sm-3">
  <a href="{{site.base_path}}/news" class="btn btn-primary btn-lg active" role="button">More News...</a>
  </div>
</div>
  </div>
</div>

<!--###############################################################-->

<!--
-->

{% comment %}
<div class="row">
	<div class="col-sm-3"> </div>
	<div class="col-sm-6">
		<a class="twitter-timeline" data-lang="en" data-height="800" data-dnt="true" href="https://twitter.com/idealabasu?ref_src=twsrc%5Etfw">Tweets by idealabasu</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>		
		<div class="panel panel-warning">
<!--
		  <div class="panel-heading">
			<h3 class="panel-title">Ad Blockers</h3>
		  </div>		
-->
		  <div class="panel-body">
			If using ad blockers, whitelist this page to enable the twitter feed.
		  </div>
		</div>		
	</div>
	<div class="col-sm-3"> </div>
</div>
{% endcomment %}

{% comment %}
<div class="row">
  <div class="col-sm-3">
  <div class="thumbnail">
  </div>
  <div class="caption">
  </div>
  </div>
</div>
{% endcomment %}