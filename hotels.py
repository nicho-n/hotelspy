import cgi
import requests
import json
import sys
#print("start")
location = sys.argv[1]
checkin = sys.argv[2]
checkout = sys.argv[3]
lng = "0"
lat = "0"
rooms = []

headers = {
	'Host': 'apis.ihg.com',
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
	'Accept': 'application/json, text/plain, */*',
	'Accept-Language': 'en-GB,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'Referer': 'https://whttps://apis.ihg.com/guest-api/v1/ihg/gb/en/searchLightww.ihg.com/hotels/gb/en/find-hotels/hotel/list?qLng=0&qGRM=0&qBrs=ic.ki.vn.in.cp.hi.ex.rs.cv.sb.cw.ul.6c.rc.tc.ma.va.sp.nd.ct&qRpn=1&srb_u=1&qCoMy=052018&qCoD=25&qRms=1&qAAR=6CBARC&qRef=df&qCiD=24&qLat=0&qCiMy=052018&qSHp=1&qWch=0&qRtP=6CBARC&qAdlt=1&qDest=Marquette%252C%2BMI%252C%2BUnited%2BStates&qSrt=sDD&qSmP=3&qPSt=0&qRpp=20&qChld=0&qRRSrt=rt',
	'Content-Type': 'application/json; charset=utf-8',
	'IHG-Language': 'en-US',
	#'X-IHG-MWS-API-Token': '58ce5a89-485a-40c8-abf4-cb70dba4229b',
	#'X-IHG-API-KEY': 'se9ym5iAzaW8pxfBjkmgbuGjJcr3Pj6Y',
	#'X-IHG-SSO-TOKEN': 'eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkExMjhDQkMtSFMyNTYifQ.B_6VTezcrG84mnJsYknoF6Sj8xn2yVkxQtqmz8TotF8d2yRNxvmP-hNbkwR9oNrGUzJXWpBPhEYsoQCt-yfG9FAcLke_lQ2TCIxNGA8nq3G88MSzHglIY6UMko05G_lUGYjfArf_VZGCEymHIBizXXYt_DbDUVSxCF3JpUxD18v3oq7zeaOH9mQhEN_HA6XRAdmwU9iz--JDOhihKqZ9MLuUdFeV-wahs4fo3WaKlTf4q1lASpsKq2HXGn1MV3kHNtXB4ByuQyyB62x7pnkrgc8WDiuNxG398Ctw3cUiN_4pNPgpCeAkB1sgTlr8kcjHIU8_lusmKIQ7kVYmtho23g.UBC47HqaoBYde33rXfHDwg.AfwQKUS1nB_tZhV0_iczpXAqhC-uNukYgepNCSEzK_jhGoFcMvH5zAewfa6fxYI-WxLc8Syq9N4DG-meBnYjCTC8hS0MBpBPCGj9S_xDwrV36JrcRFXVITvwscLsUID_.2drdbIE3vBNcNoS9opfCvg',
	'Content-Length': '345',
	'Origin': 'https://www.ihg.com',
	'Connection': 'keep-alive'
}

data ='{"version":"1.3","checkDailyPointsCost":"true","corporateId":"","stay":{"travelAgencyId":"","dateRange":{"start":"2018-06-24","end":"2018-06-25"},"rateCode":"6CBARC","children":0,"adults":1,"rooms":1},"radius":30,"bulkAvailability":true,"marketingRates":"","location":{"lng":87.395305,"lat":46.543598,"location":"Marquette, MI, United States"}}'

#populate request with inputs from user
d = json.loads(data)
d["stay"]["dateRange"]["start"] = checkin
d["stay"]["dateRange"]["end"] = checkout
d["location"]["location"] = location
d["location"]["lng"] = lng
d["location"]["lat"] = lat

