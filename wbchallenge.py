#!/usr/bin/env python2
'''
<script type="text/javascript">
var ip = "108.6.177.114, 208.93.139.30";
var userFullName = "Anonymous";
var refurl = "https://wbchallenge.imaginatik.com/wbchallengecomp.nsf/x/competition?open&eid=2011111685257879005955D51068264";
var localizationMap;
//var localizationGlossary = eval("(" +
        //decodeURIComponent("%7B%22idea%22%3A%7B%22description%22%3A%22Idea%22%2C%22uses%22%3A%5B%22%22%5D%2C%22terms%22%3A%7B%22viewsubmission%22%3A%22View%20Submission%22%2C%22submissionsnapshot%22%3A%22SUBMISSION%20SNAPSHOT%22%2C%22getinvolved%22%3A%22GET%20INVOLVED%22%2C%22newsubmissioncallout%22%3A%22%3Cdiv%20class%3D%5C%22smalltext%20firsttext%5C%22%3ENew%3C%2Fdiv%3E%3Cdiv%20class%3D%5C%22bigtext%20secondtext%5C%22%3ESubmission%3C%2Fdiv%3E%22%2C%22newcommentcallout%22%3A%22%3Cdiv%20class%3D%5C%22smalltext%20firsttext%5C%22%3ENew%3C%2Fdiv%3E%3Cdiv%20class%3D%5C%22bigtext%20secondtext%5C%22%3EComment%3C%2Fdiv%3E%22%2C%22authorinfo%22%3A%22Author%20Info%22%2C%22email%22%3A%22E-Mail%3A%22%2C%22nationality%22%3A%22Nationality%3A%22%2C%22ratethissubmission%22%3A%22Rate%20this%20Submission%22%2C%22voteguidance%22%3A%22How%20do%20you%20rate%20this%20item%3F%20Select%20the%20number%20of%20stars%20that%20reflects%20your%20opinion.%20(login%20required)%22%2C%22stats%22%3A%22Stats%22%2C%22comments%22%3A%22Comments%3A%22%2C%22votes%22%3A%22Votes%3A%22%2C%22avgvote%22%3A%22Avg.%20Vote%3A%22%2C%22challenge%22%3A%22Challenge%22%2C%22datesubmitted%22%3A%22Date%20Submitted%22%2C%22refno%22%3A%22Reference%20No.%22%2C%22title%22%3A%22Title%22%2C%22description%22%3A%22Description%22%2C%22areas%22%3A%22Area(s)%22%2C%22attachments%22%3A%22Attachment(s)%3A%22%2C%22allmonths%22%3A%22Jan%2CFeb%2CMar%2CApr%2CMay%2CJun%2CJul%2CAug%2CSep%2COct%2CNov%2CDec%22%7D%7D%7D",
            //"UTF-8") + ")");
        </script>
'''
from lxml.html import parse

ENTRY_URL = 'https://wbchallenge.imaginatik.com/wbchallengecomp.nsf/x/competition?open&eid=2011111685257879005955D51068264'

raise NotImplementedError('This one is annoying')

html = parse(ENTRY_URL)
print html.xpath('//div[@class="n02v9-recentlypub-readmore"]/a/@href')
