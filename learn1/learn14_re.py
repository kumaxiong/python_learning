#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

s = '''<ol class="breadcrumb">
          <li class="breadcrumb-item"><a>Home</a></li>
          <li class="breadcrumb-item"><a>Blog</a></li>
          <li class="breadcrumb-item active">Cybercriminals taking advantage of Cryptocurrency Boom</li>
        </ol></ol>'''
result = re.sub('<ol class="breadcrumb">[\D|\d]*?</ol>', 'QAQ', s)

s = '<img class="size-medium wp-image-12357 aligncenter" src="https://www.fox-it.com/nl/wp-content/uploads/sites/12/wiv4jpg-800x400.jpg" alt="" width="800" height="400" srcset="https://www.fox-it.com/nl/wp-content/uploads/sites/12/wiv4jpg-800x400.jpg 800w, https://www.fox-it.com/nl/wp-content/uploads/sites/12/wiv4jpg-640x320.jpg 640w, https://www.fox-it.com/nl/wp-content/uploads/sites/12/wiv4jpg-768x384.jpg 768w, https://www.fox-it.com/nl/wp-content/uploads/sites/12/wiv4jpg.jpg 1200w" sizes="(max-width: 800px) 100vw, 800px"></a>'

result = re.sub('<img class="size-medium wp-image-12357 aligncenter"[\d|\D]*?>', '', s)

s = '''
<!-- AdBegin -->
	 <span style="font-size: 15px; font-weight: bold; color: red;">
	 Protect your website!</span><br>
	 Free Trial, Nothing to install. <br>
	 No interruption of visitors.<br>
	 <a style="text-decoration: underline;" rel="nofollow">www.beyondsecurity.com/vulnerability-scanner</a>
	 <!-- AdEnd -->
'''
result = re.sub('<!-- AdBegin -->[\d|\D]+?<!-- AdEnd -->', '', s)

s = '''
fafdisadjjtest
<a name="Comments"> </a>Comments:</td>
      </tr>
	  <tr>
	   <td>
<div id="disqus_thread"></div>
<script type="text/javascript">
/* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
var disqus_shortname = 'mainsecuriteam'; // required: replace example with your forum shortname

// The following are highly recommended additional parameters. Remove the slashes in front to use.
var disqus_identifier = '5QP3M00MLM';
var disqus_url = 'http://www.securiteam.com/securitynews/5QP3M00MLM.html';

/* * * DON'T EDIT BELOW THIS LINE * * */
(function() {
 var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
 dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
 (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
})();
</script>
<noscript>Please enable JavaScript to view the <a>comments powered by Disqus.</a></noscript>
<a class="dsq-brlink">blog comments powered by <span class="logo-disqus">Disqus</span></a>
</td>
     </tr></table>djiao
'''
result = re.sub('<a name="Comments">[\d|\D]*</table>', '', s)

s = '''
<p>It is fair to say that 2017 was the year of cryptocurrencies. In 2017, many cryptocurrencies went through the roof. Let's take Bitcoin (BTC) as an example: 1.0 BTC got traded for about 1,000 USD in beginning of 2017. In December 2017, one Bitcoin was more than 18,000 USD worth. An increase of <strong>1800%</strong>! It was a very successful year for traders speculating on cryptocurrencies, and even more for cybercriminals: Cryptocurrencies like Bitcoin are the #1 means of payment when it comes to extortions. In the past years, the amount of extortions in cyberspace has grown rapidly. The most popular (and likely most easiest) way to extort money from not only random internet users but also small and medium businesses (like webshops) is DDoS extortion (DD4BC, Armada collective, you name it) and Ransomware (Crypt0L0cker, Locky, Cerber etc). Many of them demand Bitcoins as a ransom.</p>'''
result = re.findall('<p>(.*)<strong>(.*)</strong>(.*)</p>', s)

s = '1001元'
result = re.findall('(\d+)-(\d+)元', s)

s = '-5年'
result = re.findall('(\d+)-(\d+)年', s)

s = "3年以傻"
result = re.findall('(\d+)年.*?', s)
print(result[0])
# a = int(result[0][0]) + int(result[0][1])

l = '''fsfsd
<iframe width="100%" height="415" src="https://www.youtube.com/embed/BxHYtFlKruY" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
fsdfdsf<div>'''
result = re.sub('<iframe .*?</iframe>', '233', l)

# 能够识别浮点数的正则表达式
l = '20-30万/年'
result = re.findall('(\d+\.?\d*)-(\d+)万/年', l)

r = (float(result[0][0]) + float(result[0][1])) / 12 * 10000
int(r)
l = '1.8-2万/月'

result = re.findall('(\d+\.?\d*)-(\d+\.?\d*)万/月', l)

l = '1千/月'
result = re.findall('(\d+\.?\d*)千/月', l)
print(result)

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

page_num = re.search(r'start=(\d)+', url)
page_num_2 = re.search(r'start=\d+', url)

print(233)
result = re.findall(r'start=(\d+)',url)
print(result)