r = requests.post("https://apis.ihg.com/guest-api/v1/ihg/gb/en/searchLight", headers=headers, data=json.dumps(d))
for hotel in r.json()["hotels"]:
	print(hotel)
	hotelCode = hotel["hotelCode"]
	request_room_headers = {
		'Host': 'apis.ihg.com',
		'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
		'Accept': 'application/json, text/plain, */*',
		'Accept-Language': 'en-GB,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate, br',
		'Referer': 'https://www.ihg.com/hotels/gb/en/find-hotels/hotel/rooms?qDest=Marquette,%20MI,%20United%20States&qCiMy=52018&qCiD=24&qCoMy=52018&qCoD=25&qAdlt=1&qChld=0&qRms=1&qRtP=6CBARC&qSlH=MQTSB&qAkamaiCC=US&qSrt=sDD&qBrs=ic.ki.ul.in.cp.vn.hi.ex.cv.rs.va.cw.sb.ma&qAAR=6CBARC&qWch=0&qSmP=1&qRad=30',
		'Content-Type': 'application/json; charset=utf-8',
		'X-IHG-MWS-API-Token': '58ce5a89-485a-40c8-abf4-cb70dba4229b',
		'X-IHG-SSO-TOKEN': 'eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkExMjhDQkMtSFMyNTYifQ.mVayCuPPDwtOqcRHHrsxtpaNTI4ZczYglb2KiF3YMzFSGPPYFkYbdPPb99ajxBqycNStLKM0V4xUDm3kO9eM1KKwMECQTk0BbT7H7qqlEaZi53H4NtyKr5uZ5G1vPpRigwuSxWBB0Qxrta-rk0EaSvQMymlIrr_EkYzCuGini6sRcavJQyLOX23-6wPfNywxF_ekw3MSTjrLlJ6B_qD6RBSZRtiwEU0DcY0TfKzOl1-xIxTeSn4PLlfAor5xDM92TY3rWZPFjgRpa2JBkVvOq-lgBmoUWAo-N1u0XBJfnHQBBjpqcWbt4PGaui79Uw_lsS4QRD19rWxTb99Ei1uDqQ.tAwveV6MbWATkES_S_Dpsg.Pzu6FoC2IKdhe5Rup8i-nwwRfMnL-au1k7cn-ZL-OtuJ7XOlf4vEacC4wZqoBB8fKSc9goMZf_5sirwT3EoMTQ8--HZBEmEq4XeXEtTNFoA.RdY7OGFE9oRgojCRenyoRg',
		'X-IHG-API-KEY': 'se9ym5iAzaW8pxfBjkmgbuGjJcr3Pj6Y',
		'IHG-Language': 'en-US',
		'Content-Length': '220',
		'Origin': 'https://www.ihg.com',
		'Connection': 'keep-alive'
	}
	request_room_data='{"hotelCode":"MQTSB","adults":1,"children":0,"rateCode":"6CBARC","showPointsRate":true,"rooms":1,"version":"1.2","corporateId":"","travelAgencyId":"","dateRange":{"start":"2018-06-24","end":"2018-06-25"},"memberID":null}'
	rd = json.loads(request_room_data)
	rd["hotelCode"] = hotelCode
	r1 = requests.post("https://apis.ihg.com/guest-api/v1/ihg/gb/en/rates", headers=request_room_headers, data=json.dumps(rd))
	for room in r1.json()["rooms"]:
		if room["rateCode"] == "IVANI":
			rooms.append(room)
	request_rewards_nights_headers = {
		'Host': 'apis.ihg.com',
		'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
		'Accept': 'application/json, text/plain, */*',
		'Accept-Language': 'en-GB,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate, br',
		'Referer': 'https://www.ihg.com/hotels/us/en/find-hotels/hotel/rates?qDest=Marquette,%20MI,%20United%20States&qCiMy=52018&qCiD=24&qCoMy=52018&qCoD=25&qAdlt=1&qChld=0&qRms=1&qRtP=IKPCM.6CBARC.IVANI&qSlH=MQTSB&qSlRc=K1KN&qAkamaiCC=US&qSrt=sDD&qBrs=ic.ki.ul.in.cp.vn.hi.ex.cv.rs.va.cw.sb.ma&qAAR=IKPCM.6CBARC&qWch=0&qSmP=1&qRad=30',
		'Content-Type': 'application/json; charset=utf-8',
		#'X-IHG-MWS-API-Token': '58ce5a89-485a-40c8-abf4-cb70dba4229b',
		#'X-IHG-SSO-TOKEN': 'eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkExMjhDQkMtSFMyNTYifQ.mVayCuPPDwtOqcRHHrsxtpaNTI4ZczYglb2KiF3YMzFSGPPYFkYbdPPb99ajxBqycNStLKM0V4xUDm3kO9eM1KKwMECQTk0BbT7H7qqlEaZi53H4NtyKr5uZ5G1vPpRigwuSxWBB0Qxrta-rk0EaSvQMymlIrr_EkYzCuGini6sRcavJQyLOX23-6wPfNywxF_ekw3MSTjrLlJ6B_qD6RBSZRtiwEU0DcY0TfKzOl1-xIxTeSn4PLlfAor5xDM92TY3rWZPFjgRpa2JBkVvOq-lgBmoUWAo-N1u0XBJfnHQBBjpqcWbt4PGaui79Uw_lsS4QRD19rWxTb99Ei1uDqQ.tAwveV6MbWATkES_S_Dpsg.Pzu6FoC2IKdhe5Rup8i-nwwRfMnL-au1k7cn-ZL-OtuJ7XOlf4vEacC4wZqoBB8fKSc9goMZf_5sirwT3EoMTQ8--HZBEmEq4XeXEtTNFoA.RdY7OGFE9oRgojCRenyoRg',
		#'X-IHG-API-KEY': 'se9ym5iAzaW8pxfBjkmgbuGjJcr3Pj6Y',
		'IHG-Language': 'en-US',
		'Content-Length': '262',
		'Origin': 'https://www.ihg.com',
		'Connection': 'keep-alive',
	}
	request_rewards_nights_data = '{"roomCode":"K1KN","hotelCode":"MQTSB","adults":1,"children":0,"rateCode":"IVANI","rooms":1,"corporateId":"","version":"1.3","showEmployeeRate":false,"showPointsRate":true,"travelAgencyId":"","memberID":null,"dateRange":{"start":"2018-06-24","end":"2018-06-25"}}'
	rrd = json.loads(request_rewards_nights_data)
	for room in rooms:
		rrd["roomCode"] = room["roomCode"]
		rrd["hotelCode"] = hotelCode
		r2 = requests.post("https://apis.ihg.com/guest-api/v1/ihg/us/en/rateRules", headers=request_rewards_nights_headers, data=json.dumps(rrd))
		if "rate" in r2.json():
			print(hotelCode + "," + room["description"] + "," + str(r2.json()["rate"]["dailyPointsCost"]) + "," + "\0")

