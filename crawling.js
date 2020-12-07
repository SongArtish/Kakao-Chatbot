// 챗봇용 코드
// 현재 이 코드 실행 시, 사이트 상으로 이 페이지 접속하면 바로 로그인 창이 떠서 그런지, 로그인 창이 긁힙니다.

function response(room, msg, sender, isGroupChat, replier) {
  if (msg.includes("강의링크")){
    var data = org.jsoup.Jsoup.connect("http://edu.ssafy.com/edu/board/notice/detail.do?searchBrdItmCdVal=&brdItmSeq=8516&searchWord=&_csrf=bf77af84-6f95-4bc5-b7c0-82325bed1612&pageIndex=2").get().select("a");
    replier.reply(data)
  }
}