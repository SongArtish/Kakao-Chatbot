// 테스트용 JS코드! 챗봇용 코드 아님!
// 그냥 edussafy페이지는 크롤링이 가능하지만, 로그인이 필요한 공지사항 페이지는 안 긁힘! 일단 JSOUP지원해줌!
// 주석은 실패의 흔적이나 혹시나 하는 마음에 남겨둔 것이니 그냥 무시해도 됩니다~~

const request = require('request');
const cheerio = require('cheerio');

const url = "http://edu.ssafy.com/edu/board/notice/detail.do?searchBrdItmCdVal=&brdItmSeq=9115&searchWord=&_csrf=de94507c-d810-49bd-9c80-97c8abeac398&pageIndex=1";
// const url = "http://edu.ssafy.com";

request(url, (error, response, body) => {
  
  if (error) throw error;

  let $ = cheerio.load(body);

  let title = $('head > title');
  let link = $('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb20 > div.board_view > div > div > table > tbody > tr:nth-child(7) > td:nth-child(2) > a');
  console.log(title.text());
  console.log(link.text());

  // form.no.value=value;
  // document.form.action= "fnLogin()";
  // document.form.submit();
  
});
    
// LOGIN_INFO = {
//     'userId': '',
//     'userPwd': ''
// }

// with request.Session() as s:
//     login_req = s.post('https://edu.ssafy.com/comm/login/SecurityLoginForm.do', data=LOGIN_INFO)
//     print(login_req.status_code)

// function response(room, msg, sender, isGroupChat, replier) {
//   if (msg.includes("로그인하고싶다")){
//       var csrf = initial.cookies().get("csrftoken");
//       var login = org.jsoup.Jsoup.connect("https://edu.ssafy.com/comm/login/SecurityLoginForm.do").cookies(initial.cookies()).data("userId","", "userPwd", "").data("auto", "false" "csrftoken", csrf);
//       var data = org.jsoup.Jsoup.connect("http://edu.ssafy.com/edu/board/notice/detail.do?searchBrdItmCdVal=&brdItmSeq=8516&searchWord=&_csrf=bf77af84-6f95-4bc5-b7c0-82325bed1612&pageIndex=2").cookies(login.cookies()).get().select("a.onair");
//       replier.reply(data);
//   }
// }