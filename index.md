---
title: Home
---

## <span style="color:white;">Welcome to the Dierickx Lab for Circadian Regulation of Cardiometabolism</span>
{:.center}

<br>

<span style="color:white;">Circadian rhythms coordinate many different aspects of behavior and physiology (e.g., fasting/feeding cycles, body temperature and metabolism). The Dierickx lab is interested in the molecular mechanisms of the circadian clock driving rhythmic metabolic processes in the heart. We try to understand how deregulated clocks are leading to cardiovascular defects and are trying to target the circadian clock in order to treat and prevent heart diseases.</span>

---

<!-- 新闻滚动栏开始 -->
<div class="news-container" style="overflow: hidden; height: 30px; position: relative;">
  <ul id="news-list" style="list-style-type: none; margin: 0; padding: 0; position: absolute; top: 0; white-space: nowrap;">
    <!-- 这里添加新闻列表 -->
  </ul>
</div>
<!-- 新闻滚动栏结束 -->

<!-- 新闻滚动栏 JavaScript 开始 -->
<script>
const newsList = document.getElementById("news-list");
const newsItems = [
  { title: "News 1: Fun lab outing: ice hockey play-off game", link: "https://www.dierickxlab.com/2023/04/19/icehockey.html" },
  { title: "News 2：Welcome to Margaux, our new French Postdoc", link: "https://www.dierickxlab.com/2023/03/16/postdoc.html" },
  { title: "News 3：Meet Seval and Daniëlle, our newest PhD and Master’s students!", link: "https://www.dierickxlab.com/2023/02/03/Newphds.html" },
  { title: "News 4：DZHK funds the Circadian Cardiometabolism lab", link: "https://www.dierickxlab.com/2023/01/30/DZHK.html" },
  { title: "News 5：Happy New Year from our lab!", link: "https://www.dierickxlab.com/2023/01/05/Newyear.html" }
];

function createNewsItem(newsItem) {
  const li = document.createElement("li");
  const a = document.createElement("a");
  a.href = newsItem.link;
  a.textContent = newsItem.title;
  a.style.color = "white"; // 将颜色从白色更改为红色
  a.style.textDecoration = "none";
  li.appendChild(a);
  return li;
}

newsItems.forEach((item) => {
  newsList.appendChild(createNewsItem(item));
});

function scrollNews() {
  const firstChild = newsList.firstElementChild;
  newsList.appendChild(firstChild);
  newsList.style.transition = "none";
  newsList.style.top = "-30px";
  setTimeout(() => {
    newsList.style.transition = "top 1s";
    newsList.style.top = "0";
  }, 50);
}

setInterval(scrollNews, 3000);
</script>
<!-- 新闻滚动栏 JavaScript 结束 -->

---

<head>
<!-- Start WOWSlider.com HEAD section -->
<link rel="stylesheet" type="text/css" href="engine1/style.css" />
<script type="text/javascript" src="engine1/jquery.js"></script>
<!-- End WOWSlider.com HEAD section -->
 </head>

<body style="background-color:#202020;">
<!-- Start WOWSlider.com BODY section -->
<div id="wowslider-container1">
<div class="ws_images"><ul>
		<li><img src="data1/images/2.2.png" alt="" title="" id="wows1_0"/></li>
		<li><img src="data1/images/13.13.png" alt="" title="" id="wows1_1"/></li>
		<li><img src="data1/images/7.7.png" alt="" title="" id="wows1_2"/></li>
		<li><img src="data1/images/6.6.png" alt="" title="" id="wows1_3"/></li>
		<li><img src="data1/images/12.12.png" alt="" title="" id="wows1_4"/></li>
		<li><img src="data1/images/4.4.png" alt="" title="" id="wows1_5"/></li>
		<li><img src="data1/images/3.3.png" alt="" title="" id="wows1_6"/></li>
		<li><img src="data1/images/5.5.png" alt="" title="" id="wows1_7"/></li>
		<li><img src="data1/images/10.10.png" alt="" title="" id="wows1_8"/></li>
		<li><img src="data1/images/11.11.png" alt="" title="" id="wows1_9"/></li>
		<li><img src="data1/images/1.1.png" alt="" title="" id="wows1_10"/></li>
		<li><a href="http://wowslider.net"><img src="data1/images/8.8.png" alt="javascript image slider" title="" id="wows1_11"/></a></li>
		<li><img src="data1/images/9.9.png" alt="" title="" id="wows1_12"/></li>
	</ul></div>
	<div class="ws_bullets"><div>
		<a href="#" title=""><span><img src="data1/tooltips/2.2.png" alt=""/>1</span></a>
		<a href="#" title=""><span><img src="data1/tooltips/13.13.png" alt=""/>2</span></a>
		<a href="#" title=""><span><img src="data1/tooltips/7.7.png" alt=""/>3</span></a>
		<a href="#" title=""><span><img src="data1/tooltips/6.6.png" alt=""/>4</span></a>
		<a href="#" title=""><span><img src="data1/tooltips/12.12.png" alt=""/>5</span></a>
		<a href="#" title=""><span><img src="data1/tooltips/4.4.png" alt=""/>6</span></a>
		<a href="#" title=""><span><img src="data1/tooltips/3.3.png" alt=""/>7</span></a>
		<a href="#" title=""><span><img src="data1/tooltips/5.5.png" alt=""/>8</span></a>
		<a href="#" title=""><span><img src="data1/tooltips/10.10.png" alt=""/>9</span></a>
		<a href="#" title=""><span><img src="data1/tooltips/11.11.png" alt=""/>10</span></a>
		<a href="#" title=""><span><img src="data1/tooltips/1.1.png" alt=""/>11</span></a>
		<a href="#" title=""><span><img src="data1/tooltips/8.8.png" alt=""/>12</span></a>
		<a href="#" title=""><span><img src="data1/tooltips/9.9.png" alt=""/>13</span></a>
	</div></div><div class="ws_script" style="position:absolute;left:-99%"><a href="http://wowslider.net">javascript carousel</a> by WOWSlider.com v9.0m</div>
<div class="ws_shadow"></div>
</div>	
<script type="text/javascript" src="engine1/wowslider.js"></script>
<script type="text/javascript" src="engine1/script.js"></script>
<!-- End WOWSlider.com BODY section -->
  </body>
   
