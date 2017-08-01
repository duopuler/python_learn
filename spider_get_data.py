#encoding:utf-8
from bs4 import BeautifulSoup as bs
import re
html_doc = """
<html><head><script type="text/javascript" charset="gb2312" src="//www.baidu.com/cache/aladdin/ui/dropdown21/dropdown21.js?v=20140227" data-for="A.ui"></script><script type="text/javascript" charset="gb2312" src="//www.baidu.com/cache/aladdin/ui/scrollbarv/scrollbarv.js?v=20140121" data-for="A.ui"></script>
		
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<meta name="Description" content="百度学术搜索，是一个提供海量中英文文献检索的学术资源搜索平台，涵盖了各类学术期刊、学位、会议论文，旨在为国内外学者提供最好的科研体验。">

		<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
		<link rel="icon" sizes="any" mask="" href="//www.baidu.com/img/baidu.svg">

		
<title>
python_百度学术
</title>

		
		
<style>
@font-face {font-family: "iconfont";
  src: url('/r/www/cache/mid/static/xueshu/iconfont/iconfont.eot?t=1484020434930'); /* IE9*/
  src: url('/r/www/cache/mid/static/xueshu/iconfont/iconfont.eot?t=1484020434930#iefix') format('embedded-opentype'), /* IE6-IE8 */
  url('/r/www/cache/mid/static/xueshu/iconfont/iconfont.woff?t=1484020434930') format('woff'), /* chrome, firefox */
  url('/r/www/cache/mid/static/xueshu/iconfont/iconfont.ttf?t=1484020434930') format('truetype'), /* chrome, firefox, opera, Safari, Android, iOS 4.2+*/
  url('/r/www/cache/mid/static/xueshu/iconfont/iconfont.svg?t=1484020434930#iconfont') format('svg'); /* iOS 4.1- */
}
</style>
    
    <link rel="stylesheet" href="http://s1.bdstatic.com/r/www/cache/mid/static/xueshu/css/page_a14c138.css">
    



		
		
<script src="//hm.baidu.com/hm.js?43115ae30293b511088d3cbe41ec099c"></script><script>
var name,navigate,bdQid="a509339200013447";
var bds={
    se:{},
    util:{},
    //结果页js通用数据
    comm : {
        domain:"http://www.baidu.com",
        ubsurl : "http://sclick.baidu.com/w.gif",
        tn:"SE_baiduxueshu_c1gjeupa",
        queryEnc:"python",
        queryId:"a509339200013447",
        ishome : 0,
        isTransShow: 0,
        query : "python",
        queryShow : "python",
        qid : "a509339200013447",
        cid : "0",
        sid : "",
        f : "8",
        pn : "0",
        oq : "",
        rsp : "",
        sc_f_para : "sc_tasktype={firstSimpleSearch}",
        stoken : "",
        serverTime : "1501125102",
        user : "",
        username : "",
        isLogin : "0",
        loginAction : [],
        useFavo : "",
        pinyin : "python",
        favoOn : "",
        personalData : "",
        curResultNum:"10",
        rightResultExist:false,
        protectNum:0,
        zxlNum:0,
        pageNum:parseInt('1')||1,
        pageSize:parseInt('10')||10,
        taskTipsShow: 1,
        subpro: 'xueshu_respage',
        isSchoolShow: 0,
        schoolEname: "",
        resultTn:"SE_baiduxueshu_c1gjeupa",
        scFrom:"",
        scAsPara:"",
        isdetailpage: 0,
        topBannerInfo: {
            startDate: "2017\/05\/16",
            endDate: "2017\/05\/22",
            width: "200",
            height: "214",
            id: "diaoyan2017",
            imgUrl: "http:\/\/s1.bdstatic.com\/r\/www\/cache\/mid\/static\/xueshu\/img\/banner\/r_banner_diaoyan_8f0a8bc.png",
            jumpUrl: "https:\/\/sojump.com\/jq\/13980160.aspx"
        }
    }
};

bds.comm.upn = {"browser":"lbbrowser","ie":"","os":"windows","win":"win7","browsertype":"chrome"};

var selfOpen = window.open;
eval("var open = selfOpen;");

function G(id){
    return document.getElementById(id);
}

function TagQ(tag,obj){
	return obj.getElementsByTagName(tag);
}

/**
* @description 增加sclick统计
* @function
* @name c
* @grammar c(1)
* @param {Object} q 字段集合
* @return {Boolean} 当发送成功时返回true
*/
function c(q){
    var p = window.document.location.href, sQ = '', sV = '', mu='', img = window["BD_PS_C" + (new Date()).getTime()] = new Image();
    for (v in q) {
        switch (v) {
            case "title":
                sV = encodeURIComponent(q[v].replace(/<[^<>]+>/g, ""));
                break;
            case "url":
                sV = escape(q[v]);
                break;
            default:
                sV = q[v];
        }
        sQ += "&" + v + "=" + sV;
    }
    try{
        if (("p2" in q)&&G(q["p1"]).getAttribute("mu") && q["fm"]!="pl") {
            mu= "&mu=" + escape(G(q["p1"]).getAttribute("mu"));
        }
    }catch(e){};
	img.src = "http://sclick.baidu.com/w.gif?q=" + bds.comm.queryEnc + sQ + mu + "&rsv_sid=" + bds.comm.sid + "&cid="+bds.comm.cid+"&qid="+bds.comm.qid+"&t="+new Date().getTime()+"&path="+p;
    return true;
}

/**
* @description 增加nsclick统计
* @function
* @name c
* @grammar ns_c(1)
* @param {Object} q 字段集合
* @return {Boolean} 当发送成功时返回true
*/
function ns_c(q){
	ns_c_xs(q);
}

/**
* @description 增加xueshu nsclick统计
* @function
* @name c
* @grammar ns_c(1)
* @param {Object} q 字段集合
* @return {Boolean} 当发送成功时返回true
*/

function ns_c_xs(q){
    var p = encodeURIComponent(window.document.location.href), sQ = '',wd=bds.comm.queryEnc, sV = '', mu='', img = window["BD_PS_C" + (new Date()).getTime()] = new Image();
    for (v in q) {
        switch (v) {
            case "title":
                sV = encodeURIComponent(q[v].replace(/<[^<>]+>/g, ""));
                break;
            case "url":
                sV = encodeURIComponent(q[v]);
                break;
            default:
                sV = q[v]
        }
        sQ += v + "=" + sV + "&";
    }
    mu= "&mu=" + p;

    // mod当前搜索是否为图书馆模式
    var mod = bds.comm.schoolEname ? '&mod=lib_' + bds.comm.schoolEname : '';
    //fr是否来自详情页
    var fr = bds.comm.isdetailpage ? '&fr=detailpage' : '';
    img.src = "http://nsclick.baidu.com/v.gif?pid=201&pj=mp_xueshu&qid=" + bds.comm.qid + "&rsv_sid=" + bds.comm.sid + "&wd=" + wd + "&" + sQ + "f=" + bds.comm.f + "&oq=" + bds.comm.oq + "&rsp=" + bds.comm.rsp + "&path=" + p + "&tn=" + bds.comm.tn + "&t=" + new Date().getTime() + '&pn=' + bds.comm.pn + mod + fr;
    return true;
}

/**
* @description 为搜索请求添加query，并增加ie参数
* @function
* @name setHeadUrl
* @grammar setHeadUrl(el)
* @param {Object} el 点击的链接对象
*/
function setHeadUrl(el){
    var word = G("kw").value;
    word = encodeURIComponent(word);
    var url = el.href;
    url = url.replace(new RegExp("(" + el.getAttribute('wdfield') + "=)[^&]*"), '\x241' + word+"&ie=utf-8");
    el.href = url;
}

bds.util.getWinWidth = function(){
    return window.document.documentElement.clientWidth;
};
//设置页面主体宽度
//由于此时tangram还没加载，所以不能使用baidu.dom.addClass/removeClass
bds.util.setContainerWidth = function(){
    var c = G('container'),w = G('wrapper'),
    remove = function(r,o){o.className = o.className.replace(r, '');},

    add = function(cls,o){o.className = (o.className+' '+cls).replace(/^\s+/g, "");},
    has = function(r,o){return r.test(o.className)};
    if(bds.util.getWinWidth()<1310){
        remove(/\bcontainer_l\b/g,c);
        remove(/\bwrapper_l\b/g,w);
        if(!has(/\bcontainer_s\b/,c)) add('container_s',c);
        if(!has(/\bwrapper_s\b/,w)) add('wrapper_s',w);
    bds.comm.containerSize = "s";
    }else{
        remove(/\bcontainer_s\b/g,c);
        remove(/\bwrapper_s\b/g,w);
        if(!has(/\bcontainer_l\b/,c)) add('container_l',c);
        if(!has(/\bwrapper_l\b/,w)) add('wrapper_l',w);
    bds.comm.containerSize = "l";
    }
};
// ie版本
bds.util.Ieversion = function() {
    var ua = navigator.userAgent,
        iereg = /MSIE (\d+).*/,
        version = ua.match(iereg);

    if (version && version[1]) {
        return parseInt(version[1]);
    }
    return -1;
};

//阿拉丁命名空间
window.A =  bds.aladdin = {
    ids: [],
    has: true,
    list: [],
    logs: [],
    loadTimes: []
};

(function(){
    var fns = [], isReady = false;
    var exec = function(fn, thisobj){
        try{
            fn.call(thisobj);
        }catch(e){
            if(window.debugFlag) throw e;
        }
    };

    //在js基础库加载完成后执行fn
    bds.ready = function(fn){
        if(typeof fn != 'function') return;
        if(isReady){exec(fn)}
        else{fns.push(fn);}
    };

    //手动触发ready
    bds.doReady = function(){
        isReady = true;
        while(fns.length) exec(fns.shift());
    };

    //通过json字符串获取对象
    var getJson = function(jsonString){
        var result = {};
        if(jsonString){
            try{
                var r = new Function("return " + jsonString)();
                if(r) result = r;
            }catch(e){}
        }
        return result;
    },


    // 获取当前阿拉丁DOM容器
    getCurrentAladdin = (function(){
        var scripts = document.getElementsByTagName("script");
        return function(){
            var script = scripts[scripts.length - 1], container = script;
            while(container){
                if( container.className ){
                    if( /(?:^|\s)result(?:-op)?(?:$|\s)/.test(container.className)){
                        if( tplname = container.getAttribute("tpl") ){
                            return container;
                        }
                    }
                }
                container = container.parentNode;
            }
        };
    })(),

    // 筛选出阿拉丁结果
    getResults = function(){
        var els = $(".result-op").get().concat( $(".result").get() ),
        alaEls = {};

        for(var i = 0, name, el; el = els[i]; i++ ){
            if(name = el.getAttribute("tpl")){
                if( alaEls[name] ){
                    alaEls[name].push(el);
                }else{
                    alaEls[name] = [el];
                }
            }
        }
        return alaEls;
    },

    // 入口事件队列
    readyedHandlers = [],

    //销毁函数列表，每项内容为
    //{obj:instance, fn: fn}
    //每项执行fn后即删除
    disposeOnceHandlers = [],

    //每项格式同disposeOnceHandlers
    //每项执行后仍保留
    //即每次销毁实例时都执行一次
    disposeAlwaysHandlers = [],

    currentSetupContainer = null,

    // merge在bds.ready前的队列
    mergeHandlers = [],

    // 阿拉丁实例构造函数
    Ala = A._Aladdin = function(){
        this.p1 = 0;
        this.mu = null;
    };

    A.merge = function(tplname, fn){
        mergeHandlers.push({tplname: tplname, fn: fn});
    };

    // 阿拉丁入口函数
    A.init = A.setup = function(k, v){

        // 页面可能存在的空 init
        if( k === undefined || k === null){
            return;
        }

        var object, container = currentSetupContainer || getCurrentAladdin();
        if( !container){
            return;
        }

        object = {container: container};

        if(typeof k == "function"){
            object.handler = k;

        }else if(typeof k == 'object'){
            object.data = k;

        }else{
            object.data = {};
            object.data[k] = v;
        }

        readyedHandlers.push( object );
    };

    // 注册每次销毁均执行的函数
    A.addDisposeHandler = function(item){
        disposeAlwaysHandlers.push(item);
    };

    //全局阿拉丁销毁函数，在删除阿拉丁dom节点前调用
    A.dispose = function(){
        // 执行阿拉丁实例dispose队列
        while(disposeOnceHandlers.length){
            var d = disposeOnceHandlers.shift();
            exec(d.fn, d.obj);
        }
        // 顺序执行销毁函数
        var handlers = disposeAlwaysHandlers;
        for(var i=0;i<handlers.length;i++){
            var d = handlers[i];
            exec(d.fn, d.obj);
        }
    };

    // 遍历执行所有阿拉丁实例
    bds.ready(function(){

        // 将所有的merge队列转换为setup队列
        if( mergeHandlers.length ){
            var results = getResults();
            for(var i = 0, item; item = mergeHandlers[i]; i++){
                var els = results[item.tplname];
                if(els){
                    for(var j = 0, el; el = els[j]; j++){
                        currentSetupContainer = el;
                        item.fn();
                        currentSetupContainer = null;
                    }
                }
            }
        }

        // 整理出的每个Aladding JS数据
        var groupData = [],
        getGroupData = function(el){
            if(!isNaN(el.initIndex)){
                return  groupData[ el.initIndex * 1];
            }
            var data = { data:{}, handlers: [], container: el };
            groupData.push(data);
            el.initIndex = groupData.length - 1;
            return data;
        };

        // 整理setup队列顺序
        for(var i = 0, item; item = readyedHandlers[i]; i++){
            var elData = getGroupData(item.container);

            if( item.data ){
                for(var k in item.data){
                    if(item.data.hasOwnProperty(k)){
                        elData.data[k] = item.data[k];
                    }
                }

            }else if (item.handler){
                elData.handlers.push( item.handler );
            }
        }

        // 遍历所有的setup
        for(var i = 0, item; item = groupData[i]; i++){
            var fn,
            sTime,
            eTime,
            obj = {},
            ala = new Ala();

            ala.data = item.data;
            ala.container = item.container;
            ala._init();
            A.list.push(ala);

            // 执行setup队列
            sTime = new Date();
            while( fn = item.handlers.shift() ){
                exec(fn, ala);
                //执行完fn后，如果示例上定义了dispose方法
                //则将其保存到队列中
                if(typeof ala.dispose == 'function'){
                    disposeOnceHandlers.push({
                        obj:ala,
                        fn: ala.dispose
                    });
                    ala.dispose = null;
                }
            }
            eTime = new Date();

            // 统计执行时间
            obj = { srcid: ala.srcid };
            obj.tpl  = ala.container.getAttribute('tpl');
            obj.time = eTime - sTime;
            A.loadTimes.push( obj );

            $.each( A._Aladdin.fixs, function(i, f){
                f.call(ala, ala);
            });
        }

    });

    Ala.prototype = {

        //初始化实例属性
        _init: function() {
            var attrs = getJson(this.container.getAttribute('data-click'));
            this.p1 = attrs.p1 || this.container.id;
            this.mu = attrs.mu || this.container.getAttribute('mu');
            this.srcid = attrs.rsv_srcid || this.container.getAttribute('srcid');
        }
    };


})();
</script><style type="text/css">#MsnDialog.ad, #MyMoveAd, #QQ_Full, #RightAd1, #ad-SNSSplashAd, #ad6cn, #adBody01, #adBody02, #adBody03, #adBody04, #adBody06, #adBody07, #adLeftFloat, #adRightFloat, #ad_box1, #ad_box2, #ad_full, #ad_headerbanner, #ads_c_tpc, #ads_top_video, #adtop1, #adx_cggp, #crazy_ad_float, #crazy_ad_layer, #cs_left_couplet, #cs_right_couplet, #doyoo_mon_mask, #doyoo_monitor, #duilian_left, #duilian_right, #eis_pad1, #eis_pad2, #floatAd, #floatad-winpop, #fwin_popad_7ree, #gg300, #googleAdIndexTop, #haoetv1, #js-ad-map, #js_ads_banner_top, #js_ads_banner_top_slide, #kfpopupDiv, #leftCouple, #left_couple, #left_down_float_ad, #left_top_ad, #lovexin1, #lovexin11, #lovexin12, #lovexin13, #lovexin14, #lovexin2, #mbjx_ad, #miaov_float_layer, #micast_ads, #movieInfoRight, #my-adsFPR, #netease_mail_footer, #olfullad, #overture_ads_bottom_td, #overture_ads_top_td, #popup.t, #ptcmsad1, #qj960a, #qj960b, #results.content-main > .eLeft, #rightCouple, #right_couple, #right_down_float_ad, #shareman_ad, #sitefocus.focus, #snActive-wrap, #tanx-con-1, #tanx-fold-main, #textggs, #top_ads0, #toperAd2, #tr_ad1, #tr_ad10, #tr_ad11, #tr_ad2, #tr_ad3, #tr_ad4, #tr_ad5, #tr_ad6, #tr_ad7, #tr_ad8, #tr_ad9, #tripadvisor-ad, #ts-businessAds, #xinnxi, #xinxi, #zds_ad, .a_cn, .a_fl, .a_fr, .a_p, .a_pb, .a_pr, .ad-above-footer, .ad-below-adjacent-post, .ad-below-header-menu, .ad-below-post-title, .ad-below-related-post, .ad-left-down, .ad-left-top, .ad-right-down, .ad-right-top, .ad250left, .ad250right, .ad300left, .ad336left, .ad990x130, .ad990x90, .ad_couplebanner, .ad_fixed, .ad_footerbanner, .ad_headerbanner, .ad_hf, .ad_home_current, .ad_midd, .ad_thread, .adsense160, .adsense200, .adsoho, .assort-ad, .banner-ad-section, .banner-site, .below_ads, .bm.a_c, .bn728-93, .bottom-adv, .bottomSponsor, .bus_adsbox, .cari-ads, .chat-right-ad, .chat-top-ad, .comiis_adbox, .con_ad, .content_ad_300, .customSlideshow-ad-below, .d_slidebanner, .gg1000, .gg_300, .gg_950, .gg_960, .gg_full, .ggad, .ggbox, .ggdistich, .gggtop, .ggpost-below, .ggtop, .google_adsense2, .gpt_ads_box, .index_alert_gg, .indexad2, .indexad3, .indexad4, .iqshwad-div, .it618_firstad_flex, .kf_qycn_com_cckf_welcomebox, .leftadv, .lol-ad, .lol_ad, .lyzm-prevent, .menutab_ad, .ml_ad1, .ml_ad3, .ml_ad5, .mlad, .movie-advert-link, .pagead_3, .player-bottom-gg, .readerAd, .room-ad-bottom, .room-ad-top, .room-ad-video-down, .scupioadslot, .showHaoSouBanner, .sxAdBox, .theme_custom_slidebox-ad-below, .tipadds, .tmall_ad_container, .top-read-ad, .topSponsor, .twavt-ads, .wf_ad_block, .widget_ad_sidebar, .widget_adbox, .wp.a_f, .wp.a_h, .wumii-bottom-popup, .wumii-widget-ad, .wzad, .yd_ad, .yd_ad1, .yd_ad2, .yd_ad3, .yd_ad5, .yd_ad6, div#ad_id, #A9AdsMiddleBoxTop, #A9AdsOutOfStockWidgetTop, #A9AdsServicesWidgetTop, #AD-300x250, #AD-300x250-1, #AD-300x250-2, #AD-300x250-3, #AD-HOME-LEFT, #AD001, #AD1line, #AD2line, #AD300Right, #AD300_VAN, #AD300x250, #AD300x600, #AD728Top, #ADEXPERT_PUSHDOWN, #ADEXPERT_RECTANGLE, #ADInterest, #ADNETwallBanner1, #ADNETwallBanner2, #ADSLOT_1, #ADSLOT_2, #ADSLOT_3, #ADSLOT_4, #ADSLOT_SKYSCRAPER, #ADS_2, #ADSlideshow, #ADSpro, #ADV120x90, #ADVERTISE_HERE_ROW, #ADVERTISE_RECTANGLE1, #ADVERTISE_RECTANGLE2, #ADVTLEFT1, #ADVTLEFT2, #ADVTRIGHT1, #ADV_VIDEOBOX_2_CNT, #ADVleaderboard, #AD_160, #AD_300, #AD_468x60, #AD_C, #AD_CONTROL_13, #AD_CONTROL_22, #AD_CONTROL_28, #AD_CONTROL_29, #AD_CONTROL_8, #AD_G, #AD_ROW, #AD_Top, #AD_Zone, #AD_banner, #AD_banner_bottom, #AD_gallery, #AD_google, #AD_half, #AD_newsblock, #AD_rectangle, #AD_rr_a, #AD_text, #ADbox, #ADgoogle_newsblock, #ADoverThePlayer, #ADsmallWrapper, #AFF_popup, #APC_ads_details, #AUI_A9AdsMiddleBoxTop, #AUI_A9AdsWidgetAdsWrapper, #Ad-0-0-Slider, #Ad-0-1-Slider, #Ad-1-0-Slider, #Ad-1-1-Slider, #Ad-1-2-Slider, #Ad-3-Slider, #Ad-4-Slider, #Ad-5-2-Slider, #Ad-8-0-Slider, #Ad-9-0-Slider, #Ad-Container, #Ad-Top, #Ad160x600, #Ad160x600_0_adchoice, #Ad300x145, #Ad300x250, #Ad300x250_0, #Ad300x600_0_adchoice, #Ad3Left, #Ad3Right, #Ad3TextAd, #Ad728x90, #Ad990, #AdAboveGame, #AdArea, #AdAreaH, #AdAuth1, #AdAuth2, #AdAuth3, #AdAuth4, #AdBanner, #AdBannerSmallContainer, #AdBanner_F1, #AdBanner_S, #AdBar, #AdBar1, #AdBigBox, #AdBlock, #AdBlockBottomSponsor, #AdBottomLeader, #AdBottomRight, #AdBox160, #AdBox2, #AdBox300, #AdBox728, #AdBoxMoreGames, #AdButtons, #AdColumn, #AdContainer, #AdContainerTop, #AdContentModule_F, #AdContent_0_0_pnlDiv, #AdControl_TowerAd, #AdDetails_GoogleLinksBottom, #AdDetails_InsureWith, #AdDetails_SeeMoreLink, #AdDisclaimer, #AdDisplay_LongLink, #AdDisplay_TallLink, #AdDiv, #AdExtraBlock, #AdFeedbackLinkID_lnkItem, #AdFoxDiv, #AdFrame1, #AdFrame2, #AdFrame4, #AdHeader, #AdHouseRectangle, #AdImage, #AdIndexTower, #AdLayer1, #AdLayer2, #AdLeaderboard2RunofSite, #AdLeaderboardBottom, #AdLeaderboardTop, #AdLocationMarketPage, #AdMPUHome, #AdMediumRectangle1300x250, #AdMediumRectangle2300x250, #AdMiddle, #AdMobileLink, #AdPanel, #AdPanelBigBox, #AdPanelLogo, #AdPopUp, #AdRectangle, #AdRectangleBanner, #AdSense-Skyscraper, #AdSense1, #AdSense2, #AdSense3, #AdSenseBottomAds, #AdSenseDiv, #AdSenseMiddleAds, #AdSenseResults1_adSenseSponsorDiv, #AdSenseTopAds, #AdServer, #AdShopSearch, #AdShowcase, #AdShowcase_F, #AdShowcase_F1, #AdSky23, #AdSkyscraper, #AdSlot_AF-Right-Multi, #AdSpaceLeaderboard, #AdSpacing, #AdSponsor_SF, #AdSpotMovie, #AdSquare02, #AdSubsectionShowcase_F1, #AdTaily_Widget_Container, #AdTargetControl1_iframe, #AdTop, #AdTopBlock, #AdTopLeader, #AdWidgetContainer, #AdZone1, #AdZone2, #Ad_976x105, #Ad_BelowContent, #Ad_Block, #Ad_Center1, #Ad_Premier, #Ad_Right1, #Ad_RightBottom, #Ad_RightTop, #Ad_TopLeaderboard, #Adbanner, #Adc1_AdContainer, #Adc2_AdContainer, #Adc3_AdContainer, #AdcBB_AdContainer, #Adcode, #Adrectangle, #Ads-C, #Ads-D-728x90-hori, #Ads270x510-left, #Ads470by50, #AdsBannerTop, #AdsBottomContainer, #AdsBottomIframe, #AdsCarouselBoxArea, #AdsContainerTop, #AdsContent, #AdsContent_SearchShortRecB_UPSSR, #AdsDiv, #AdsFrame, #AdsHome2, #AdsLeader, #AdsLeft_1, #AdsPlayRight_1, #AdsRight, #AdsShowCase, #AdsTopContainer, #AdsVideo250, #AdsWrap, #Ads_BA_BUT_box, #Ads_BA_CAD, #Ads_BA_CAD2, #Ads_BA_CAD2_Text, #Ads_BA_CAD_box, #Ads_BA_FLB, #Ads_BA_SKY, #Ads_CAD, #Ads_OV_BS, #Ads_Special, #Ads_TFM_BS, #Ads_google_01, #Ads_google_02, #Ads_google_03, #Ads_google_04, #Ads_google_05, #Adsense300x250, #Adtag300x250Bottom, #Adtag300x250Top, #Adv-div, #Adv10, #Adv11, #Adv8, #Adv9, #AdvArea, #AdvBody, #AdvContainer, #AdvContainerBottom, #AdvContainerMiddleRight, #AdvContainerTopCenter, #AdvContainerTopRight, #AdvFooter, #AdvFrame1, #AdvHead, #AdvHeader, #Adv_Footer, #Adv_Main_content, #Advert1, #AdvertMPU23b, #AdvertPanel, #AdvertText, #AdvertiseFrame, #Advertisement1, #AdvertisementRightColumnRectangle, #Advertisements, #AdvertisingDiv_0, #AdvertisingLeaderboard, #AdvertismentHomeTopRight, #Advertorial, #Advertorials, #AdvertsBottom, #AdvertsBottomR, #Adverts_AdDetailsBottom_300x600, #Adverts_AdDetailsMiddle_300x250, #ArticleBottomAd, #BANNER_160x600, #BANNER_300x250, #BANNER_728x90, #BBCPH_MCPH_MCPH_P_ArticleAd1, #BBCPH_MCPH_MCPH_P_OasAdControl1Panel, #BBCPH_MCPH_MCPH_P_OasAdControl2Panel, #BBCPH_MCPH_MCPH_SponsoredLinks1, #BBoxAd, #BDV_fullAd, #BackgroundAdContainer, #Banner300x250Module, #Banner728x90, #BannerAd, #BannerAds, #BannerAdvert, #BannerAdvertisement, #BannerXGroup, #BelowFoldAds, #BigBoxAd, #BigboxAdUnit, #BillBoardAdd, #BodyAd, #BodyTopAds, #BotAd, #Bottom468x60AD, #BottomAd0, #BottomAdContainer, #BottomAdSpacer, #BottomAds, #BottomPageAds, #BrokerBox-AdContainer, #ButtonAd, #CONTENTAD, #CSpromo120x90, #ClickPop_LayerPop_Container, #ClickStory_ViewAD1, #ClickStory_ViewRightAD2, #CommonHeaderAd, #CompanyDetailsNarrowGoogleAdsPresentationControl, #CompanyDetailsWideGoogleAdsPresentationControl, #ContentAd, #ContentAd1, #ContentAd2, #ContentAdPlaceHolder1, #ContentAdPlaceHolder2, #ContentAdView, #ContentAdXXL, #ContentAdtagRectangle, #ContentPlaceHolder1_adds, #ContentPlaceHolder1_advertControl1_advertLink, #ContentPlaceHolder1_advertControl3_advertLink, #ContentPlaceHolder1_pnlGoogleAds, #ContentPolepositionAds_Result, #Content_CA_AD_0_BC, #Content_CA_AD_1_BC, #ConversationDivAd, #CornerAd, #CountdownAdvert, #DARTad300x250, #DEFAULT_ADV4_SWF, #DFM-adPos-bottomline, #DFPAD_MR, #DFP_in_article_mpu, #DFP_top_leaderboard, #DartAd300x250, #DartAd990x90, #DealsPageSideAd, #DivAd, #DivAd1, #DivAd2, #DivAd3, #DivAdA, #DivAdB, #DivAdC, #DivAdEggHeadCafeTopBanner, #DivAdForumSplitBottom, #DivMsnCamara, #DivTopAd, #DividerAd, #DynamicAD, #FFN_imBox_Container, #FIN_300_250_position2_ad, #FIN_300_x_250_600_position2_ad, #FIN_300x250_pos1_ad, #FIN_300x80_facebook_ad, #FIN_468x60_sponsor_ad, #FIN_640x60_promo_ad, #FIN_728_90_leaderboard_ad, #FIN_ad_300x100_pos_1, #FIN_videoplayer_300x250ad, #FRONTADVT2, #FRONTADVT3, #FRONTADVT4, #FRONTADVT5, #FRONTADVT8, #FooterAd, #FooterAdBlock, #FooterAdContainer, #ForumSponsorBanner, #Freeforums-AdS-footer-728x90, #Freeforums-AdS-header-728x90, #FrontPageRectangleAd, #GOOGLEADS_BOT, #GOOGLEADS_CENTER, #GOOGLE_ADS_13, #GOOGLE_ADS_151, #GOOGLE_ADS_16, #GOOGLE_ADS_2, #GOOGLE_ADS_49, #GOOGLE_ADS_56, #GOOGLE_ADS_94, #GameMediumRectangleAD, #GamePageAdDiv, #GoogleADsense, #GoogleADthree, #GoogleAd, #GoogleAd1, #GoogleAd2, #GoogleAd3, #GoogleAdExploreMF, #GoogleAdRight, #GoogleAdTop, #GoogleAds250X200, #GoogleAdsPlaceHolder, #GoogleAdsPresentationControl, #GoogleAdsense, #GoogleAdsenseMerlinWrapper, #GoogleLeaderBoardAdUnit, #GoogleLeaderBoardAdUnitSeperator, #GoogleRelatedAds, #GoogleSponsored, #Google_Adsense_Main, #HALExchangeAds, #HALHouseAd, #HB_News-ad, #HEADERAD, #HOME_TOP_RIGHT_BOXAD, #HP_adUnits, #H_Ad_728x90, #H_Ad_Wrap, #HeaderAD, #HeaderAd, #HeaderAdBlock, #HeaderAdSidebar, #HeaderAdsBlock, #HeaderAdsBlockFront, #HeaderBannerAdSpacer, #HeaderTextAd, #HeroAd, #HomeAd1, #HomeBannerAd, #Home_AdSpan, #HomepageAdSpace, #HorizontalAd, #HouseAd, #HouseAdInsert, #ID_Ad_Sky, #IM_AD, #IN_HOUSE_AD_SWITCHER_0, #IframeAdBannerSmallContainer, #ImageAdSideColumn, #ImageRotaAreaAD, #IslandAd_DeferredAdSpacediv, #JobsearchResultsAds, #Journal_Ad_125, #Journal_Ad_300, #JuxtapozAds, #KH-contentAd, #LB_Row_Ad, #LS-google-ad, #LargeRectangleAd, #LeaderTop-ad, #LeaderboardAdvertising, #LeaderboardNav_ad_placeholder, #LeftAd, #LeftAd1, #LeftAdF1, #LeftAdF2, #LeftSideBarAD, #LftAd, #LittleAdvert, #LoungeAdsDiv, #LovelabAdoftheDay, #LowerContentAd, #MAINAD-box, #MPUAdSpace, #MPUadvertising, #MPUadvertisingDetail, #M_AD, #MainAd, #MainAd1, #MainContent_ucTopRightAdvert, #MainHeader1_FRONTADVT10, #MainHeader1_FRONTADVT11, #MainRightStrip1_RIGHTADVT2, #MainRightStrip1_RIGHTADVT3, #MainRightStrip1_RIGHTADVT4, #MainRightStrip1_RIGHTADVT5, #MainSponsoredLinks, #MastheadAd, #MediumRectangleAD, #MidPageAds, #MiddleRightRadvertisement, #Module-From_Advertisers, #MyAdHeader, #MyAdSky, #NavAD, #Nightly_adContainer, #NormalAdModule, #OAS2, #OASMiddleAd, #OASRightAd, #OAS_AD_TOPRIGHT, #OAS_Top, #OAS_posBottom, #OAS_posRight, #OAS_posTopRight, #OpenXAds, #OverrideAdArea, #PPX_imBox_Container, #PREFOOTER_LEFT_BOXAD, #PREFOOTER_RIGHT_BOXAD, #PageLeaderAd, #PaneAdvertisingContainer, #PhotoAd1, #PostSponsorshipContainer, #PreRollAd, #PushDownAd, #RHS2Adslot, #RadAdSkyscraper, #RadAd_Skyscraper, #RelevantAds, #RgtAd1, #RhsIsland_DeferredAdSpacediv, #RightAd, #RightAdBlock, #RightAdSpace, #RightAdvertisement, #RightBottom300x250AD, #RightColumn125x125AD, #RightColumnAdContainer, #RightColumnSkyScraperAD, #RightNavTopAdSpot, #RightRailSponsor, #RightSponsoredAd, #RollOutAd970x66, #RollOutAd970x66iframe, #SE20-ad-container, #SE_ADLINK_LAY_gd, #SIDEMENUAD, #SIM_ad_300x100_homepage_pos1, #SIM_ad_300x250-600_pos1, #SIM_ad_300x250_pos2, #SIM_ad_468x60_homepage_pos1, #SIM_ad_468x60_homepage_pos2, #SIM_ad_468x60_homepage_pos3, #SIM_ad_728x90_bottom, #SRPadsContainer, #ScoreboardAd, #SearchAd_PlaceHolder, #SearchAdsBottom, #SearchAdsTop, #Section-Ads, #SectionAd300-250, #SectionSponsorAd, #ServerAd, #SideAdMpu, #SideBarAdWidget, #SideMpuAdBar, #SidebarAdContainer, #SkyAd, #SkyscraperAD, #SpecialAds, #Spons-Link, #SponsorBarWrap, #SponsoredAd, #SponsoredAds, #SponsoredLinks, #SponsoredResultsTop, #SponsorsAds, #TDads, #TL_footer_advertisement, #TOPADS, #TOP_ADROW, #TOP_RIGHT_BOXAD, #TPVideoPlayerAd300x250, #Tadspacecbar, #Tadspacefoot, #Tadspacehead, #Tadspacemrec, #TextLinkAds, #ThemeSection_adbanner2, #ThemeSection_adbanner3, #ThreadAd, #TipTopAdSpace, #TitleAD, #Top-Ad-Container, #Top468x60AD, #TopADs, #TopAd, #TopAd0, #TopAdBox, #TopAdContainer, #TopAdDiv, #TopAdPlacement, #TopAdPos, #TopAdTable, #TopAdvert, #TopBannerAd, #TopCenterAdUnit, #TopGoogleCustomAd, #TopRightRadvertisement, #TopSideAd, #TopTextAd, #VM-MPU-adspace, #VM-footer-adspace, #VM-footer-adwrap, #VM-header-adspace, #VM-header-adwrap, #VertAdBox, #VertAdBox0, #WNAd1, #WNAd103, #WNAd17, #WNAd20, #WNAd41, #WNAd43, #WNAd46, #WNAd47, #WNAd49, #WNAd52, #WNAd63, #WarningCodecBanner, #WelcomeAd, #WindowAdHolder, #WordFromSponsorAdvertisement, #XEadLeaderboard, #XEadSkyscraper, #YahooAdParentContainer, #YahooAdsContainer, #YahooAdsContainerPowerSearch, #YahooContentAdsContainerForBrowse, #YahooSponsoredResults, #Zergnet, #\5f _mom_ad_12, #\5f _mom_ad_2, #a4g-floating-ad, #a_ad10Sp, #a_ad11Sp, #abHeaderAdStreamer, #ab_adblock, #abc-AD_topbanner, #about_adsbottom, #above-comments-ad, #above-fold-ad, #above-footer-ads, #aboveAd, #aboveGbAd, #aboveNodeAds, #aboveplayerad, #abovepostads, #acAdContainer, #acm-ad-tag-300x250-atf, #acm-ad-tag-300x250-btf, #acm-ad-tag-728x90-atf, #acm-ad-tag-728x90-btf, #ad-0, #ad-1, #ad-1000x90-1, #ad-1050, #ad-109, #ad-118, #ad-120-left, #ad-120x600-1, #ad-120x600-other, #ad-120x600-sidebar, #ad-120x60Div, #ad-125x125, #ad-13, #ad-133, #ad-143, #ad-160, #ad-160-long, #ad-160x600, #ad-160x600-sidebar, #ad-160x600-wrapper, #ad-162, #ad-17, #ad-170, #ad-180x150-1, #ad-19, #ad-197, #ad-2, #ad-2-160x600, #ad-200x200_newsfeed, #ad-21, #ad-213, #ad-220x90-1, #ad-230x100-1, #ad-240x400-1, #ad-240x400-2, #ad-250, #ad-250x300, #ad-28, #ad-29, #ad-3, #ad-3-300x250, #ad-300, #ad-300-250, #ad-300-additional, #ad-300-detail, #ad-300-sidebar, #ad-300X250-2, #ad-300a, #ad-300b, #ad-300x-container, #ad-300x250, #ad-300x250-01, #ad-300x250-02, #ad-300x250-1, #ad-300x250-2, #ad-300x250-b, #ad-300x250-right, #ad-300x250-right0, #ad-300x250-sidebar, #ad-300x250-wrapper, #ad-300x250Div, #ad-300x250_top, #ad-300x40-1, #ad-300x40-2, #ad-300x40-5, #ad-300x60-1, #ad-32, #ad-320, #ad-336, #ad-350, #ad-37, #ad-376x280, #ad-4, #ad-4-300x90, #ad-5-images, #ad-55, #ad-63, #ad-635x40-1, #ad-655, #ad-7, #ad-728, #ad-728-90, #ad-728x90, #ad-728x90-1, #ad-728x90-leaderboard-top, #ad-728x90-top, #ad-728x90-top0, #ad-732, #ad-734, #ad-74, #ad-88, #ad-88-wrap, #ad-970, #ad-98, #ad-a, #ad-a1, #ad-abs-b-0, #ad-abs-b-1, #ad-abs-b-10, #ad-abs-b-2, #ad-abs-b-3, #ad-abs-b-4, #ad-abs-b-5, #ad-abs-b-6, #ad-abs-b-7, #ad-absolute-160, #ad-ads, #ad-adsensemedium, #ad-advertorial, #ad-affiliate, #ad-area, #ad-around-the-web, #ad-article, #ad-article-in, #ad-aside-1, #ad-atf-mid, #ad-atf-top, #ad-background, #ad-ban, #ad-banner, #ad-banner-1, #ad-banner-970, #ad-banner-980, #ad-banner-atf, #ad-banner-body-top, #ad-banner-bottom, #ad-banner-image, #ad-banner-top, #ad-banner-wrap, #ad-bar, #ad-base, #ad-beauty, #ad-below-content, #ad-bg, #ad-big, #ad-bigbox, #ad-bigsize, #ad-billboard, #ad-billboard-atf, #ad-billboard-bottom, #ad-blade, #ad-block, #ad-block-125, #ad-block-bottom, #ad-block-container, #ad-border, #ad-bottom, #ad-bottom-300x250, #ad-bottom-banner, #ad-bottom-right-container, #ad-bottom-wrapper, #ad-bottomright, #ad-box, #ad-box-1, #ad-box-2, #ad-box-bottom, #ad-box-first, #ad-box-second, #ad-box1, #ad-box2, #ad-boxATF, #ad-boxes, #ad-br-container, #ad-bs, #ad-btf-bot, #ad-btm, #ad-buttons, #ad-campaign, #ad-carousel, #ad-case, #ad-center, #ad-circfooter, #ad-code, #ad-col, #ad-colB-1, #ad-column, #ad-container, #ad-container-1, #ad-container-2, #ad-container-adaptive-1, #ad-container-adaptive-3, #ad-container-fullpage, #ad-container-inner, #ad-container-leaderboard, #ad-container-mpu, #ad-container-outer, #ad-container-overlay, #ad-container1, #ad-contentad, #ad-cube-Bottom, #ad-cube-Middle, #ad-cube-sec, #ad-cube-top, #ad-desktop-wrap, #ad-discover, #ad-display-ad, #ad-div-leaderboard, #ad-double-spotlight-container, #ad-drawer, #ad-e-container, #ad-ear, #ad-extra-comments, #ad-extra-flat, #ad-f-container, #ad-featured-right, #ad-first-post, #ad-five, #ad-five-75x50s, #ad-flex-first, #ad-flex-top, #ad-footer, #ad-footer-728x90, #ad-footprint-160x600, #ad-for-map, #ad-frame, #ad-framework-top, #ad-front-btf, #ad-front-footer, #ad-front-page-160x600-placeholder, #ad-front-sponsoredlinks, #ad-full-width, #ad-fullbanner-btf, #ad-fullbanner-outer, #ad-fullbanner2, #ad-fullbanner2-billboard-outer, #ad-fullwidth, #ad-giftext, #ad-globalleaderboard, #ad-google-chrome-sidebar, #ad-googleAdSense, #ad-gpt-bottomrightrec, #ad-gpt-leftrec, #ad-gpt-rightrec, #ad-gutter-left, #ad-gutter-right, #ad-halfpage, #ad-header, #ad-header-728x90, #ad-header-left, #ad-header-mad, #ad-header-mobile, #ad-header-right, #ad-holder, #ad-homepage-content-well, #ad-homepage-top-wrapper, #ad-horizontal, #ad-horizontal-header, #ad-horizontal-top, #ad-idreammedia, #ad-img, #ad-in-post, #ad-index, #ad-inner, #ad-inside1, #ad-inside2, #ad-interstitial-wrapper, #ad-introtext, #ad-label, #ad-label2, #ad-large-header, #ad-lb, #ad-lb-secondary, #ad-ldr-spot, #ad-lead, #ad-leader, #ad-leader-atf, #ad-leader-container, #ad-leaderboard, #ad-leaderboard-1, #ad-leaderboard-1-container, #ad-leaderboard-2, #ad-leaderboard-2-container, #ad-leaderboard-bottom, #ad-leaderboard-container, #ad-leaderboard-footer, #ad-leaderboard-spot, #ad-leaderboard-top, #ad-leaderboard-top-container, #ad-leaderboard_bottom, #ad-leadertop, #ad-left, #ad-left-sidebar-ad-1, #ad-left-sidebar-ad-2, #ad-left-sidebar-ad-3, #ad-left-timeswidget, #ad-links-content, #ad-list-row, #ad-lrec, #ad-main, #ad-main-bottom, #ad-main-top, #ad-makeup, #ad-manager, #ad-manager-ad-bottom-0, #ad-manager-ad-top-0, #ad-medium, #ad-medium-lower, #ad-medium-rectangle, #ad-medrec, #ad-medrec_premium, #ad-megaban2, #ad-megasky, #ad-mid, #ad-mid-rect, #ad-middle, #ad-middlethree, #ad-middletwo, #ad-midpage, #ad-minibar, #ad-module, #ad-mpu, #ad-mpu-topRight-container, #ad-mpu-warning, #ad-mpu1-spot, #ad-mpu2, #ad-mpu2-spot, #ad-mpu600-right-container, #ad-mrec, #ad-mrec2, #ad-new, #ad-news-sidebar-300x250-placeholder, #ad-north, #ad-north-base, #ad-northeast, #ad-one, #ad-other, #ad-output, #ad-overlay, #ad-page-1, #ad-page-sky-300-a1, #ad-page-sky-300-a2, #ad-page-sky-left, #ad-pan3l, #ad-panel, #ad-pencil, #ad-placard, #ad-placeholder, #ad-placement, #ad-plate, #ad-popup, #ad-popup1, #ad-position-a, #ad-post, #ad-push, #ad-pushdown, #ad-r, #ad-rbkua, #ad-rec-atf, #ad-rec-btf-top, #ad-recommend, #ad-rect, #ad-rectangle, #ad-rectangle-flag, #ad-rectangle1, #ad-rectangle1-outer, #ad-rectangle2, #ad-rectangle3, #ad-region-1, #ad-results, #ad-rian, #ad-right, #ad-right-3, #ad-right-sidebar, #ad-right-sidebar-ad-1, #ad-right-sidebar-ad-2, #ad-right-skyscraper-container, #ad-right-top, #ad-right2, #ad-right3, #ad-righttop, #ad-ros-atf-300x90, #ad-ros-btf-300x90, #ad-rotator, #ad-row, #ad-row-1, #ad-s1, #ad-safe, #ad-secondary-sidebar-1, #ad-section, #ad-separator, #ad-shop, #ad-side, #ad-side-text, #ad-sidebar, #ad-sidebar-1, #ad-sidebar-2, #ad-sidebar-3, #ad-sidebar-300x80, #ad-sidebar-btf, #ad-sidebar-container, #ad-sidebar-mad, #ad-sidebar-mad-wrapper, #ad-sidebar-right_300-1, #ad-sidebar-right_300-2, #ad-sidebar-right_300-3, #ad-sidebar-right_bitgold, #ad-sidebar1, #ad-sidebar2, #ad-sidebarleft-bottom, #ad-sidebarleft-top, #ad-single-spotlight-container, #ad-skin, #ad-sky, #ad-sky-atf, #ad-sky-btf, #ad-skyscraper, #ad-skyscraper-feedback, #ad-skyscraper1-outer, #ad-sla-sidebar300x250, #ad-slot-1, #ad-slot-2, #ad-slot-4, #ad-slot-right, #ad-slot1, #ad-slot4, #ad-slug-wrapper, #ad-small-banner, #ad-software-description-300x250-placeholder, #ad-software-sidebar-300x250-placeholder, #ad-space, #ad-space-1, #ad-space-2, #ad-space-big, #ad-special, #ad-splash, #ad-sponsored-traffic, #ad-sponsors, #ad-spot, #ad-spot-bottom, #ad-spot-one, #ad-springboard-300x250, #ad-squares, #ad-standard-wrap, #ad-story-bottom-in, #ad-story-bottom-out, #ad-story-right, #ad-story-top, #ad-stripe, #ad-tab, #ad-tail-placeholder, #ad-tape, #ad-target, #ad-target-Leaderbord, #ad-teaser, #ad-techwords, #ad-text, #ad-textad-single, #ad-three, #ad-tlr-spot, #ad-top, #ad-top-250, #ad-top-300x250, #ad-top-728, #ad-top-banner, #ad-top-banner-placeholder, #ad-top-leaderboard, #ad-top-left, #ad-top-lock, #ad-top-right, #ad-top-right-container, #ad-top-text-low, #ad-top-wrap, #ad-top-wrapper, #ad-tower, #ad-tower1, #ad-trailerboard-spot, #ad-two, #ad-typ1, #ad-unit, #ad-uprrail1, #ad-video, #ad-west, #ad-wide-leaderboard, #ad-wrap, #ad-wrap-right, #ad-wrapper, #ad-wrapper-728x90, #ad-wrapper-left, #ad-wrapper-right, #ad-wrapper1, #ad-yahoo-simple, #ad-zone-1, #ad-zone-2, #ad-zone-inline, #ad001, #ad002, #ad01, #ad02, #ad1-468x400, #ad1-home, #ad1-placeholder, #ad1-wrapper, #ad1006, #ad101, #ad10Sp, #ad11, #ad11Sp, #ad120x600, #ad120x600container, #ad120x60_override, #ad125B, #ad125BL, #ad125BR, #ad125TL, #ad125TR, #ad125x125, #ad160, #ad160-2, #ad160600, #ad160Container, #ad160Wrapper, #ad160a, #ad160x600, #ad160x600right, #ad180, #ad1Sp, #ad1_holder, #ad1_top-left, #ad2-home, #ad2-label, #ad2-original-placeholder, #ad250, #ad260x60, #ad2CONT, #ad2Sp, #ad2_footer, #ad2_iframe, #ad2_inline, #ad2gameslayer, #ad300, #ad300-250, #ad300-title, #ad300250top, #ad300IndexBox, #ad300X250, #ad300_250, #ad300_a, #ad300_x_250, #ad300b, #ad300c, #ad300text, #ad300top, #ad300x100Middle, #ad300x150, #ad300x250, #ad300x250Module, #ad300x250_336x280_300x600_336x850, #ad300x250_336x280_bottom, #ad300x250_callout, #ad300x250box, #ad300x250box2, #ad300x250c, #ad300x50, #ad300x60, #ad300x600, #ad300x600_callout, #ad31, #ad32, #ad330x240, #ad336, #ad336atf, #ad336iiatf, #ad336x280, #ad375x85, #ad3Article, #ad3small, #ad468, #ad468_hidden, #ad468x60, #ad468x60-story, #ad468x60_top, #ad470, #ad508x125, #ad520x85, #ad526x250, #ad5_inline, #ad6, #ad600, #ad600x90, #ad650, #ad720x90bot, #ad728, #ad72890, #ad72890foot, #ad728Bottom, #ad728Box, #ad728BoxBtm, #ad728Header, #ad728Mid, #ad728Top, #ad728Wrapper, #ad728X90, #ad728foot, #ad728h, #ad728mid, #ad728top, #ad728x90, #ad728x90_1, #ad728x90asme, #ad728x90box, #ad76890topContainer, #ad768top1, #ad90, #ad97090, #adAd, #adBadges, #adBanner, #adBanner1, #adBanner10, #adBanner120x600, #adBanner160x600, #adBanner160x610, #adBanner2, #adBanner3, #adBanner336x280, #adBanner4, #adBanner728, #adBanner728_bot, #adBanner9, #adBannerBottom, #adBannerBreaking, #adBannerHeader, #adBannerSpacer, #adBannerTable, #adBannerTop, #adBannerWrap, #adBannerWrapperFtr, #adBar, #adBelt, #adBlock01, #adBlock125, #adBlockBanner, #adBlockContainer, #adBlockContent, #adBlockOverlay, #adBlockTop, #adBlocks, #adBottbanner, #adBottom, #adBox, #adBox11, #adBox16, #adBox350, #adBox390, #adBoxUpperRight, #adBrandDev, #adBrandingStation, #adBreak, #adCENTRAL, #adCTXSp, #adCarousel, #adChannel, #adChoiceFooter, #adChoices, #adChoicesIcon, #adChoicesLogo, #adCirc300X200, #adCirc300X250, #adCirc300x300, #adCirc620X100, #adCirc_620_100, #adClickLeft, #adClickMe, #adClickRight, #adCol, #adColumn, #adColumn3, #adCompanionBanner, #adCompanionSubstitute, #adComponentWrapper, #adContainerCC, #adContainerForum, #adContainer_1, #adContainer_2, #adContainer_3, #adContent, #adContentHolder, #adContext, #adControl1, #adDailyDeal, #adDiv, #adDiv0, #adDiv1, #adDiv300, #adDiv4, #adDiv728, #adDivContainer, #adDivleaderboard, #adDivminimodulebutton1, #adDivminimodulebutton2, #adDivminimodulebutton3, #adDivmrec, #adDivmrecadhomepage, #adFiller, #adFixFooter, #adFlashDiv, #adFooter, #adFooterTitel, #adFot, #adFoxBanner, #adFps, #adFrame, #adFtofrs, #adGallery, #adGmWidget, #adGoogleText, #adGroup1, #adGroup4, #adHeader, #adHeaderTop, #adHeaderWrapper, #adHolder, #adHolder1, #adHolder2, #adHolder3, #adHolder300x250, #adHolder4, #adHolder5, #adHolder6, #adIframe, #adInBetweenPosts, #adInCopy, #adInstoryOneWrap, #adInstoryTwoWrap, #adInteractive1, #adInteractive4, #adInteractiveInline, #adIsland, #adLB, #adLContain, #adLabel, #adLayer, #adLeader, #adLeaderTop, #adLeaderboard, #adLeaderboard-middle, #adLeaderboardUp, #adLeft, #adLink, #adLink1, #adLink300, #adLocation-1, #adLocation-2, #adLocation-3, #adLocation-4, #adLounge, #adLrec, #adMOBILETOP, #adMPU, #adMPUHolder, #adMagAd, #adMain, #adMarketplace, #adMed, #adMedRect, #adMediaWidget, #adMediumRectangle, #adMeld, #adMessage, #adMid1, #adMid2, #adMiddle0Frontpage, #adMiddle_imgAd, #adMiniPremiere, #adMonster1, #adMpu, #adMpuBottom, #adNshareWrap, #adOne, #adOuter, #adPLaceHolderTop728, #adPUSHDOWNBANNER, #adPageContainer, #adPanelAjaxUpdate, #adPlaceHolder1, #adPlaceHolder2, #adPlaceHolderRight, #adPlaceScriptrightSidebarFirstBanner, #adPlaceScriptrightSidebarSecondBanner, #adPlaceScripttopBanner, #adPlacer, #adPopover, #adPosOne, #adPosition0, #adPosition14, #adPosition5, #adPosition6, #adPosition7, #adPosition9, #adPush, #adRContain, #adRectangleFooter, #adRectangleHeader, #adRight, #adRight1, #adRight2, #adRight3, #adRight4, #adRight5, #adRightColumnHolder, #adSPLITCOLUMNTOPRIGHT, #adScraper, #adSection, #adSense, #adSenseBottomDiv, #adSenseBox, #adSenseContentTop, #adSenseLoadingPlaceHolder, #adSenseModule, #adSenseResultAdblock, #adSenseResults, #adSenseSidebarBottom, #adSenseTall, #adSenseWrapper, #adServer_marginal, #adSet, #adShortTower, #adSide, #adSideButton, #adSidebar, #adSidebarSq, #adSite, #adSkin, #adSkinBackdrop, #adSky, #adSkyPosition, #adSkyscraper, #adSlider, #adSlot-inPage-300x250-right, #adSlot01, #adSlot02, #adSlot1, #adSlot2, #adSlot2_grid, #adSlot3, #adSlot3_grid, #adSlot4, #adSlot4_grid, #adSlug, #adSpace, #adSpace0, #adSpace1, #adSpace10, #adSpace11, #adSpace12, #adSpace13, #adSpace14, #adSpace15, #adSpace16, #adSpace17, #adSpace18, #adSpace19, #adSpace2, #adSpace20, #adSpace21, #adSpace22, #adSpace23, #adSpace24, #adSpace25, #adSpace3, #adSpace300_ifrMain, #adSpace4, #adSpace5, #adSpace6, #adSpace7, #adSpace8, #adSpace9, #adSpaceBottom, #adSpace_footer, #adSpace_right, #adSpace_top, #adSpacer, #adSpecial, #adSplotlightEm, #adSponsor, #adSpot-Leader, #adSpot-banner, #adSpot-island, #adSpot-mrec1, #adSpot-promobox1, #adSpot-promobox2, #adSpot-sponsoredlinks, #adSpot-textbox1, #adSpot-twin, #adSpot-widestrip, #adSpotAdvertorial, #adSpotIsland, #adSpotIslandLarge, #adSpotSponsoredLinks, #adSpotholder-EGN, #adSpotlightSquare1, #adSqb, #adSquare, #adStaticA, #adStrip, #adSuperAd, #adSuperPremiere, #adSuperSkyscraper, #adSuperbanner, #adTableCell, #adTag, #adTag-genre, #adTag1, #adTag2, #adTeaser, #adText, #adText2, #adTextCustom, #adTextLink, #adTextRt, #adText_container, #adThree, #adTicker, #adTiff, #adTile, #adTop, #adTop1, #adTop2, #adTopBanner-inner, #adTopBanner1, #adTopBig, #adTopBox300x300, #adTopContent, #adTopModule, #adTopbanner, #adTopboxright, #adTower, #adTower1, #adTower2, #adTwo, #adUn_1, #adUn_2, #adUn_3, #adUnit, #adValue, #adVcss, #adWideSkyscraper, #adWrap, #adWrapper, #adWrapper1, #adWrapperLeft, #adWrapperRight, #adWrapperSky, #adZoneTop, #ad_0, #ad_02, #ad_03, #ad_04, #ad_1, #ad_120_sidebar, #ad_120x600, #ad_120x90, #ad_130x250_inhouse, #ad_160, #ad_160_600, #ad_160_600_2, #ad_160_container_left, #ad_160_container_right, #ad_160_sidebar, #ad_160x160, #ad_160x600, #ad_175x300, #ad_190x90, #ad_2, #ad_250, #ad_250x250, #ad_3, #ad_300, #ad_300_250, #ad_300_250_1, #ad_300_250_inline, #ad_300_container, #ad_300_interruptor, #ad_300_wrapper, #ad_300a, #ad_300b, #ad_300c, #ad_300misc, #ad_300x100, #ad_300x100_m_c, #ad_300x250, #ad_300x250Ando, #ad_300x250_1, #ad_300x250_2, #ad_300x250_container, #ad_300x250_content_column, #ad_300x250_frame, #ad_300x250_m_c, #ad_300x250_secondary, #ad_300x250_startgame, #ad_300x250m, #ad_300x60, #ad_300x600, #ad_300x90, #ad_336, #ad_350_200, #ad_380x35, #ad_4, #ad_450x280, #ad_468_60, #ad_468x120, #ad_468x60, #ad_470x60a, #ad_5, #ad_500, #ad_500_label, #ad_500x150, #ad_6, #ad_700_90, #ad_700x430, #ad_728, #ad_728_90, #ad_728_foot, #ad_728_holder, #ad_728a, #ad_728b, #ad_728x90, #ad_728x90_container, #ad_728x90_content, #ad_728x90home, #ad_728x91, #ad_8, #ad_88x31, #ad_940, #ad_984, #ad_990x90, #ad_A, #ad_B, #ad_B1, #ad_Banner, #ad_Bottom, #ad_C, #ad_C2, #ad_D, #ad_DisplayAd1, #ad_DisplayAd2, #ad_E, #ad_Entry_160x600, #ad_Entry_728x90, #ad_F, #ad_G, #ad_H, #ad_Header_768x90, #ad_Home_300x250, #ad_I, #ad_J, #ad_K, #ad_L, #ad_LargeRec01, #ad_M, #ad_Middle, #ad_Middle1, #ad_N, #ad_NorthBanner, #ad_O, #ad_P, #ad_Position1, #ad_Pushdown, #ad_R1, #ad_Right, #ad_Top, #ad_Top2, #ad_TopLongBanner, #ad_Wrap, #ad_YieldManager-160x600, #ad_YieldManager-300x250, #ad_YieldManager-728x90, #ad_above_game, #ad_ad, #ad_adsense, #ad_after_navbar, #ad_anchor, #ad_and_content_ad_box, #ad_area, #ad_article_btm, #ad_banner, #ad_bannerManage_1, #ad_banner_1, #ad_banner_120x600, #ad_banner_125x300, #ad_banner_300x250, #ad_banner_468x60, #ad_banner_728x90, #ad_banner_728x90_bot, #ad_banner_bot, #ad_banner_example, #ad_banner_top, #ad_banners, #ad_banners_content, #ad_bar, #ad_bar_rect, #ad_bellow_post, #ad_bg, #ad_bg_image, #ad_big, #ad_bigbox, #ad_bigbox_companion, #ad_bigrectangle, #ad_bigsize, #ad_bigsize_wrapper, #ad_billboard, #ad_billboard2, #ad_billboard_ifm, #ad_block, #ad_block_0, #ad_block_1, #ad_block_2, #ad_block_300x250, #ad_block_mpu, #ad_board_after_forums, #ad_board_before_forums, #ad_body, #ad_bottom, #ad_bottom_1x1, #ad_bottom_728x90, #ad_bottom_another, #ad_bottom_article_text, #ad_bottombrandtext, #ad_box, #ad_box02, #ad_box160a, #ad_box300x250, #ad_box_2, #ad_box_ad_0, #ad_box_ad_1, #ad_box_colspan, #ad_box_top, #ad_branding, #ad_bs_area, #ad_btmslot, #ad_bucket_med_rectangle_1, #ad_bucket_med_rectangle_2, #ad_buttons, #ad_category_middle, #ad_cell, #ad_center, #ad_center_monster, #ad_channel, #ad_chitikabanner_120x600LH, #ad_choices, #ad_circ300x250, #ad_circ_300_200, #ad_circ_300x250, #ad_circ_300x300, #ad_close, #ad_closebtn, #ad_cna2, #ad_comments, #ad_companion_banner, #ad_complex, #ad_comps_top, #ad_cont, #ad_cont1, #ad_cont2, #ad_container, #ad_container_0, #ad_container_300x250, #ad_container_marginal, #ad_container_side, #ad_container_sidebar, #ad_container_top, #ad_content, #ad_content_before_first_para, #ad_content_fullsize, #ad_content_primary, #ad_content_right, #ad_content_top, #ad_content_wrap, #ad_creative_2, #ad_creative_3, #ad_creative_5, #ad_cyborg, #ad_display_300_250, #ad_display_728_90, #ad_div, #ad_div_bottom, #ad_div_top, #ad_embed_300x250, #ad_fb_circ, #ad_feature, #ad_feedback, #ad_fg, #ad_firstpost, #ad_flyrelax, #ad_foot, #ad_footer, #ad_footer1, #ad_footerAd, #ad_footer_s, #ad_footer_small, #ad_frame, #ad_frame1, #ad_front_three, #ad_fullbanner, #ad_gallery, #ad_gallery_bot, #ad_global_300x250, #ad_global_above_footer, #ad_global_header, #ad_global_header1, #ad_global_header2, #ad_google_content336, #ad_googlebanner_160x600LH, #ad_grp1, #ad_grp2, #ad_gutter_top, #ad_h3, #ad_haha_1, #ad_haha_4, #ad_halfpage, #ad_hdr_2, #ad_head, #ad_header, #ad_header_1, #ad_header_container, #ad_header_logo_placeholder, #ad_headerlarge, #ad_help_link_new, #ad_hf, #ad_hide_for_menu, #ad_holder, #ad_home, #ad_home_middle, #ad_horizontal, #ad_horseshoe_left, #ad_horseshoe_right, #ad_horseshoe_spacer, #ad_horseshoe_top, #ad_hotpots, #ad_houseslot1_desktop, #ad_houseslot_a, #ad_houseslot_b, #ad_iframe_160_by_600_middle, #ad_iframe_300, #ad_img, #ad_img_banner, #ad_in_arti, #ad_infoboard_box, #ad_inplace_1, #ad_interestmatch, #ad_interestmatch400, #ad_island, #ad_island2, #ad_island_incontent, #ad_island_incontent2, #ad_keywrods, #ad_kvadrat_under_player, #ad_label, #ad_large, #ad_large_rectangular, #ad_lastpost, #ad_layer, #ad_layer1, #ad_layer2, #ad_ldb, #ad_lead1, #ad_leader, #ad_leaderBoard, #ad_leaderboard, #ad_leaderboard2, #ad_leaderboard3, #ad_leaderboard728x90, #ad_leaderboard_1, #ad_leaderboard_flex, #ad_leaderboard_master, #ad_leaderboard_middle, #ad_leaderboard_top, #ad_leaderboardtwo, #ad_leaderborder_container1, #ad_left, #ad_left_1, #ad_left_2, #ad_left_3, #ad_left_skyscraper, #ad_left_skyscraper_2, #ad_left_top, #ad_leftslot, #ad_lft, #ad_link, #ad_links, #ad_links_footer, #ad_lnk, #ad_lrec, #ad_lwr_square, #ad_main, #ad_main_top, #ad_marker, #ad_mast, #ad_med_rect, #ad_medium, #ad_medium_rectangle, #ad_medium_rectangular, #ad_mediumrectangle, #ad_megabanner, #ad_menu_header, #ad_message, #ad_messageboard_x10, #ad_middle, #ad_middle_122, #ad_middle_2, #ad_middle_bottom, #ad_midstrip, #ad_ml, #ad_mobile, #ad_module, #ad_most_pop_234x60_req_wrapper, #ad_mpu, #ad_mpu2, #ad_mpu300x250, #ad_mpu_1, #ad_mpuav, #ad_mpuslot, #ad_mrcontent, #ad_mrec, #ad_mrec1, #ad_mrec2, #ad_msgplus-gallery-5, #ad_myFrame, #ad_netpromo, #ad_new, #ad_newsletter, #ad_num_1, #ad_num_2, #ad_num_3, #ad_one, #ad_overlay, #ad_overlay_content, #ad_overlay_countdown, #ad_overture, #ad_panel, #ad_panel_1, #ad_panel_2, #ad_panorama_top, #ad_pencil, #ad_ph_1, #ad_place, #ad_placeholder, #ad_play_300, #ad_plugs, #ad_post, #ad_post_300, #ad_poster, #ad_pr_info, #ad_primary, #ad_primaryAd, #ad_promoAd, #ad_publicidad, #ad_pushupbar-closed, #ad_rail, #ad_rect, #ad_rect1, #ad_rect2, #ad_rect3, #ad_rect_body, #ad_rect_bottom, #ad_rect_c, #ad_rectangle, #ad_rectangle_medium, #ad_rectangular, #ad_region1, #ad_region2, #ad_region3, #ad_region5, #ad_related_links_div, #ad_related_links_div_program, #ad_replace_div_0, #ad_replace_div_1, #ad_report_leaderboard, #ad_report_rectangle, #ad_results, #ad_right, #ad_right3, #ad_rightSidebarFirstBanner, #ad_rightSidebarSecondBanner, #ad_right_1, #ad_right_box, #ad_right_column1_1, #ad_right_column2_1, #ad_right_content_article_page, #ad_right_content_home, #ad_right_main, #ad_right_out, #ad_right_rail_bottom, #ad_right_rail_flex, #ad_right_rail_top, #ad_right_second, #ad_right_skyscraper, #ad_right_skyscraper_2, #ad_right_top, #ad_rightslot, #ad_righttop-300x250, #ad_ros_tower, #ad_rotator-2, #ad_rotator-3, #ad_row, #ad_row_home, #ad_rr_1, #ad_rside, #ad_rside_link, #ad_script_head, #ad_sec, #ad_sec_div, #ad_secondary, #ad_sense, #ad_sense_help, #ad_sgd, #ad_short, #ad_sidebar, #ad_sidebar1, #ad_sidebar2, #ad_sidebar3, #ad_sidebar_1, #ad_sidebar_top, #ad_silo, #ad_sitebar, #ad_skin, #ad_sky, #ad_sky1, #ad_sky2, #ad_sky3, #ad_skyscraper, #ad_skyscraper160x600, #ad_skyscraper_1, #ad_skyscraper_right, #ad_skyscraper_text, #ad_slot, #ad_slot_bottom, #ad_slot_leaderboard, #ad_slot_livesky, #ad_slot_right_bottom, #ad_slot_right_top, #ad_slot_sky_top, #ad_small, #ad_space, #ad_space_300_250, #ad_space_728, #ad_space_top, #ad_sponsored, #ad_sponsorship_2, #ad_spot300x250, #ad_spot_a, #ad_spot_b, #ad_spotlight, #ad_square, #ad_squares, #ad_ss, #ad_stck, #ad_strapad, #ad_stream10, #ad_stream11, #ad_stream12, #ad_stream16, #ad_stream17, #ad_stream19, #ad_stream8, #ad_strip, #ad_table, #ad_takeover, #ad_tall, #ad_tbl, #ad_term_bottom_place, #ad_thread_first_post_content, #ad_thread_last_post_content, #ad_tile_home, #ad_top, #ad_topBanner, #ad_top_728x90, #ad_top_banner, #ad_top_bar, #ad_top_header_center, #ad_top_holder, #ad_topbanner, #ad_topmob, #ad_topnav, #ad_topslot, #ad_topslot_b, #ad_tp_banner_1, #ad_tp_banner_2, #ad_two, #ad_txt, #ad_under_game, #ad_unit, #ad_unit2, #ad_unit_slot1, #ad_unit_slot2, #ad_unit_slot3, #ad_unit_slot4, #ad_vertical, #ad_video_abovePlayer, #ad_video_belowPlayer, #ad_video_large, #ad_website_top, #ad_wide, #ad_wide_box, #ad_widget, #ad_widget_1, #ad_window, #ad_wp_base, #ad_wrap, #ad_wrapper, #ad_wrapper1, #ad_wrapper2, #ad_x10, #ad_x20, #ad_xrail_top, #ad_zone, #ad_zone1, #ad_zone2, #ad_zone3, #adamazonbox, #adaptv_ad_player_div, #adaptvcompanion, #adbForum, #adbackground, #adbanner, #adbanner-home-left, #adbanner-home-right, #adbanner-middle, #adbanner-top-left, #adbanner-top-right, #adbanner00001, #adbanner00002, #adbanner00003, #adbanner00004, #adbanner00005, #adbanner1, #adbanner_abovethefold_300, #adbanner_mobile_top, #adbannerbox, #adbannerdiv, #adbannerleft, #adbannerright, #adbannerwidget, #adbar, #adbar_ad_1_div, #adbar_ad_2_div, #adbar_ad_3_div, #adbar_ad_4_div, #adbar_ads_container_div, #adbar_main_div, #adbarbox, #adbard, #adbdiv, #adbg_ad_0, #adbg_ad_1, #adbig, #adblade, #adblade-disc, #adbladeSp, #adblade_ad, #adblkad, #adblock, #adblock-300x250, #adblock-big, #adblock-jango, #adblock-leaderboard, #adblock-small, #adblock1, #adblock2, #adblock4, #adblock_header_ad_1, #adblock_header_ad_1_inner, #adblock_sidebar_ad_2, #adblock_sidebar_ad_2_inner, #adblock_v, #adblockbottom, #adblockerMess, #adblockerwarnung, #adblockrighta, #adblocktop, #adblocktwo, #adbn, #adbn_UMU, #adbnr, #adboard, #adbody, #adbottom, #adbottomgao, #adbox, #adbox-indivisual-body-topright, #adbox-placeholder-topbanner, #adbox-topbanner, #adbox1, #adbox2, #adbox300600, #adbox300x250_1, #adbox300x250_2, #adbox_right, #adbrite, #adbrite_inline_div, #adbritebottom, #adbutton, #adbuttons, #adcarousel, #adcatfish, #adcell, #adcenter, #adcenter2, #adcenter4, #adchoices-icon, #adchoices_container, #adclear, #adclose, #adcode, #adcode1, #adcode10, #adcode2, #adcode3, #adcode4, #adcolContent, #adcolumn, #adcolumnwrapper, #adcontainer, #adcontainer1, #adcontainer125px, #adcontainer2, #adcontainer250x250, #adcontainer3, #adcontainer5, #adcontainerRight, #adcontainer___gelement_adbanner_2_0, #adcontainer_top_ads, #adcontainsm, #adcontent, #adcontent1, #adcontextlinks, #adcontrolPushSite, #adcontrolhalfbanner, #adcontrolisland, #add-top, #add720, #add_160x600, #add_720bottom, #add_block_ad1, #add_block_ad2, #add_ciao2, #add_space_google, #add_space_sidebar, #addbottomleft, #addiv-bottom, #addiv-top, #addspaceleft, #addspaceright, #adfactor-label, #adfloat, #adfooter, #adfooter_728x90, #adfooter_hidden, #adframetop, #adfreead, #adhalfbanner_wrapper, #adhalfpage, #adhead, #adhead_g, #adheader, #adheadhubs, #adhesionAdSlot, #adhide, #adholder, #adhome, #adhomepage, #adhzh, #adid10601, #adid2161, #adiframe1_iframe, #adiframe2_iframe, #adiframe3_iframe, #adigniter, #adimg, #adimg0, #adimg1, #adimg3, #adimg6, #adition_content_ad, #adjacency, #adjacent-list-ad, #adjs_id, #adk2_slider_top_right, #adkit_content-block, #adkit_content-foot, #adkit_footer, #adkit_mrec1, #adkit_mrec2, #adkit_rectangle, #adkit_rnav-bt, #adkit_rnav-fb, #adl_120x600, #adl_250x250, #adl_300x100, #adl_300x120, #adl_300x250, #adl_300x250_td, #adl_728x90, #adl_individual_1, #adl_leaderboard, #adl_medium_rectangle, #adlabel, #adlabelFooter, #adlabelfooter, #adlabelheader, #adlanding, #adlandscape, #adlargeverti, #adlargevertimarginauto, #adlayer, #adlayerContainer, #adlayer_back, #adlayerad, #adleaderboard, #adleaderboard_flex, #adleaderboardb, #adleaderboardb_flex, #adleft, #adlink-13, #adlink-133, #adlink-19, #adlink-197, #adlink-213, #adlink-28, #adlink-55, #adlink-74, #adlink-98, #adlinks, #adlinkws, #adlove, #adlrec, #admain, #admanagerResultListBox, #admanager_leaderboard, #admanager_top_banner, #admid, #admiddle3, #admiddle3center, #admiddle3left, #admiddleCenter, #admod2, #admon-300x250, #admon-728x90, #admputop, #admsg, #admulti520, #adnet, #adnews, #adnorth, #adops_cube, #adops_leaderboard, #adops_skyscraper, #adoptionsimg, #adoverlaysrc, #adpanel-block, #adplace, #adplaceholder_mpu01, #adplacement, #adplacer_preroll1, #adplate-content, #adpos-top, #adpos1-leaderboard, #adposition, #adposition-C, #adposition-FPMM, #adposition-REM2, #adposition-SHADE, #adposition-TOCSS, #adposition-TVSP, #adposition-inner-REM1, #adposition-inner-REM3, #adposition1, #adposition10, #adposition1_container, #adposition2, #adposition3, #adposition4, #adpositionbottom, #adpostloader, #adpromo, #adprovider-default, #adrect, #adrectangle, #adrectanglea, #adrectanglea_flex, #adrectanglea_hidden, #adrectangleb, #adrectangleb_flex, #adrectmarginauto, #adrig, #adright, #adright2, #adrightbottom, #adrightgame, #adrighthome, #adrightrail, #adriver_middle, #adriver_top, #adrotate_widgets-11, #adrotate_widgets-12, #adrotate_widgets-2, #adrotate_widgets-20, #adrotate_widgets-24, #adrotate_widgets-3, #adrotate_widgets-4, #adrotate_widgets-5, #adrotate_widgets-6, #adrotate_widgets-7, #adrow, #adrow-house, #adrow1, #adrow3, #ads-1, #ads-125, #ads-125-2, #ads-160x600, #ads-200, #ads-200x200-a, #ads-250, #ads-300, #ads-300-250, #ads-300x250-L3-2, #ads-336x280, #ads-468, #ads-5, #ads-728x90, #ads-728x90-I3, #ads-728x90-I4, #ads-A, #ads-B, #ads-B1, #ads-C, #ads-C1, #ads-E, #ads-E1, #ads-F, #ads-G, #ads-H, #ads-K, #ads-area, #ads-banner, #ads-banner-top, #ads-block, #ads-block-frame, #ads-bot, #ads-bottom, #ads-box-header-pb, #ads-by-google, #ads-category, #ads-center-text, #ads-col, #ads-contain-125, #ads-container-2, #ads-container-anchor, #ads-container-top, #ads-dell, #ads-div2, #ads-dw, #ads-footer, #ads-footer-inner, #ads-footer-wrap, #ads-google, #ads-h-left, #ads-h-right, #ads-header, #ads-header-728, #ads-horizontal, #ads-hoster-2, #ads-indextext, #ads-king, #ads-leader, #ads-leaderboard, #ads-leaderboard1, #ads-left-top, #ads-lrec, #ads-main, #ads-main-bottom, #ads-menu, #ads-middle, #ads-mn, #ads-mpu, #ads-outer, #ads-panel, #ads-prices, #ads-rhs, #ads-right, #ads-right-bottom, #ads-right-cube, #ads-right-skyscraper, #ads-right-text, #ads-right-top, #ads-right-twobottom, #ads-rt, #ads-sidebar-bottom, #ads-sidebar-skyscraper-unit, #ads-sidebar-top, #ads-slot, #ads-sponsored-boxes, #ads-sticky, #ads-text, #ads-top, #ads-tp, #ads-under-rotator, #ads-vers7, #ads-vertical, #ads-vertical-wrapper, #ads-wrap, #ads-wrapper, #ads1, #ads100Box, #ads100Middlei4, #ads120, #ads120_600-widget-2, #ads125, #ads160_600-widget-3, #ads160_600-widget-5, #ads160_600-widget-7, #ads160left, #ads2, #ads3, #ads300, #ads300-250, #ads300Bottom, #ads300Top, #ads300_250-widget-1, #ads300_250-widget-10, #ads300_250-widget-11, #ads300_250-widget-2, #ads300_250-widget-3, #ads300_250-widget-4, #ads300_250-widget-6, #ads300_600-widget-2, #ads300hp, #ads300k, #ads300x200, #ads300x250, #ads300x250_2, #ads300x250_single, #ads315, #ads336Box, #ads336x280, #ads340web, #ads4, #ads7, #ads728, #ads72890top, #ads728bottom, #ads728top, #ads728x90, #ads728x90_2, #ads790, #adsBannerFrame, #adsBar, #adsBottom, #adsBox-460_left, #adsBox-dynamic-right, #adsBoxResultsPage, #adsCTN, #adsCombo02_1, #adsCombo02_2, #adsCombo02_3, #adsCombo02_4, #adsCombo02_5, #adsCombo02_6, #adsCombo02_7, #adsContainer, #adsContent, #adsDisplay, #adsDiv0, #adsDiv1, #adsDiv2, #adsDiv3, #adsDiv4, #adsDiv5, #adsDiv6, #adsDiv7, #adsGooglePos, #adsHeadLine, #adsHeader, #adsHeading, #adsID, #adsIframe, #adsIfrme1, #adsIfrme2, #adsIfrme3, #adsIfrme4, #adsLREC, #adsLeftZone1, #adsLeftZone2, #adsLinkFooter, #adsNarrow, #adsPanel, #adsProdHighlight_wrap, #adsRight, #adsRightDiv, #adsSPRBlock, #adsSuperCTN, #adsTop, #adsTopLeft, #adsZone1, #adsZone2, #adsZone_1, #ads_01, #ads_120x60_block, #ads_160, #ads_2015, #ads_2015_1, #ads_3, #ads_300, #ads_300x250, #ads_320_260, #ads_320_260_2, #ads_728, #ads_728x90, #ads_absolute_left, #ads_absolute_right, #ads_back, #ads_banner, #ads_banner1, #ads_banner_header, #ads_banner_right1, #ads_bar, #ads_belowforumlist, #ads_belownav, #ads_big, #ads_bigrec1, #ads_bigrec2, #ads_bigrec3, #ads_block, #ads_bottom, #ads_bottom_inner, #ads_bottom_outer, #ads_box, #ads_box1, #ads_box2, #ads_box_bottom, #ads_box_right, #ads_box_top, #ads_button, #ads_by_google, #ads_campaign, #ads_catDiv, #ads_center, #ads_center_banner, #ads_central, #ads_container, #ads_dynamicShowcase, #ads_eo, #ads_expand, #ads_footer, #ads_fullsize, #ads_h, #ads_halfsize, #ads_header, #ads_header_games, #ads_horiz, #ads_horizontal, #ads_html1, #ads_html2, #ads_im, #ads_inner, #ads_insert_container, #ads_layout_bottom, #ads_lb, #ads_lb_frame, #ads_leaderbottom, #ads_left, #ads_left_top, #ads_line, #ads_mads_r1, #ads_mads_r2, #ads_medrect, #ads_notice, #ads_pave, #ads_place, #ads_placeholder, #ads_player, #ads_player_audio, #ads_player_line, #ads_postdownload, #ads_pro_468_60_on_vid, #ads_r_c, #ads_right, #ads_right_sidebar, #ads_right_top, #ads_section_textlinks, #ads_side, #ads_sidebar_bgnd, #ads_sidebar_roadblock, #ads_sky, #ads_slide_div, #ads_space, #ads_space_header, #ads_special_center, #ads_sponsFeed-headline, #ads_sponsFeed-left, #ads_sponsored_link_pixel, #ads_superbanner1, #ads_superbanner2, #ads_superior, #ads_td, #ads_text, #ads_textlinks, #ads_title, #ads_top, #ads_top2, #ads_top_banner, #ads_top_container, #ads_top_right, #ads_top_sec, #ads_topbanner, #ads_tower1, #ads_video, #ads_watch_top_square, #ads_wide, #ads_wrapper, #ads_zone27, #adsbottom, #adsbottombluesleft, #adsbox, #adsbox-left, #adsbox-right, #adsbox1, #adsbox2, #adsbox3, #adsbox336x280, #adsbox4, #adsbox728x90, #adsbysourcewidget-2, #adscenter, #adscolumn, #adscontainer, #adscontent, #adsctl00_AdsHome2, #adsd_contentad_r1, #adsd_contentad_r2, #adsd_contentad_r3, #adsd_topbanner, #adsd_txt_sky, #adsdaq160600, #adsdaq300250, #adsdaq72890, #adsdiv, #adsdiv300, #adsdiv468, #adsdiv_close, #adsection, #adsense, #adsense-2, #adsense-468x60, #adsense-area, #adsense-bottom, #adsense-end-300, #adsense-head-spacer, #adsense-header, #adsense-letterbox, #adsense-link, #adsense-middle, #adsense-module-bottom, #adsense-new, #adsense-post, #adsense-right, #adsense-sidebar, #adsense-tag, #adsense-text, #adsense-top, #adsense-wrap, #adsense03, #adsense04, #adsense05, #adsense1, #adsense160600, #adsense2, #adsense2pos, #adsense300x250, #adsense468, #adsense6, #adsense728, #adsenseArea, #adsenseHeader, #adsenseLeft, #adsenseOne, #adsenseWrap, #adsense_300x250, #adsense_article_bottom, #adsense_article_left, #adsense_banner_top, #adsense_block, #adsense_block_238x200, #adsense_block_350x320, #adsense_bottom_ad, #adsense_box, #adsense_box2, #adsense_box_video, #adsense_honeytrap, #adsense_image, #adsense_inline, #adsense_item_detail, #adsense_leaderboard, #adsense_overlay, #adsense_placeholder_2, #adsense_sidebar, #adsense_testa, #adsense_top, #adsense_unit5, #adsense_ziel, #adsensebreadcrumbs, #adsenseheader, #adsensehorizontal, #adsensempu, #adsensepo, #adsensepos, #adsensequadr, #adsenseskyscraper, #adsensetext, #adsensetopmobile, #adsensetopplay, #adsensewide, #adsensewidget-3, #adserv, #adserve-Banner, #adserve-Leaderboard, #adserve-MPU, #adserve-Sky, #adsfundo, #adshometop, #adshowbtm, #adshowtop, #adside, #adsideblock1, #adsider, #adsiframe, #adsimage, #adskinleft, #adskinlink, #adskinright, #adskintop, #adsky, #adskyleftdiv, #adskyrightdiv, #adskyscraper, #adskyscraper_flex, #adsleft1, #adslider, #adslist, #adslistbox, #adslot, #adslot-2-container, #adslot-3-container, #adslot-4-container, #adslot1, #adslot1173, #adslot1189, #adslot1202, #adslot2, #adslot3, #adslot4, #adslot5, #adslot6, #adslot7, #adslot_c2, #adslot_m1, #adslot_m2, #adslot_m3, #adsmegabanner, #adsmiddle, #adsnews, #adsonar, #adsonarBlock, #adspace, #adspace-1, #adspace-2, #adspace-300x250, #adspace-728, #adspace-728x90, #adspace-bottom, #adspace-leaderboard-top, #adspace-one, #adspace-panorama, #adspace-top, #adspace300x250, #adspaceBox, #adspaceBox300, #adspaceBox300_150, #adspaceBox300white, #adspaceRow, #adspace_header, #adspace_leaderboard, #adspace_top, #adspacer, #adspan, #adspdl-container, #adspecial_offer_box, #adsplace1, #adsplace2, #adsplace4, #adsplash, #adsponsorImg, #adsponsored_links_box, #adspot, #adspot-1, #adspot-149x170, #adspot-1x4, #adspot-2, #adspot-295x60, #adspot-2a, #adspot-2b, #adspot-300x110-pos-1, #adspot-300x125, #adspot-300x250-pos-1, #adspot-300x250-pos-2, #adspot-300x250-pos1, #adspot-300x250-pos3, #adspot-300x600-pos1, #adspot-468x60-pos-2, #adspot-620x270-pos-1, #adspot-620x45-pos-1, #adspot-620x45-pos-2, #adspot-728x90, #adspot-728x90-pos-2, #adspot-a, #adspot-bottom, #adspot-c, #adspot-d, #adspot-top, #adspot300x250, #adspot_220x90, #adspot_300x250, #adspot_468x60, #adspot_728x90, #adspotlight1, #adsquare, #adsquare2, #adsright, #adss, #adssidebar2, #adssidebar3, #adsspace, #adstd, #adstext2, #adstop, #adstory, #adstrip, #adstripbottom, #adstripnew, #adstuff, #adswidget1-quick-adsense, #adswidget2-quick-adsense, #adswidget2-quick-adsense-reloaded-2, #adswizzBanner, #adsxpls2, #adszed-728x90, #adtab, #adtab-feedback2, #adtable_top, #adtag5, #adtag8, #adtag_right_side, #adtagfooter, #adtagheader, #adtagrightcol, #adtags_left, #adtaily, #adtaily-widget-light, #adtech_0, #adtech_1, #adtech_2, #adtech_3, #adtech_728or920_2, #adtech_googleslot_03c, #adtech_leaderboard01, #adtech_takeover, #adtechbanner728, #adtext, #adtext-top-content, #adtop, #adtopDet, #adtopHeader, #adtopPrograma, #adtop_dfp, #adtopbanner, #adtopbox, #adtophp, #adtrafficright, #adtxt, #adundergame, #adunderpicture, #adunit, #adunit-mpu-atf, #adunit-mpu-atf-feed, #adunit-mpu-atf-sidebar, #adunit-mpu-btf-1, #adunit-mpu-btf-6, #adunit-mpu-btf-article, #adunit-mpu-btf-article-2, #adunit-mpu-btf-sidebar, #adunit-mpu-second, #adunit-pages1x1, #adunit-roadblock, #adunit300x500, #adunit_article_center_bottom_computer, #adunit_article_center_middle1_computer, #adunit_article_center_middle4_computer, #adunit_article_center_middle6_computer, #adunit_article_center_top_computer, #adunit_article_right_middle2_computer, #adunit_article_right_top_computer, #adunit_main_center_bottom_computer, #adunit_main_right_middle2_computer, #adunit_main_right_top_computer, #adunit_video, #adunitl, #adv-01, #adv-300, #adv-box, #adv-comments-placeholder, #adv-companion-iframe, #adv-container, #adv-ext-ext-1, #adv-ext-ext-2, #adv-fb-container, #adv-google, #adv-leaderboard, #adv-left, #adv-masthead, #adv-middle, #adv-middle1, #adv-midroll, #adv-mpux, #adv-preroll, #adv-right, #adv-right1, #adv-scrollable, #adv-sticky-1, #adv-sticky-2, #adv-strip, #adv-text, #adv-title, #adv-top, #adv-x34, #adv-x35, #adv-x36, #adv-x37, #adv-x38, #adv-x39, #adv-x40, #adv130x195, #adv160x600, #adv170, #adv2_ban, #adv300bottom, #adv300top, #adv300x250, #adv300x250container, #adv3_ban, #adv468x90, #adv728, #adv728x90, #adv768x90, #advCard1, #advCard2, #advCard3, #advCarrousel, #advHome, #advHomevideo, #advMegaBanner, #advRectangle, #advRectangle1, #advSidebarDocBox, #advSkin, #advTop, #advTopRight_anchor, #advWrapper, #adv_300, #adv_300x250_1, #adv_300x250_2, #adv_300x250_3, #adv_468x60_content, #adv_5, #adv_52, #adv_6, #adv_62, #adv_65, #adv_7, #adv_70, #adv_71, #adv_728, #adv_728x90, #adv_73, #adv_94, #adv_96, #adv_97, #adv_98, #adv_BoxBottom, #adv_Inread, #adv_IntropageOvl, #adv_LdbMastheadPush, #adv_Reload, #adv_Skin, #adv_banner_featured, #adv_banner_sidebar, #adv_bootom, #adv_border, #adv_box_a, #adv_center, #adv_config, #adv_contents, #adv_contents_tem, #adv_google_300, #adv_google_728, #adv_halfpage, #adv_halfpage_title, #adv_holder, #adv_leaderboard, #adv_mpu1, #adv_mpu2, #adv_network, #adv_overlay, #adv_overlay_content, #adv_r, #adv_right, #adv_skin, #adv_skin_1, #adv_skin_1_a, #adv_sky, #adv_sponsorRowFooter, #adv_sponsorRowHeader, #adv_sponsor_cat, #adv_textlink, #adv_textual_google_div, #adv_top, #adv_top_banner_wrapper, #adv_videobox, #adv_wallpaper, #adv_wallpaper2, #adv_wideleaderboard, #adver, #adver-top, #adver1, #adver2, #adver3, #adver4, #adver5, #adver6, #adver7, #adverFrame, #advert-1, #advert-120, #advert-2, #advert-ahead, #advert-banner, #advert-banner-wrap, #advert-block, #advert-boomer, #advert-box, #advert-column, #advert-container-top, #advert-display, #advert-footer, #advert-footer-hidden, #advert-header, #advert-hpu, #advert-island, #advert-leaderboard, #advert-left, #advert-links-bottom, #advert-mpu, #advert-placeholder-post-content-image-1, #advert-right, #advert-right-not-home, #advert-sky, #advert-skyscaper, #advert-skyscraper, #advert-stickysky, #advert-text, #advert-top, #advert-top-banner, #advert-wrapper, #advert1, #advert1hp, #advert2, #advert234_container, #advert2area, #advert2areasmall, #advert300x260, #advert3area, #advert3areasmall, #advertBanner, #advertBox, #advertBoxRight, #advertBoxSquare, #advertColumn, #advertContainer, #advertControl4_advertLink, #advertCover, #advertDB, #advertMPUContainer, #advertMarkerHorizontalConatiner, #advertMarkerVerticalConatiner, #advertOverlay, #advertRight, #advertSection, #advertSeparator, #advertTop, #advertTopLarge, #advertTopSmall, #advertTower, #advertWrapper, #advert_01, #advert_04, #advert_05, #advert_07, #advert_1, #advert_125x125, #advert_250x250, #advert_300x2502, #advert_300x2503, #advert_561_01, #advert_561_02, #advert_561_03, #advert_561_04_container, #advert_561_04_left_end, #advert_561_04_right_end, #advert_561_05, #advert_561_07, #advert_back_160x600, #advert_back_300x250_1, #advert_back_300x250_2, #advert_banner, #advert_belowmenu, #advert_bottom_100x70, #advert_box, #advert_container, #advert_header, #advert_home01, #advert_home02, #advert_home03, #advert_home04, #advert_leaderboard, #advert_lrec_format, #advert_media, #advert_mid, #advert_mpu, #advert_mpu_1, #advert_mpu_2, #advert_right_skyscraper, #advert_sky, #advert_top, #advert_yell, #advertblock, #advertborder, #advertbox2, #advertbox3, #advertbox4, #adverthome, #adverti, #advertise, #advertise-here, #advertise-here-sidebar, #advertise-now, #advertise-sidebar, #advertise1, #advertise2, #advertiseBanner, #advertiseGoogle, #advertiseHere, #advertiseLink, #advertise_top, #advertisediv, #advertiseheretop, #advertisement-300x250, #advertisement-728x90, #advertisement-content, #advertisement-detail1, #advertisement-detail2, #advertisement-large, #advertisement-rightcolumn, #advertisement-text, #advertisement1, #advertisement160x600, #advertisement2, #advertisement3, #advertisement728x90, #advertisementArea, #advertisementBottomThreadUser, #advertisementBox, #advertisementDIV2, #advertisementFooterTop, #advertisementHeaderBottom, #advertisementHorizontal, #advertisementLigatus, #advertisementPrio2, #advertisementRight, #advertisementRightcolumn0, #advertisementRightcolumn1, #advertisementThread, #advertisementTop, #advertisement_RightPanel, #advertisement_banner, #advertisement_block, #advertisement_box, #advertisement_container, #advertisement_label, #advertisement_notice, #advertisementblock1, #advertisementblock2, #advertisementblock3, #advertisements_bottom, #advertisements_sidebar, #advertisements_top, #advertisementsarticle, #advertisementsxml, #advertiser-container, #advertiserLinks, #advertiserReports, #advertisers-caption, #advertisetop, #advertising-160x600, #advertising-300x250, #advertising-728x90, #advertising-banner, #advertising-caption, #advertising-container, #advertising-control, #advertising-mockup, #advertising-skyscraper, #advertising-top, #advertising2, #advertising3, #advertising300x250, #advertisingBlocksLeaderboard, #advertisingBottomFull, #advertisingHrefTop, #advertisingLeftLeft, #advertisingLink, #advertisingModule160x600, #advertisingModule728x90, #advertisingRightColumn, #advertisingRightRight, #advertisingTop, #advertisingTopWrapper, #advertising_1, #advertising_2, #advertising_300, #advertising_300_under, #advertising_300x105, #advertising_320, #advertising_728, #advertising_728_under, #advertising_btm, #advertising_column, #advertising_container, #advertising_contentad, #advertising_header, #advertising_holder, #advertising_horiz_cont, #advertising_iab, #advertising_top_container, #advertising_wrapper, #advertisment-block-1, #advertisment-horizontal, #advertisment1, #advertismentBottom728x90_, #advertismentElementInUniversalbox, #advertisment_content, #advertisment_panel, #advertismentgoogle, #advertistop_td, #advertleft, #advertorial, #advertorial-box, #advertorial-wrap, #advertorial1, #advertorial_block_3, #advertorial_links, #advertorial_red_listblock, #adverts, #adverts-top-container, #adverts-top-left, #adverts-top-middle, #adverts-top-right, #adverts_right, #advertscroll, #advertsingle, #advertspace, #advertssection, #adverttop, #advetisement_300x250, #advframe, #advgeoul, #advgoogle, #advman-2, #advr_mobile, #advsingle, #advt, #advt-right-skyscraper, #advt_bottom, #advtbar, #advtext, #advtop, #advtopright, #advx3_banner, #adwhitepaperwidget, #adwidget, #adwidget-5, #adwidget-6, #adwidget1, #adwidget2, #adwidget2_hidden, #adwidget3_hidden, #adwidget_hidden, #adwin, #adwin_rec, #adwith, #adwords-4-container, #adwords-box, #adwrap-295x295, #adwrap-722x90, #adwrap-729x90, #adwrap-966x90, #adwrapper, #adxBigAd, #adxBigAd2, #adxLeaderboard, #adxMiddle, #adxMiddle5, #adxMiddleRight, #adxSponLink, #adxSponLink2, #adxSponLinkA, #adxToolSponsor, #adx_ad, #adx_ad_bottom, #adx_ad_bottom_close, #adxtop, #adxtop2, #adzbanner, #adzerk, #adzerk1, #adzerk2, #adzerk_by, #adzone, #adzone-halfpage_1, #adzone-leaderboard_1, #adzone-leaderboard_2, #adzone-middle1, #adzone-middle2, #adzone-mpu_1, #adzone-mpu_2, #adzone-parallax_1, #adzone-right, #adzone-sidebarSmallPromo1, #adzone-sidebarSmallPromo2, #adzone-teads, #adzone-top, #adzone-wallpaper, #adzone-weatherbar-logo, #adzoneBANNER, #adzone_content, #adzonebanner, #adzoneheader, #aetn_3tier_ad_bar, #af_ad_large, #af_ad_small, #af_adblock, #afc-container, #affiliate_ad, #affinityBannerAd, #after-content-ad, #after-content-ads, #after-header-ad-left, #after-header-ad-right, #after-header-ads, #after_ad, #afterpostad, #agencies_ad, #agi-ad300x250, #agi-ad300x250overlay, #agi-sponsored, #alert_ads, #amazon-ads, #amazon_ad, #amazon_bsa_block, #ami_ad_cntnr, #amsSparkleAdFeedback, #amsSparkleAdWrapper, #amzn-native-ad-0, #amzn_assoc_ad_div_adunit0_0, #anAdScGame300x250, #analytics_ad, #analytics_banner, #anchorAd, #annoying_ad, #annoying_extra_ad_wrapper, #anyvan-ad, #ap-widget-ad, #ap-widget-ad-label, #ap_adframe, #ap_adtext, #ap_cu_overlay, #ap_cu_wrapper, #apiBackgroundAd, #apiTopAdContainer, #apiTopAdWrap, #apmNADiv, #apolload, #app_advertising_pregame_content, #app_advertising_rectangle, #app_advertising_rectangle_ph, #apt-homebox-ads, #araHealthSponsorAd, #area-adcenter, #area-left-ad, #area13ads, #area1ads, #article-ad, #article-ad-container, #article-advert, #article-agora-ad, #article-billboard-ad-1, #article-bottom-ad, #article-box-ad, #article-footer-sponsors, #article-island-ad, #article-sidebar-ad, #article-sponspred-content, #article-top-728x90-ad-wrapper, #articleAd, #articleAdReplacement, #articleBoard-ad, #articleLeftAdColumn, #articleSideAd, #article_LeftAdWords, #article_SponsoredLinks, #article_ad, #article_ad_1, #article_ad_3, #article_ad_bottom, #article_ad_bottom_cont, #article_ad_container, #article_ad_rt1, #article_ad_top, #article_ad_top_cont, #article_ad_w, #article_adholder, #article_ads, #article_advert, #article_banner_ad, #article_body_ad1, #article_bottom_ad01, #article_box_ad, #article_gallery_desktop_ad, #article_left_ad01, #article_sidebar_ad, #article_sidebar_ad_02, #articlead1, #articlead2, #articlead300x250r, #articleadblock, #articletop_ad, #articleview_ad, #articleview_ad2, #artist-ad-container, #as24-magazine-rightcol-adtag-1, #aside_ad, #asideads, #asinglead, #atad1, #atad2, #atlasAdDivGame, #atwAdFrame0, #atwAdFrame1, #atwAdFrame2, #atwAdFrame3, #atwAdFrame4, #autos_banner_ad, #aw-ad-container, #awds-nt1-ad, #awesome-ad, #awp_advertisements-2, #b-ad-choices, #b-adw, #b5-skyscraper-ad-3, #b5_ad_footer, #b5_ad_sidebar1, #b5_ad_top, #b5ad300, #bLinkAdv, #babAdTop, #backad, #background-ad-head-spacer, #background-adv, #background_ad_left, #background_ad_right, #background_ads, #backgroundadvert, #ban_300x250, #ban_728x90, #banner-300x250, #banner-300x250-area, #banner-300x250-north, #banner-300x600-area, #banner-336x280-north, #banner-336x280-south, #banner-468x60, #banner-728, #banner-728adtag, #banner-728adtag-bottom, #banner-728x90, #banner-728x90-area, #banner-ad, #banner-ad-container, #banner-ad-first, #banner-ad-last, #banner-ad-loader, #banner-ad-square-first, #banner-ad-square-last, #banner-ads, #banner-advert, #banner-advert-container, #banner-lg-ad, #banner-skyscraper, #banner120x600, #banner250x250, #banner300-top-right, #banner300x250, #banner468, #banner468x60, #banner600, #banner660x90, #banner728, #banner728x90, #banner975_container, #bannerAd, #bannerAdContainer1_1, #bannerAdContainer1_2, #bannerAdContainer1_3, #bannerAdContainer1_4, #bannerAdContainer1_5, #bannerAdContainer1_6, #bannerAdContainer2_1, #bannerAdContainer2_2, #bannerAdContainer2_3, #bannerAdContainer2_4, #bannerAdContainer2_5, #bannerAdContainer2_6, #bannerAdFrame, #bannerAdLInk, #bannerAdRight3, #bannerAdTop, #bannerAdWrap, #bannerAdWrapper, #bannerAd_ctr, #bannerAd_rdr, #bannerAds, #bannerAdsense, #bannerAdvert, #bannerGoogle, #banner_280_240, #banner_300_250, #banner_300x250_sidebar, #banner_468x60, #banner_ad, #banner_ad_Sponsored, #banner_ad_bottom, #banner_ad_div_fw, #banner_ad_footer, #banner_ad_module, #banner_ad_placeholder, #banner_ad_top, #banner_admicro, #banner_ads, #banner_adsense, #banner_adv, #banner_advertisement, #banner_adverts, #banner_content_ad, #banner_mpu1, #banner_mpu3, #banner_sedo, #banner_slot, #banner_spacer, #banner_topad, #banner_videoad, #banner_wrapper_top, #bannerad, #bannerad-bottom, #bannerad-top, #bannerad2, #banneradrow, #bannerads, #banneradspace, #banneradvert3, #barAdWrapper, #base-advertising-top, #base-board-ad, #baseAdvertising, #baseboard-ad, #baseboard-ad-wrapper, #basket-adContainer, #bbContentAds, #bb_ad_container, #bbadwrap, #bbccom_leaderboard, #bbccom_leaderboard_container, #bbccom_mpu, #bbccom_sponsor_section, #bbccom_sponsor_section_text, #bbccom_storyprintsponsorship, #bbo_ad1, #bcaster-ad, #bdnads-top-970x90, #before-footer-ad, #below-listings-ad, #below-post-ad, #belowAd, #belowContactBoxAd, #belowNodeAds, #below_comments_ad_holder, #below_content_ad_container, #belowad, #belowheaderad, #bg-footer-ads, #bg-footer-ads2, #bg_YieldManager-160x600, #bg_YieldManager-300x250, #bg_YieldManager-728x90, #bg_banner_120x600, #bg_banner_468x60, #bg_banner_728x90, #bgad, #bh_adFrame_ag_300x250_atf, #bh_adFrame_bh_300x250_atf, #bh_adFrame_bh_300x250_btf, #big-ad-switch, #big-box-ad, #bigAd, #bigAd1, #bigAd2, #bigAdDiv, #bigBannerAd, #bigBoxAd, #bigBoxAdCont, #big_ad, #big_ad_label, #big_ads, #bigad, #bigad300outer, #bigadbox, #bigadframe, #bigadspace, #bigadspot, #bigboard_ad, #bigboard_ad_ini, #bigbox-ad, #bigsidead, #billboard-ad-container, #billboard_ad { display: none !important; } </style><style type="text/css">#bingadcontainer2, #bl11adv, #blancco-ad, #block--ex_dart-ex_dart_adblade_article, #block-ad_blocks-0, #block-ad_cube-0, #block-ad_cube-1, #block-adsense-0, #block-adsense-2, #block-adsense_managed-0, #block-advert-content, #block-advert-content2, #block-advertisement, #block-bean-artadocean-splitter, #block-bean-artadocean-text-link-1, #block-bean-artadocean-text-link-2, #block-bean-artadocean300x250-1, #block-bean-artadocean300x250-3, #block-bean-artadocean300x250-6, #block-bean-in-content-ad, #block-boxes-taboola, #block-dart-dart-tag-ad_top_728x90, #block-dart-dart-tag-gfc-ad-top-2, #block-dctv-ad-banners-wrapper, #block-dfp-billboard-leaderboard, #block-dfp-mpu-1, #block-dfp-mpu-2, #block-dfp-mpu-3, #block-dfp-skyscraper_left_1, #block-dfp-skyscraper_left_2, #block-dfp-top, #block-display-ads-leaderboard, #block-ex_dart-ex_dart_adblade_article, #block-ex_dart-ex_dart_sidebar_ad_block_bottom, #block-ex_dart-ex_dart_sidebar_ad_block_top, #block-fan-ad-fan-ad-front-leaderboard-bottom, #block-fan-ad-fan-ad-front-medrec-top, #block-fcc-advertising-first-sidebar-ad, #block-google-ads, #block-ibtimestv-player-companion-ad, #block-localcom-localcom-ads, #block-openads-0, #block-openads-1, #block-openads-13, #block-openads-14, #block-openads-2, #block-openads-3, #block-openads-4, #block-openads-5, #block-openads-brand, #block-openx-0, #block-openx-1, #block-openx-4, #block-openx-5, #block-panels-mini-top-ads, #block-sponsors, #block-spti_ga-spti_ga_adwords, #block-thewrap_ads_250x300-0, #block-thewrap_ads_250x300-1, #block-thewrap_ads_250x300-2, #block-thewrap_ads_250x300-3, #block-thewrap_ads_250x300-4, #block-thewrap_ads_250x300-5, #block-thewrap_ads_250x300-6, #block-thewrap_ads_250x300-7, #block-views-Advertorial-block_5, #block-views-Advertorial-block_6, #block-views-Advertorial-block_7, #block-views-ad-directory-block, #block-views-advertisements-block, #block-views-advt-story-bottom-block, #block-views-custom-advertisement-2-block--2, #block-views-custom-advertisement-block--2, #block-views-premium-ad-slideshow-block, #block-views-sidebar-ad, #block-views-sponsor-block, #blockAd, #blockAds, #block_ad, #block_ad2, #block_ad_container, #block_advert, #block_advert1, #block_advert2, #block_advertisement, #block_timeout_sponsored_0, #blog-ad, #blog-advert, #blog-header-ad, #blogImgSponsor, #blog_ad_area, #blog_ad_content, #blog_ad_opa, #blog_ad_right, #blog_ad_top, #blogad, #blogad-wrapper, #blogad_728x90_header, #blogad_right_728x91_bottom, #blogad_top_300x250_sidebar, #blogads, #blogads_most_right_ad, #blox-big-ad, #blox-big-ad-bottom, #blox-big-ad-top, #blox-halfpage-ad, #blox-tile-ad, #blox-tower-ad, #bn_ad, #bnr-300x250, #bnr-468x60, #bnr-728x90, #bnrAd, #bnrhd468, #body-ads, #bodyAd1, #bodyAd2, #bodyAd3, #bodyAd4, #body_728_ad, #body_ad, #bodymainAd, #bonus-offers-advertisement, #book-ad, #bookmarkListDeckAdPlaceholder, #boss_banner_ad-2, #boss_banner_ad-3, #bot_ads, #botad, #botads2, #bott_ad2, #bott_ad2_300, #bottom-728-ad, #bottom-ad, #bottom-ad-1, #bottom-ad-banner, #bottom-ad-container, #bottom-ad-leaderboard, #bottom-ad-tray, #bottom-ad-wrapper, #bottom-add, #bottom-ads, #bottom-ads-container, #bottom-adspot, #bottom-advertising, #bottom-article-ad-336x280, #bottom-banner-spc, #bottom-boxad, #bottom-side-ad, #bottom-sponsor-add, #bottomAd, #bottomAd300, #bottomAdBlcok, #bottomAdCCBucket, #bottomAdContainer, #bottomAdSection, #bottomAdSense, #bottomAdSenseDiv, #bottomAdWrapper, #bottomAds, #bottomAdvBox, #bottomBannerAd, #bottomContentAd, #bottomDDAd, #bottomFullAd, #bottomGoogleAds, #bottomLeftAd, #bottomMPU, #bottomRightAd, #bottomRightAdContainer, #bottomRightAdSpace, #bottomSponsorAd, #bottom_ad, #bottom_ad_area, #bottom_ad_box, #bottom_ad_container, #bottom_ad_left, #bottom_ad_region, #bottom_ad_right, #bottom_ad_unit, #bottom_ad_wrapper, #bottom_adbox, #bottom_ads, #bottom_ads_container, #bottom_advert_container, #bottom_adwrapper, #bottom_banner_ad, #bottom_ex_ad_holder, #bottom_leader_ad, #bottom_overture, #bottom_player_adv, #bottom_sponsor_ads, #bottom_sponsored_links, #bottom_text_ad, #bottomad, #bottomad300, #bottomad_table, #bottomadbanner, #bottomadbar, #bottomadholder, #bottomads, #bottomadsdiv, #bottomadsense, #bottomadvert, #bottomadwrapper, #bottomcontentads, #bottomleaderboardad, #bottommpuAdvert, #bottommpuSlot, #bottomsponad, #bottomsponsoredresults, #box-ad, #box-ad-section, #box-ad-sidebar, #box-ads-small-1, #box-ads-small-2, #box-ads-tr, #box-ads300-picture-detail, #box-content-ad, #box-googleadsense-1, #box-googleadsense-r, #box1ad, #box2ad, #boxAD, #boxAd, #boxAd300, #boxAdContainer, #boxAdvert, #boxLightImageGalleryAd, #box_ad, #box_ad_container, #box_ad_middle, #box_ads, #box_advertisement, #box_advertising_info, #box_advertisment, #box_articlead, #box_mod_googleadsense, #box_text_ads, #boxad, #boxad1, #boxad2, #boxad3, #boxad4, #boxad5, #boxads, #boxes-box-ad300x250set2, #boxes-box-ad300x250set2block, #boxes-box-ad_300x250_1, #boxes-box-ad_728x90_1, #boxes-box-ad_mpu, #boxtube-ad, #bpAd, #bps-header-ad-container, #bq_homeMiddleAd, #br_ad, #brand-box-ad, #brand-box-ad-1-container, #branding_ad_comment, #branding_ad_header, #branding_click, #browse-ad-container, #browse_ads_ego_container, #browsead, #bsaadvert, #bsap_aplink, #btfAdNew, #btm_ads, #btmad, #btmsponsoredcontent, #btn-sponsored-features, #btnAds, #btnads, #btr_horiz_ad, #burn_header_ad, #bus-center-ad, #button-ads, #button-ads-horizontal, #button-ads-vertical, #buttonAdWrapper1, #buttonAdWrapper2, #buttonAds, #buttonAdsContainer, #button_ad_container, #button_ad_wrap, #button_ads, #buttonad-widget-3, #buttonad-widget-4, #buy-sell-ads, #buySellAds, #buysellads, #buysellads-4x1, #c-adzone, #c4_ad, #c4ad-Middle1, #c4ad-Top-parent, #c_ad_sb, #c_ad_sky, #c_sponsoredSquare, #c_upperad, #c_upperad_c, #caAdLarger, #carbonads-container, #card-ads-top, #catad, #catalyst-125-ads, #catalyst-ads-2, #category-ad, #category-sponsor, #category_sponsorship_ad, #cb-ad, #cb_medrect1_div, #cbs-video-ad-overlay, #cbz-ads-text-link, #cbz-comm-advert-1, #cellAd, #center-ad, #center-ad-group, #center-ads-72980, #center-three-ad, #centerAdsHeadlines, #center_ad-0, #centerads, #central-ads, #cgp-bigbox-ad, #ch-ads, #channel-ads-300-box, #channel-ads-300x600-box, #channel_ad, #channel_ads, #chartAdWrap, #charts_adv, #chatAdv2, #chatad, #cherry_ads, #chitikaAdBlock, #ciHomeRHSAdslot, #circ_ad, #circ_ad_300x100, #circ_ad_620x100, #circ_ad_holder, #circad_wrapper, #city_House_Ad_300x137, #clickforad, #cliczone-advert-left, #cliczone-advert-right, #clientAds, #closeAdsDiv, #closeable-ad, #cltAd, #cmMediaRotatorAdTLContainer, #cmn_ad_box, #cmn_ad_tag_head, #cmn_toolbar_ad, #cnhi_premium_ads, #cnnAboveFoldBelowAd, #cnnBottomAd, #cnnCMAd, #cnnRR336ad, #cnnSponsoredPods, #cnnTopAd, #cnnTowerAd, #cnnVPAd, #cnn_cnn_adtag-3, #coAd, #cobalt-ad-1-container, #coda_ad_728x90_9, #cokeAd, #col-right-ad, #col3_advertising, #colAd, #colRightAd, #collapseobj_adsection, #college_special_ad, #column-ads-bg, #column2-145x145-ad, #column4-google-ads, #columnAd, #columnTwoAdContainer, #column_adverts, #column_extras_ad, #commentAdWrapper, #commentTopAd, #comment_ad_zone, #comments-ad-container, #comments-ads, #comments_advert, #commercial-textlinks, #commercial_ads, #commercial_ads_footer, #common_right_ad_wrapper, #common_right_adspace, #common_right_lower_ad_wrapper, #common_right_lower_adspace, #common_right_lower_player_ad_wrapper, #common_right_lower_player_adspace, #common_right_player_ad_wrapper, #common_right_player_adspace, #common_right_right_adspace, #common_top_adspace, #community_ads, #compAdvertisement, #comp_AdsLeaderboardBottom, #comp_AdsLeaderboardTop, #companion-ad, #companionAd, #companionAdDiv, #companion_Ad, #companionad, #componentAdRectangle, #componentAdSkyscraper, #conduitAdPopupWrapper, #container-ad, #container-ad-content-rectangle, #container-ad-topright, #container-advMoreAbout, #container-polo-ad, #container-righttopads, #container-topleftads, #containerAds980, #containerLocalAds, #containerLocalAdsInner, #containerMrecAd, #containerSqAd, #container_ad, #container_top_ad, #contener_pginfopop1, #content-ad, #content-ad-header, #content-ads, #content-adver, #content-advertising-header, #content-advertising-right, #content-adwrapper, #content-area-ad, #content-columns-post-ad-bottom, #content-columns-post-ad-top, #content-header-ad, #content-left-ad, #content-right-ad, #contentAd, #contentAdBottomRight, #contentAdHalfpage, #contentAdSense, #contentAdTwo, #contentAds, #contentAds300x200, #contentAds300x250, #contentAds667x100, #contentAdsCatArchive, #contentBottomAdLeaderboard, #contentBoxad, #contentFooterAD, #contentMain_sponsoredResultsPanel, #contentTopAds2, #content_0_storyarticlepage_main_0_pnlAdSlot, #content_0_storyarticlepage_main_0_pnlAdSlotInner, #content_0_storyarticlepage_sidebar_0_pnlAdSlot, #content_0_storyarticlepage_sidebar_11_pnlAdSlot, #content_0_storyarticlepage_sidebar_6_pnlAdSlot, #content_11_pnlAdSlot, #content_11_pnlAdSlotInner, #content_16_pnlAdSlot, #content_16_pnlAdSlotInner, #content_2_pnlAdSlot, #content_2_pnlAdSlotInner, #content_3_twocolumnrightfocus_right_bottomright_0_pnlAdSlot, #content_3_twocolumnrightfocus_right_bottomright_1_pnlAdSlot, #content_4_threecolumnallfocus_right_0_pnlAdSlot, #content_7_pnlAdSlot, #content_7_pnlAdSlotInner, #content_9_twocolumnleftfocus_b_right_1_pnlAdSlot, #content_Ad, #content_ad, #content_ad_1, #content_ad_2, #content_ad_block, #content_ad_container, #content_ad_placeholder, #content_ad_square, #content_ad_top, #content_ads, #content_ads_content, #content_adv, #content_bottom_ad, #content_bottom_ads, #content_box_300body_sponsoredoffers, #content_box_adright300_google, #content_lower_center_right_ad, #content_mpu, #content_right_ad, #content_right_area_ads, #content_right_side_advertisement_on_top_wrapper, #contentad, #contentad-adsense-homepage-1, #contentad-adsense-homepage-2, #contentad-commercial-1, #contentad-content-box-1, #contentad-footer-tfm-1, #contentad-last-medium-rectangle-1, #contentad-lower-medium-rectangle-1, #contentad-sponsoredlinks-1, #contentad-story-bottom-1, #contentad-story-middle-1, #contentad-story-top-1, #contentad-superbanner-1, #contentad-superbanner-2, #contentad-top-adsense-1, #contentad_imtext, #contentad_right, #contentad_urban, #contentadcontainer, #contentads, #contentarea-ad, #contentarea-ad-widget-area, #contentinlineAd, #contents_post_ad, #contest-ads, #contextad, #contextual-ads, #contextual-ads-block, #contextual-ads-bricklet, #contextual-dummy-ad, #contextualad, #corner_ad, #cornerad, #cosponsor, #cosponsorTab, #coverADS, #coverads, #cpad_242306, #cph_cph_tlda_pnlAd, #crowd-ignite, #crowd-ignite-header, #csBotterAd, #csTopAd, #ct-ad-lb, #ctl00_AdPanel1, #ctl00_AdPanelISRect2, #ctl00_AdWords, #ctl00_Adspace_Top_Height, #ctl00_BottomAd, #ctl00_BottomAd2_AdArea, #ctl00_BottomAdPanel, #ctl00_ContentMain_BanManAd468_BanManAd, #ctl00_ContentPlaceHolder1_AdRotator3, #ctl00_ContentPlaceHolder1_BannerAd_TABLE1, #ctl00_ContentPlaceHolder1_DrillDown1_trBannerAd, #ctl00_ContentPlaceHolder1_TextAd_Pulse360AdPanel, #ctl00_ContentPlaceHolder1_ad12_adRotator_divAd, #ctl00_ContentPlaceHolder1_blockAdd_divAdvert, #ctl00_ContentPlaceHolder1_ctl00_ContentPlaceHolder1_pnlGoogleAdsPanel, #ctl00_ContentPlaceHolder1_ctl00_StoryContainer1_ImageHouseAd, #ctl00_ContentPlaceHolder1_toplead_news1_dvFlashAd, #ctl00_ContentPlaceHolder1_ucAdHomeRightFO_divAdvertisement, #ctl00_ContentPlaceHolder1_ucAdHomeRight_divAdvertisement, #ctl00_ContentPlaceHolder_PageHeading_Special_divGoogleAd2, #ctl00_ContentRightColumn_RightColumn_Ad1_BanManAd, #ctl00_ContentRightColumn_RightColumn_Ad1_googlePublisherAd, #ctl00_ContentRightColumn_RightColumn_Ad2_BanManAd, #ctl00_ContentRightColumn_RightColumn_Ad2_googlePublisherAd, #ctl00_ContentRightColumn_RightColumn_PremiumAd1_ucBanMan_BanManAd, #ctl00_Content_SquareAd_AdBox, #ctl00_Content_skyAd, #ctl00_Footer1_v5footerad, #ctl00_FooterHome1_AdFooter1_AdRotatorFooter, #ctl00_GoogleAd1, #ctl00_GoogleAd3, #ctl00_GoogleSkyscraper, #ctl00_Header1_AdHeader1_LabelHeaderScript, #ctl00_HyperLinkHouseAd, #ctl00_ImageHouseAd, #ctl00_LHTowerAd, #ctl00_LeftHandAd, #ctl00_MainContent_adDiv1, #ctl00_MainContent_adDiv2, #ctl00_MasterHolder_IBanner_adHolder, #ctl00_RightBanner_AdvertisementText, #ctl00_SiteHeader1_TopAd1_AdArea, #ctl00_TopAd, #ctl00_TowerAd, #ctl00_VBanner_adHolder, #ctl00__Content__RepeaterReplies_ctl03__AdReply, #ctl00_adCar, #ctl00_adFooter, #ctl00_advert_LargeMPU_div_AdPlaceHolder, #ctl00_advert_WideSky_Right_divOther, #ctl00_bottom_advert_728x90, #ctl00_cphMainContent_lblPartnerAds, #ctl00_cphMain_adView_dlAds_ctl01_advert_AboveAds_divOther, #ctl00_cphMain_hlAd1, #ctl00_cphMain_hlAd2, #ctl00_cphMain_hlAd3, #ctl00_cphMain_phMain_ctl00_ctl03_ctl00_topAd, #ctl00_cphRoblox_boxAdPanel, #ctl00_ctl00_MainPlaceHolder_itvAdSkyscraper, #ctl00_ctl00_RightColumn1_ctl04_csc300x250Ad1, #ctl00_ctl00_RightColumn1_ctl04_pnlAdBlock300x250Ad1, #ctl00_ctl00_RightPanePlaceHolder_pnlAdv, #ctl00_ctl00_ctl00_Main_Main_PlaceHolderGoogleTopBanner_MPTopBannerAd, #ctl00_ctl00_ctl00_Main_Main_SideBar_MPSideAd, #ctl00_ctl00_ctl00_divAdsTop, #ctl00_ctl00_ctl00_tableAdsTop, #ctl00_ctl00_ctl00_tdBannerAd, #ctl00_ctl00_pnlAdBottom, #ctl00_ctl00_pnlAdTop, #ctl00_ctl01_ctl00_tdBannerAd, #ctl00_ctl05_ctl00_tableAdsTop, #ctl00_ctl05_ctl00_tdBannerAd, #ctl00_ctl08_ctl00_tableAdsTop, #ctl00_ctl11_AdvertisementText, #ctl00_ctrlAdvert6_iframeAdvert, #ctl00_ctrlAdvert7_iframeAdvert, #ctl00_ctrlAdvert8_iframeAdvert, #ctl00_divAdSuper, #ctl00_dlTilesAds, #ctl00_fc_ctl02_AdControl, #ctl00_fc_ctl03_AdControl, #ctl00_fc_ctl04_AdControl, #ctl00_fc_ctl06_AdControl, #ctl00_headerAdd, #ctl00_m_skinTracker_m_adLBL, #ctl00_mainContent_lblSponsor, #ctl00_phContents_ctlNewsPanel_rptMainColumn_ctl02_ctlLigatusAds_pnlContainer, #ctl00_phContents_ctlNewsPanel_rptMainColumn_ctl02_pnlLigatusAds, #ctl00_phCrackerMain_ucAffiliateAdvertDisplayMiddle_pnlAffiliateAdvert, #ctl00_phCrackerMain_ucAffiliateAdvertDisplayRight_pnlAffiliateAdvert, #ctl00_pnlAdTop, #ctl00_siteHeader_bannerAd, #ctl00_skyscraperAdvertContainer, #ctl00_tc_ctl03_AdControl, #ctl00_tc_ctl04_AdControl, #ctl00_tc_ctl05_AdControl, #ctl00_tc_ctl06_AdControl, #ctl00_tc_ctl14_AdControl, #ctl00_tc_ctl15_AdControl, #ctl00_tc_ctl16_AdControl, #ctl00_tc_ctl18_AdControl, #ctl00_tc_ctl19_AdControl, #ctl00_topAd, #ctl00_ucAffiliateAdvertDisplay_pnlAffiliateAdvert, #ctl00_ucFooter_ucFooterBanner_divAdvertisement, #ctl08_ad1, #ctlDisplayAd1_lblAd, #ctl_bottom_ad, #ctl_bottom_ad1, #ctr-ad, #ctr_adtech2, #ctr_adtech_mpu_bot, #ctr_adtech_mpu_top, #ctrlsponsored, #ctx_listing_ads, #ctx_listing_ads2, #cubeAd, #cube_ad, #cube_ads, #cube_ads_inner, #cubead, #cubead-2, #cubead2, #currencies-sponsored-by, #custom-advert-leadboard-spacer, #custom-small-ad, #customAd, #cxnAdrail, #d-adCont543x90, #d-adCont728x90Inner, #d4_ad_google02, #dAdverts, #dItemBox_ads, #d_AdLink, #dap300x250, #dart-300x250, #dart-container-728x90, #dart_160x600, #dart_300x250, #dart_ad_block, #dart_ad_island, #dartad11, #dartad13, #dartad16, #dartad17, #dartad19, #dartad25, #dartad28, #dartad8, #dartad9, #db_ad, #dc-display-right-ad-1, #dc_ad_data_1, #dc_ad_data_2, #dc_ad_data_4, #dc_advertisement, #dcadSpot-Leader, #dcadSpot-LeaderFooter, #dclinkad, #dcol-sponsored, #dcomad_728x90_0, #dcomad_ad_728x90_1, #dcomad_top_300x250_0, #dcomad_top_300x250_1, #dcomad_top_300x251_2, #ddAd, #ddAdZone2, #defer-adright, #desktop-aside-ad-container, #detail_page_vid_topads, #devil-ad, #dfp-ad-1, #dfp-ad-2, #dfp-ad-billboard_leaderboard, #dfp-ad-billboard_leaderboard-wrapper, #dfp-ad-boombox, #dfp-ad-boombox-wrapper, #dfp-ad-boombox_2, #dfp-ad-boombox_2-wrapper, #dfp-ad-boombox_3, #dfp-ad-boombox_3-wrapper, #dfp-ad-boombox_4, #dfp-ad-boombox_4-wrapper, #dfp-ad-boombox_5, #dfp-ad-boombox_5-wrapper, #dfp-ad-clone_of_sidebar_top, #dfp-ad-content_1-wrapper, #dfp-ad-content_2-wrapper, #dfp-ad-content_3-wrapper, #dfp-ad-content_4-wrapper, #dfp-ad-dfp_ad_atf_728x90, #dfp-ad-dfp_ad_atf_728x90-wrapper, #dfp-ad-fm_300x250-wrapper, #dfp-ad-half_page-wrapper, #dfp-ad-half_page_sidebar-wrapper, #dfp-ad-home_1-wrapper, #dfp-ad-home_2-wrapper, #dfp-ad-home_3-wrapper, #dfp-ad-homepage_300x250-wrapper, #dfp-ad-homepage_728x90, #dfp-ad-homepage_728x90-wrapper, #dfp-ad-kids_300x250-wrapper, #dfp-ad-large_rectangle, #dfp-ad-large_rectangle-wrapper, #dfp-ad-leaderboard, #dfp-ad-leaderboard-wrapper, #dfp-ad-local_300x250-wrapper, #dfp-ad-medium_rectangle, #dfp-ad-mediumrect-wrapper, #dfp-ad-mediumrectangle-wrapper, #dfp-ad-mediumrectangle2-wrapper, #dfp-ad-mosad_1, #dfp-ad-mosad_1-wrapper, #dfp-ad-mpu1, #dfp-ad-mpu2, #dfp-ad-mpu_1, #dfp-ad-mpu_1-wrapper, #dfp-ad-mpu_2, #dfp-ad-mpu_2-wrapper, #dfp-ad-mpu_3, #dfp-ad-mpu_3-wrapper, #dfp-ad-ne_carousel_300x250, #dfp-ad-ne_carousel_300x250-wrapper, #dfp-ad-ne_column3a_300x250, #dfp-ad-ne_column3a_300x250-wrapper, #dfp-ad-ne_news2_468x60, #dfp-ad-ne_news2_468x60-wrapper, #dfp-ad-pencil_pushdown, #dfp-ad-pencil_pushdown-wrapper, #dfp-ad-right1, #dfp-ad-right2, #dfp-ad-right3, #dfp-ad-schedule_300x250-wrapper, #dfp-ad-slot2, #dfp-ad-slot3, #dfp-ad-slot3-wrapper, #dfp-ad-slot4-wrapper, #dfp-ad-slot5, #dfp-ad-slot5-wrapper, #dfp-ad-slot6, #dfp-ad-slot6-wrapper, #dfp-ad-slot7, #dfp-ad-slot7-wrapper, #dfp-ad-stamp_1, #dfp-ad-stamp_1-wrapper, #dfp-ad-stamp_2, #dfp-ad-stamp_2-wrapper, #dfp-ad-stamp_3, #dfp-ad-stamp_3-wrapper, #dfp-ad-stamp_4, #dfp-ad-stamp_4-wrapper, #dfp-ad-top, #dfp-ad-tower_1, #dfp-ad-tower_1-wrapper, #dfp-ad-tower_2, #dfp-ad-tower_2-wrapper, #dfp-ad-tower_half_page, #dfp-ad-tower_half_page-wrapper, #dfp-ad-tv_300x250-wrapper, #dfp-ad-wallpaper, #dfp-ad-wallpaper-wrapper, #dfp-article-mpu, #dfp-article-related-mpu, #dfp-middle, #dfp-middle1, #dfpAd, #dfp_ad_1, #dfp_ad_16, #dfp_ad_2, #dfp_ad_20, #dfp_ad_21, #dfp_ad_3, #dfp_ad_7, #dfp_ad_DictHome_300x250, #dfp_ad_DictHome_728x90, #dfp_ad_Entry_160x600, #dfp_ad_Entry_180x150, #dfp_ad_Entry_300x250, #dfp_ad_Entry_728x90, #dfp_ad_Entry_Btm_300x250, #dfp_ad_Entry_EntrySetA_300x250, #dfp_ad_Entry_EntrySetA_728x90, #dfp_ad_Entry_EntrySetB_300x250, #dfp_ad_Entry_EntrySetB_728x90, #dfp_ad_Entry_EntrySetC_728x90, #dfp_ad_Home_300x250, #dfp_ad_Home_728x90, #dfp_ad_Home_Btm_300x250, #dfp_ad_IC_728x90, #dfp_ad_InternalAdX_300x250_right, #dfp_ad_Internal_EntryBr_300x250, #dfp_ad_Internal_Home_250x262, #dfp_ad_Result_728x90, #dfp_ad_SecContent_300x250, #dfp_ad_Thesaurus_728x90, #dfp_ad_mpu, #dfp_container, #dfpad-0, #dfrads-widget-6, #dfrads-widget-7, #dhm-bar, #dict-adv, #direct-ad, #disable-ads-container, #displayAd, #displayAdSet, #display_ad, #displayad_bottom-page, #div-ad-1x1, #div-ad-1x1_3, #div-ad-2, #div-ad-bottom, #div-ad-coupon_1, #div-ad-coupon_10, #div-ad-coupon_11, #div-ad-coupon_12, #div-ad-coupon_2, #div-ad-coupon_3, #div-ad-coupon_4, #div-ad-coupon_5, #div-ad-coupon_6, #div-ad-coupon_7, #div-ad-coupon_8, #div-ad-coupon_9, #div-ad-flex, #div-ad-inread, #div-ad-leaderboard, #div-ad-r, #div-ad-r1, #div-ad-top, #div-adcenter1, #div-adcenter2, #div-adid-4000, #div-dfp-BelowContnet, #div-gpt-ad-lr-cube1, #div-gpt-ad-mrec-5, #div-gpt-ad-spotlight, #div-id-for-interstitial-ad, #div-insticator-ad-1, #div-insticator-ad-2, #div-social-ads, #div-vip-ad-banner, #div-web-ad-billboard, #div-web-ad-content-article, #div-web-ad-content-ressort, #div-web-ad-marginale-1, #div-web-ad-marginale-2, #div-web-ad-marginale-3, #div-web-ad-marginale-4, #div-web-ad-marginale-5, #div-web-ad-performance, #divAd, #divAdBox, #divAdHere, #divAdHorizontal, #divAdLeft, #divAdRight, #divAdSpecial, #divAdWrapper, #divAdd728x90, #divAdd_Right, #divAdd_Top, #divAds, #divAdsTop, #divAdv300x250, #divAdvertisement, #divAdvertisingSection, #divArticleInnerAd, #divBannerTopAds, #divBottomad1, #divBottomad2, #divDoubleAd, #divFoldersAd, #divFooterAd, #divFooterAds, #divLeftAd12, #divLeftRecAd, #divMenuAds, #divReklamaTop, #divRightNavAdsLoader, #divTopAd, #divTopAds, #divWNAdHeader, #divWNAdUnitLanding, #divWrapper_Ad, #div_ad_TopRight, #div_ad_float, #div_ad_holder, #div_ad_leaderboard, #div_content_mid_lft_ads, #div_googlead, #div_header_sponsors, #div_prerollAd_1, #div_side_big_ad, #div_video_ads, #divadfloat, #divadsensex, #divmiddlerightad, #divuppercenterad, #divupperrightad, #dlads, #dni-advertising-skyscraper-wrapper, #dni-header-ad, #dnn_AdBannerPane, #dnn_Advertisement, #dnn_adSky, #dnn_adTop, #dnn_ad_banner, #dnn_ad_island1, #dnn_ad_skyscraper, #dnn_ad_sponsored_links, #dnn_banner_120x600, #dnn_banner_486x60, #dnn_ctl00_Ad2Pane, #dnn_dnn_dartBanner, #dnn_googleAdsense_a, #dnn_playerAd, #dnn_sponsoredLinks, #docmainad, #dogear_promo, #dotnAd_300x250_c20, #double-card-ad, #doubleClickAds3, #doubleClickAds_bottom_big_box, #doubleClickAds_bottom_skyscraper, #doubleClickAds_top_banner, #doubleclick-island, #download-leaderboard-ad-bottom, #download-leaderboard-ad-top, #downloadAd, #download_ad, #download_ad-box, #download_ads, #download_slide_ad, #dp_ad_1, #dp_ads1, #drudge-column-ads-14, #drudge-column-ads-2, #drudge-column-ads-5, #drudge-column-ads-7, #ds-mpu, #dsStoryAd, #ds_ad_north_leaderboard, #dvAd1Data, #dvAd1main, #dvAd2Center, #dvAd5Data, #dvAd5Main, #dvAdHead, #dvCenterAd, #dvad2, #dvad2main, #dvad5, #dvad6cntnr, #dvad6main, #dvadfirst, #dvadfirstmain, #dvadscnd, #dvadsecondmain, #dvsmladlft, #dvsmladrgt, #dynamicAdDiv, #dynamicAdWinDiv, #ear_ad, #eastAds, #ebsponsoredads, #editorsmpu, #elections-ad-container, #elite-ads, #em_ad_superbanner, #embedAD, #embedded-ad, #embeded_ad_content_container, #entrylist_ad, #epmads-holder, #eshopad-728x90, #eventAd, #event_ads, #events-adv-side1, #events-adv-side2, #events-adv-side3, #events-adv-side4, #events-adv-side5, #events-adv-side6, #evotopTen_advert, #ex-ligatus, #ex_dart--ex_dart_header_ad, #exads, #exoAd, #expandableAd, #expandable_welcome_ad, #expanderadblock, #external-links-column-ad, #externalAd, #extra-search-ads, #extraAd, #extraAdsBlock, #ezadswidget-2, #f2p-ad-cnt, #f_ad, #f_adsky, #facebook-ad, #fav-advert, #fav-advertwrap, #fb_adbox, #fb_rightadpanel, #fearless_responsive_image_ad-2, #featAds, #featureAd, #featureAdSpace, #feature_ad, #feature_adlinks, #featuread, #featured-ad-left, #featured-ad-right, #featured-ads, #featured-advertisements, #featuredAdContainer2, #featuredAdWidget, #featuredAds, #featuredSponsors, #featured_ad_links, #featured_ad_widget_area, #featured_sponsor_cnt, #feed_links_ad_container, #feedjiti-footerTR, #ffsponsors, #file_sponsored_link, #fin_ad_728x90_bottom, #fin_advertorial_features, #fin_dc_ad_300x100_pos_1, #fin_ds_homepage_adtag_468x60, #first-300-ad, #first-adframe, #first-adlayer, #firstAdUnit, #first_ad, #first_ad_unit, #firstad, #fixedAd, #flAdData6, #fl_hdrAd, #flash_ads_1, #flashad, #flex_sponsored_links, #flexiad, #flipbookAd, #floatAD_l, #floatAD_r, #floatads, #floating-ad-spacer, #floating-ads, #floating-advert, #floatingAd, #floatingAdContainer, #floatingAds, #floating_ad, #floating_ad_container, #floatyContent, #foot-ad-1, #foot-add, #footAds, #footad, #footer-ad, #footer-ad-728, #footer-ad-block, #footer-ad-box, #footer-ad-col, #footer-ad-google, #footer-ad-large, #footer-ad-loader, #footer-ad-shadow, #footer-ad-unit, #footer-ad-wrapper, #footer-ads, #footer-adspace, #footer-adv, #footer-advert, #footer-advert-area, #footer-advertisement, #footer-adverts, #footer-adwrapper, #footer-affl, #footer-banner-ad, #footer-leaderboard-ad, #footer-sponsored, #footerAd, #footerAdBg, #footerAdBottom, #footerAdBox, #footerAdDiv, #footerAdLink, #footerAdSpecial, #footerAdd, #footerAds, #footerAdsPlacement, #footerAdvert, #footerAdvertisement, #footerAdverts, #footerGoogleAd, #footer_AdArea, #footer_ad, #footer_ad_01, #footer_ad_block, #footer_ad_cloud, #footer_ad_container, #footer_ad_frame, #footer_ad_holder, #footer_ad_inventory, #footer_ad_modules, #footer_adcode, #footer_add, #footer_addvertise, #footer_ads, #footer_ads_holder, #footer_adsense_ad, #footer_adspace, #footer_adv, #footer_advertising, #footer_leaderboard_ad, #footer_text_ad, #footerad, #footerad728, #footerads, #footeradsbox, #footeradvert, #form_bottomad, #forum_top_ad, #forumlist-ad, #four_ads, #fp_rh_ad, #fpad1, #fpad2, #fpv_companionad, #fr_ad_center, #fr_adtop, #frameAd, #frameTextAd2, #frame_admain, #free_ad, #frmRightnavAd, #frnAdSky, #frnBannerAd, #frnContentAd, #front-ad-cont, #front-page-advert, #frontPageAd, #front_ad728, #front_adtop_content, #front_advert, #front_mpu, #front_mpu_content, #frontlowerad, #frontpage_ad1, #frontpage_ad2, #ft-ad, #ft-ad-1, #ft-ad-container, #ft-ads, #ft_mpu, #ftad1, #ftad2, #full_banner_ad, #fulldown_ads_box, #fulldown_ads_frame, #fullsizebanner_468x60, #fullstory-google-textad, #fusionad, #fw-advertisement, #fwAdBox, #g-adblock2, #gAds, #gBnrAd, #gBottomRightAd, #g_ad, #g_adsense, #ga_300x250, #gad300x250, #gads-pub, #gads300x250, #gads_middle, #galleries-tower-ad, #gallery-ad, #gallery-ad-m0, #gallery-advert, #gallery-below-line-advert, #gallery-page-ad-bigbox, #gallery-random-ad, #gallery-sidebar-advert, #gallery-slideshow-interstitial-ad, #gallery_ad, #gallery_ads, #gallery_header_ad, #galleryad1, #game-ad, #game-info-ad, #gameAdMiddle, #gameAdTopMiddle, #gameSquareAd, #game_header_ad, #game_profile_ad_300_250, #gamead, #gameads, #gamepage_ad, #gameplay_ad, #games-mpu-container, #games_ad_container, #gasense, #gbl_topmost_ad, #gcommonad, #genad, #geoAd, #getUnderplayerIDAd, #gf-mrecs-ads, #gft-adChoicesCopy, #ggl-ad, #gglads, #gglads213A, #gglads213B, #ggogle_AD, #gl_ad_300, #glamads, #glinkswrapper, #global-banner-ad, #globalHeader_divAd, #globalLeftNavAd, #globalTopNavAd, #global_header_ad, #global_header_ad_area, #gm-ad-lrec, #gmi-ResourcePageAd, #gmi-ResourcePageLowerAd, #gnadww, #go-ads-double-2, #go-ads-double-3, #goad1, #goads, #gog_ad, #gooadtop, #google-ad, #google-ad-art, #google-ad-table-right, #google-ad-tower, #google-ads, #google-ads-bottom, #google-ads-bottom-container, #google-ads-container, #google-ads-container1, #google-ads-header, #google-ads-left-side, #google-adsense, #google-adsense-for-content, #google-adsense-mpusize, #google-adv-728x90, #google-adwords, #google-afc, #google-post-ad, #google-post-adbottom, #google-top-ads, #google336x280, #google468x60, #googleAd, #googleAdArea, #googleAdBottom, #googleAdBox, #googleAdMid, #googleAdSenseAdRR, #googleAdTop, #googleAdView, #googleAdYarrp, #googleAd_words, #googleAds, #googleAdsFrame, #googleAdsSml, #googleAdsense, #googleAdsenseAdverts, #googleAdsenseBanner, #googleAdsenseBannerBlog, #googleAdwordsModule, #googleAfcContainer, #googleSearchAds, #googleShoppingAdsRight, #googleShoppingAdsTop, #googleSubAds, #googleTxtAD, #google_ad, #google_ad_468x60_contnr, #google_ad_EIRU_newsblock, #google_ad_below_stry, #google_ad_container, #google_ad_container_right_side_bar, #google_ad_inline, #google_ad_test, #google_ad_top, #google_ads, #google_ads_1, #google_ads_aCol, #google_ads_box, #google_ads_div_Blog_300, #google_ads_div_Front-160x600, #google_ads_div_Raw_Override, #google_ads_div_Second_160, #google_ads_div_header1, #google_ads_div_header2, #google_ads_div_video_wallpaper_ad_container, #google_ads_frame, #google_ads_frame1_anchor, #google_ads_frame2_anchor, #google_ads_frame3_anchor, #google_ads_frame4_anchor, #google_ads_frame5_anchor, #google_ads_frame6_anchor, #google_ads_frame_quad, #google_ads_frame_vert, #google_ads_test, #google_ads_top, #google_ads_wide, #google_adsense, #google_adsense_ad, #google_adsense_home_468x60_1, #google_textlinks, #googlead, #googlead-leaderboard, #googlead-left, #googlead-post-mpu, #googlead-sidebar-middle, #googlead-sidebar-top, #googlead01, #googlead1, #googlead2, #googlead_outside, #googleadbig, #googleadleft, #googleads, #googleads1, #googleads_h_injection, #googleads_mpu_injection, #googleadsense, #googleadsense300x250, #googleadsrc, #googleadstop, #googlebanner, #googleblock300, #googlesponsor, #googletextads, #googtxtad, #gpt-ad-1, #gpt-ad-halfpage, #gpt-ad-rectangle1, #gpt-ad-rectangle2, #gpt-ad-skyscraper, #gpt-ad-story_rectangle3, #gpt2_ads_widget-10, #gpt2_ads_widget-6, #gpt2_ads_widget-7, #gpt2_ads_widget-8, #gpt2_ads_widget-9, #gpt_ad_panorama_top, #gpt_ad_small_insider_1, #gpt_unit_videoAdSlot1_0, #gridAdSidebar, #gridAdSidebarRight, #grid_ad, #grouponAdContainer, #gsyadrectangleload, #gsyadrightload, #gsyadtop, #gsyadtopload, #gtAD, #gtopadvts, #gtv_tabSponsor, #gwt-debug-ad, #h-ads, #hAd, #hAdv, #h_ads0, #h_ads1, #half-page-ad, #halfPageAd, #halfe-page-ad-box, #hb-header-ad, #hcf-ad-wrapper, #hd-ads, #hd-banner-ad, #hd_ad, #hd_ad_wp, #hdr-ad, #hdr-banner-ad, #hdrAdBanner, #hdrAds, #hdtv_ad_ss, #head-ad, #head-ad-1, #head-ads, #head-advertisement, #head-banner468, #head1ad, #headAd, #headAds, #headAdv, #headGoogleAffiliateLinkblock, #head_ad, #head_ad0, #head_ad_area, #head_ads, #head_advert, #headad, #headadvert, #header-ad, #header-ad-1, #header-ad-background, #header-ad-block, #header-ad-bottom, #header-ad-container, #header-ad-holder, #header-ad-label, #header-ad-left, #header-ad-placeholder, #header-ad-rectangle-container, #header-ad-right, #header-ad-wrap, #header-ad-wrapper, #header-ad2, #header-ad2010, #header-ads, #header-ads-wrapper, #header-adsense, #header-adspace, #header-adv, #header-advert, #header-advert-panel, #header-advertisement, #header-advertising, #header-adverts, #header-advrt, #header-banner-728-90, #header-banner-ad, #header-banner-spc, #header-block-ads, #header-google, #header-house-ad, #header-lb-ad, #header-leader-ad, #header-leader-ad-2, #header-menu-horizontal-ad-superbanner, #header-top-ads-text, #headerAd, #headerAdBackground, #headerAdButton, #headerAdContainer, #headerAdSpace, #headerAdUnit, #headerAdWrap, #headerAds, #headerAds4, #headerAdsWrapper, #headerAdv, #headerAdvert, #headerBannerAdNew, #headerNewAdsContainer, #headerNewAdsContainerB, #headerTopAd, #headerTopAdWide, #header_1_adv, #header_ad, #header_ad_167, #header_ad_728, #header_ad_728_90, #header_ad_banner, #header_ad_block, #header_ad_container, #header_ad_leaderboard, #header_ad_units, #header_ad_widget, #header_ad_wrap, #header_adbox, #header_adcode, #header_ads, #header_ads2, #header_ads_2, #header_ads_p, #header_adsense, #header_adv, #header_advert, #header_advertisement, #header_advertisement_top, #header_advertising, #header_adverts, #header_bottom_ad, #header_flag_ad, #header_leaderboard_ad_container, #header_publicidad, #header_right_ad, #header_sponsors, #header_top_ad, #headerad, #headeradbox, #headeradcontainer, #headerads, #headeradsbox, #headeradsense, #headeradspace, #headeradvert1div, #headeradvertholder, #headeradwrap, #headergooglead, #headerprimaryad, #headersponsors, #headingAd, #headline-sponsor, #headline_ad, #headlinesAdBlock, #hi5-ad-1, #hidadvnet, #hiddenadAC, #hide_ad_section_v2, #hideads, #hideads1, #hl-sponsored-links, #hl-sponsored-results, #hl-top-ad, #hldhdAds, #hly_ad_side_bar_tower_left, #hly_inner_page_google_ad, #hmt-widget-ad-unit-3, #holder-storyad, #holdunderad, #home-ad, #home-ad-block, #home-ad-slot, #home-adv-300x250, #home-advert-module, #home-advertise, #home-banner-ad, #home-left-ad, #home-page-listing-ad, #home-rectangle-ad, #home-right-col-ad, #home-side-ad, #home-top-ads, #homeAd, #homeAdLeft, #homeAds, #homeArticlesAd, #homeBottomAdWrapperInner, #homeMPU, #homePageBotAd, #homeSideAd, #homeTopRightAd, #home_ad, #home_ad_sub_spotlight, #home_ads_top_hold, #home_ads_vert, #home_bottom_ad, #home_contentad, #home_feature_ad, #home_lower_center_right_ad, #home_mpu, #home_sec2_adverts, #home_sidebar_ad, #home_spensoredlinks, #home_top_right_ad, #homead, #homegoogletextad, #homeheaderad, #homepage-ad, #homepage-adbar, #homepage-footer-ad, #homepage-header-ad, #homepage-right-rail-ad, #homepage-sidebar-ad, #homepage-sidebar-ads, #homepageAd, #homepageAdsTop, #homepageFooterAd, #homepageGoogleAds, #homepage__desktop-lead-ad-wrap, #homepage__lead-ad-slot, #homepage_ad, #homepage_middle_ads, #homepage_middle_ads_2, #homepage_middle_ads_3, #homepage_rectangle_ad, #homepage_right_ad, #homepage_right_ad_container, #homepage_top_ad, #homepage_top_ads, #homepagead_300x250, #homepageadvert, #homestream-advert3, #hometop_234x60ad, #hometopads, #horAd, #hor_ad, #horadslot, #horizad, #horizads728, #horizontal-ad, #horizontal-adspace, #horizontal-banner-ad, #horizontal-banner-ad-container, #horizontalAd, #horizontal_ad, #horizontal_ad2, #horizontal_ad_top, #horizontalad, #horizontalads, #hot-deals-ad, #hottopics-advert, #hours_ad, #houseAd, #hovered_sponsored, #hp-header-ad, #hp-mpu, #hp-right-ad, #hp-store-ad, #hpSponsor, #hpV2_300x250Ad, #hpV2_googAds, #hp_ad300x250, #hp_right_ad_300, #i9lsdads, #i_ads_table, #iaa_ad, #ibt_local_ad728, #icePage_SearchLinks_AdRightDiv, #icePage_SearchLinks_DownloadToolbarAdRightDiv, #icePage_SearchResults_ads0_SponsoredLink, #icePage_SearchResults_ads1_SponsoredLink, #icePage_SearchResults_ads2_SponsoredLink, #icePage_SearchResults_ads3_SponsoredLink, #icePage_SearchResults_ads4_SponsoredLink, #icom-ad-top, #idDivAd, #idMapAdvertising, #idRightAdArea, #idSponsoredresultend, #idSponsoredresultstart, #id_SearchAds, #ifmSocAd, #iframe-ad, #iframe-ad-container-Top3, #iframeAd_2, #iframeRightAd, #iframeTopAd, #iframe_ad_2, #iframe_ad_300, #iframe_ad_728, #iframe_container300x250, #iframead-300x250, #ignad_medrec, #ii_banner_ads, #imPopup, #im_box, #im_popupDiv, #im_popupFixed, #ima_ads-2, #ima_ads-3, #ima_ads-4, #imageGalleryAd, #imageGalleryAdHeadLine, #imageGalleryAdPlaceholder, #image_selector_ad, #imageadsbox, #imgCollContentAdIFrame, #imgad1, #imu_ad_module, #in-article-ad, #in-content-ad, #in-story-ad-wrapper, #inVideoAd, #in_ad_col_a, #in_post_ad_middle_1, #in_serp_ad, #inadspace, #inarticlead, #inc-ads-bigbox, #index-ad, #index-bottom-advert, #indexSquareAd, #index_ad, #indexad, #indexad300x250l, #indexsmallads, #indiv_adsense, #influads_block, #infoBottomAd, #inhousead, #initializeAd, #injectableTopAd, #inline-ad, #inline-advert, #inline-story-ad, #inline-story-ad2, #inlineAd, #inlineAdCont, #inlineAdtop, #inlineAdvertisement, #inlineBottomAd, #inline_ad, #inline_ad_section, #inline_search_ad, #inlinead, #inlineads, #inlinegoogleads, #inlist-ad-block, #inner-ad, #inner-advert-row, #inner-deals-ads, #inner-top-ads, #innerad, #innerpage-ad, #innovativeadspan, #inside-page-ad, #insideCubeAd, #insidearticleBodyAd, #insider_ad_wrapper, #insticator-container, #instoryad, #instoryadtext, #instoryadwrap, #insurance-ad-1-container, #int-ad, #intAdUnit, #int_ad, #interads, #internalAdvert, #internalads, #interstitialAd, #interstitialAdContainer, #interstitialAdUnit, #interstitial_ad, #interstitial_ad_container, #interstitial_ad_wrapper, #interstitial_ads, #interviews-ad, #introAds, #invid_ad, #ip-ad-leaderboard, #ip-ad-skyscraper, #ipadv, #iq-AdSkin, #iqadcontainer, #iqadoverlay, #iqadtile1, #iqadtile11, #iqadtile14, #iqadtile15, #iqadtile2, #iqadtile3, #iqadtile4, #iqadtile5, #iqadtile8, #iqadtile9, #iqd_align_Ad, #iqd_mainAd, #iqd_rightAd, #iqd_topAd, #ir-sidebar-ad, #irgoogleadsense, #islandAd, #islandAdPan, #islandAdPane, #islandAdPane2, #islandAdPaneGoogle, #islandAdSponsored, #island_ad_top, #islandad, #isliveContainer, #issue-sidebar-ad, #item-detail-feature-ad, #itemGroupAd2, #iv160ad, #iv728ad, #iwad, #j_ad, #j_special_ad, #ji_medShowAdBox, #jmp-ad-buttons, #job_ads_container, #jobs-ad, #jobsAdBox, #joead, #joead2, #js-ad-leaderboard, #js-image-ad-mpu, #js-outbrain-rightrail-ads-module, #js-site-nav-ad-wrap, #js-wide-ad, #js_adsense, #jt-advert, #jupiter-ads, #ka_adFullBanner, #ka_adMediumRectangle, #ka_adRightSkyscraperWide, #ka_adsense_container, #ka_samplead, #kads-main, #kamidarticle-adnotice, #kamidarticle-middle-content, #karmaAds, #kaufDA-widget, #kb-ad-banner, #kbbAdsMainCenterAd, #kdz_ad1, #kdz_ad2, #keen_overlay_ad_display, #keyadvertcontainer, #khAdSpace, #ksperAD, #l_home-keen_ad_mask, #landing-adserve, #landing-adserver, #lapho-top-ad-1, #large-ads, #large-rectange-ad, #large-rectange-ad-2, #large-screen-ads, #large-skyscraper-ad, #largeAd, #largeAds, #large_rec_ad1, #largead, #lateAd, #lateralAdWrapper, #launchpad-ads-2, #layerAds_layerDiv, #layerTLDADSERV, #layer_ad, #layer_ad_content, #layer_ad_main, #layer_adv1, #layerad, #layeradsense, #layout-header-ad-wrapper, #lb-ad, #lb-sponsor-left, #lb-sponsor-right, #lbAdBar, #lbAdBarBtm, #lblAds, #lead-ads, #lead_ad, #leadad_1, #leadad_2, #leader-ad, #leader-board-ad, #leaderAd, #leaderAdContainer, #leaderAdContainerOuter, #leaderBoardAd, #leader_ad, #leader_board_ad, #leaderad, #leaderad_section, #leaderadvert, #leaderboard-ad, #leaderboard-ad-1, #leaderboard-ad-1-container, #leaderboard-ad-1_iframe, #leaderboard-ad-2, #leaderboard-ad-2_iframe, #leaderboard-ad-3, #leaderboard-ad-3_iframe, #leaderboard-ad-4, #leaderboard-ad-4_iframe, #leaderboard-ad-5, #leaderboard-ad-5_iframe, #leaderboard-ad-bottom, #leaderboard-ad-bottom-container, #leaderboard-ad-container, #leaderboard-ad-container-1, #leaderboard-advertisement, #leaderboard-bottom-ad, #leaderboardAd, #leaderboardAdArea, #leaderboardAdArea2, #leaderboardAdLabel, #leaderboardAdSibling, #leaderboardAdTop, #leaderboardAds, #leaderboardAdvert, #leaderboardAdvertFooter, #leaderboardBottomAd, #leaderboard_728x90, #leaderboard_Ad, #leaderboard_ad, #leaderboard_ad_gam, #leaderboard_ad_main, #leaderboard_ad_unit, #leaderboard_ads, #leaderboard_bottom_ad, #leaderboard_top_ad, #leaderboardad, #leaderboardadtagwidget-2, #learad, #leatherboardad, #left-ad, #left-ad-1, #left-ad-2, #left-ad-col, #left-ad-skin, #left-bottom-ad, #left-col-ads-1, #left-lower-adverts, #left-lower-adverts-container, #left-rail-ad, #leftAD, #leftAdAboveSideBar, #leftAdCol, #leftAdContainer, #leftAdMessage, #leftAdSpace, #leftAd_fmt, #leftAd_rdr, #leftAds, #leftAdsSmall, #leftAdvert, #leftBanner-ad, #leftColumnAdContainer, #leftGoogleAds, #leftSectionAd300-100, #leftTopAdWrapper, #left_ad, #left_ads, #left_adsense, #left_adspace, #left_adv, #left_advertisement, #left_bg_ad, #left_block_ads, #left_float_ad, #left_global_adspace, #left_side_ads, #left_sidebar_ads, #left_skyscraper_ad, #left_ws_ad_container, #leftad, #leftadg, #leftads, #leftcolAd, #leftcolumnad, #leftforumad, #leftframeAD, #lg-banner-ad, #lgfRightBarAd, #lhsBottomAd, #li-right-geobooster-oas, #ligatus, #ligatusdiv, #lightboxAd, #lilo_imageAd, #linebreak-ads, #linkAdSingle, #linkAds, #link_ads, #linkads, #links-ads-detailnews, #listadholder, #liste_top_ads_wrapper, #listing-ad, #live-ad, #lj_ad_row, #load-adslargerect, #localAds, #logoAd, #logoAd2, #logo_ad, #long-ad, #long-ad-box, #long-ad-space, #long-bottom-ad-wrapper, #longAdSpace, #longAdWrap, #long_advert_header, #long_advertisement, #lower-ad-banner, #lower-advertising, #lowerAdvertisement, #lowerAdvertisementImg, #lower_ad, #lowerads, #lowerthirdad, #lowertop-adverts, #lowertop-adverts-container, #lpAdPanel, #lrec_ad, #lrecad, #lsadvert-left_menu_1, #lsadvert-left_menu_2, #lsadvert-top, #mBannerAd, #m_top_adblock, #madison_ad_248_100, #madskills-ad-manager-0, #madskills-ad-manager-1, #madskills-ad-manager-2, #madskills-ad-manager-3, #magnify_player_continuous_ad, #main-ad, #main-ad160x600, #main-ad160x600-img, #main-ad728x90, #main-advert, #main-advert1, #main-advert2, #main-advert3, #main-bottom-ad, #main-bottom-ad-tray, #main-content-ad1, #main-content-adcontent1, #main-header-ad-wrap, #main-header-ad-wrap-home, #main-header-advertisement, #main-middle-ad, #main-right-ad-tray, #main-tj-ad, #mainAd, #mainAd1, #mainAdUnit, #mainAdvert, #mainAdvertismentP, #mainHeaderAdvertisment, #mainMenu_divTopAd, #mainPageAds, #mainPlaceHolder_coreContentPlaceHolder_rightColumnAdvert_divControl, #main_AD, #main_ad, #main_ads, #main_content_ad, #main_left_side_ads, #main_rec_ad, #main_right_side_ads, #main_right_side_ads_130_01, #main_top_ad, #main_top_ad_container, #major_ad, #maker-rect-ad, #mapAdvert, #marcoad, #marketing-promo, #marketplace-ad-1, #marketplace-ad-2, #marketplaceAds, #marquee_ad, #masSearchAd, #mason_adv_bp_1, #mason_adv_bp_2, #mason_adv_bp_3, #mason_adv_bp_4, #mason_adv_rn_2, #mastAd, #mastAdvert, #mast_ad_wrap, #mast_ad_wrap_btm, #mast_logo_advertisement, #mastad, #masterTopAds, #masterad, #mastercardAd, #masthead-ad, #masthead_ad, #masthead_ads_container, #masthead_topad, #matchFooterAd, #mbbs-ad-in-content-shortcode, #mc_ad, #md-sidebar-video-companion-ad-loaded, #md_adLoader, #md_topad, #me-adspace-002, #med-rect-ad, #med-rectangle-ad, #medRecAd, #medReqAd, #media-ad, #media-ad-thumbs, #media-temple-ad, #mediaAdLeaderboard, #media_ad, #mediaget_box, #mediagoogleadsense, #mediaplayer_adburner, #medium-ad, #medium-rectangle-ad1, #mediumAd1, #mediumAdContainer, #mediumAdvertisement, #mediumRectangleAd, #mediumrectangle_300x250, #medrec_bottom_ad, #medrec_middle_ad, #medrec_top_ad, #medrectad, #medrectangle_banner, #mee-ad-wrapper, #memberad, #mens-journal-feature-ad, #menu-ads, #menuAds, #menuad, #menubanner-ad-content, #mgid-container, #mhheader_ad, #mi_story_assets_ad, #microAdDiv, #microsoft_ad, #mid-ad300x250, #mid-table-ad, #midAD, #midRightAds, #midRightTextAds, #mid_ad_div, #mid_ad_title, #mid_left_ads, #mid_mpu, #mid_roll_ad_holder, #midadd, #midadspace, #midadvert, #midbarad, #midbnrad, #midcolumn_ad, #middle-ad, #middle-ad-destin, #middle-story-ad-container, #middleRightColumnAdvert, #middle_ad, #middle_ads, #middle_bannerad, #middle_bannerad_section, #middle_body_advertising, #middle_mpu, #middle_sponsor_ads, #middlead, #middleads, #middleads2, #midpost_ad, #midrect_ad, #midstrip_ad, #mini-ad, #mini-panel-dart_stamp_ads, #mini-panel-dfp_stamp_ads, #mini-panel-top_ads, #mini-panel-two_column_ads, #miniAdsAd, #mini_ads_inset, #mn_ads, #moa-ads-long, #mobileAd_holder, #mobile_ad_spot_header, #mochila-column-right-ad-300x250, #mochila-column-right-ad-300x250-1, #mod-partner-center, #mod_ad, #mod_ad_top, #modal-ad, #modal_videoAd_wrapper, #module-ad-300x250, #module-ad-728x90, #module-google_ads, #module_ad, #module_box_ad, #module_sky_scraper, #monsterAd, #moogleAd, #more_ad, #moreads, #morefooterads, #mos-adCarouselContainer, #mosBannerAd, #mosTileAds, #most_popular_ad, #motionAd, #movads10, #movieads, #mozo-ad, #mph-rightad, #mpl_adv_text, #mpr-ad-leader, #mpr-ad-wrapper-1, #mpr-ad-wrapper-2, #mpu-ad, #mpu-advert, #mpu-cont, #mpu-content, #mpu-sidebar, #mpu2, #mpu2_container, #mpu300250, #mpuAd, #mpuAdvert, #mpuContainer, #mpuDiv, #mpuInContent, #mpuSecondary, #mpuSlot, #mpuWrapper, #mpuWrapper600, #mpuWrapperAd, #mpuWrapperAd2, #mpu_300x250, #mpu_ad, #mpu_ad2, #mpu_adv, #mpu_banner, #mpu_box, #mpu_container, #mpu_div, #mpu_firstpost, #mpu_holder, #mpu_text_ad, #mpuad, #mpubox, #mpuholder, #mpuholder01, #mpusLeftAd, #mr_banner_topad, #mrec-advertisement, #mrecAdContainer, #mrecPlacement, #mrt-node-tgtm-Col2-4-ComboAd, #msAds, #ms_ad, #msad, #msnAds_inner, #msn_header_ad, #msnau_ad_medium_rectangle, #mtSponsor, #mt_adv, #mts_ad_widget, #mu_2_ad, #multiLinkAdContainer, #multi_ad, #multibar-ads, #mvp_160_ad, #my-ads, #my-adsFPAD, #my-adsFPL, #my-adsFPT, #my-adsLREC, #my-adsLREC2, #my-adsLREC4-base, #my-adsMAST, #my-medium-rectangle-ad-1-container, #my-medium-rectangle-ad-2-container, #myAd, #myElementAd, #myads_HeaderButton, #mydfpad, #n_sponsor_ads, #na_adblock, #name-advert, #namecom_ad_hosting_main, #narrow-ad, #narrow_ad_unit, #nat-ad-300x250, #natadad300x250, #nationalAd_secondary_btm, #nationalAd_secondary_top, #national_ad, #national_microlink_ads, #nationalad, #native_ad2, #nativeadsteaser, #navAdBanner, #nav_ad, #nav_ad_728_mid, #navads-container, #navbar_ads, #navi_banner_ad_780, #navigation-ad, #nba160PromoAd, #nba300Ad, #nbaGI300ad, #nbaHeaderAds, #nbaHouseAnd600Ad, #nbaLeft600Ad, #nbaMidAds, #nbaVid300Ad, #nbabot728ad, #nbcAd300x250, #nbcShowcaseAds, #nc-header-ads, #netBoard-ad, #network_header_ad_1, #new-ad-footer, #new-ad-leaderboard, #new-ad-sidebottom, #new-ad-sidetop, #newAd, #newPostProfileAd, #newPostProfileVerticalAd, #newTopAds, #new_ad_728_90, #new_ad_header, #new_topad, #newadmpu, #newads, #news-adocs, #news_advertorial_content, #news_advertorial_top, #news_article_ad_mrec, #news_article_ad_mrec_right, #news_left_ad, #news_right_ad, #newstream_first_ad, #newuser_ad, #ng_rtcol_ad, #nib-ad, #nlrightsponsorad, #noresults_ad_container, #noresultsads, #northad, #northbanner-advert, #northbanner-advert-container, #notify_ad, #np_content_ads_module, #nrAds, #nrcAd_Top, #ns_ad1, #ns_ad2, #ns_ad3, #ntvAdZone, #ntvads, #nuevo_ad, #oanda_ads, #oas_Middle, #oas_Middle1, #oas_Right, #oas_Right1, #oas_Right2, #oas_Top, #oas_Top1, #oas_asponsor, #oas_wide_skyscraper, #ob_sponsoredcontent, #oba_message, #objadscript, #oem_ad, #ofie_ad, #omnibar_ad, #onespot-ads, #online_ad, #onpageads, #onpageadstext, #onscroll-ad-holder-mpu2, #openx-slc, #openx-text-ad, #openx-widget, #openx_iframe, #osDirAd2Post, #osads_300, #outbrain-paid, #outbrainAdWrapper, #outbrain_dual_ad_fs_0_dual, #outbrain_vertical, #outerAd300, #outerTwrAd, #outer_div_top_ad, #outsideAds, #ovAd, #ovAdWrap, #ovadsense, #overlay_ad, #overlayadd, #overtureSponsoredLinks, #p-advert, #p-googlead, #p-googleadsense, #p-googleadsense-portletlabel, #p2HeaderAd, #p2squaread, #p360_ad_unit, #p_lt_zoneContent_SubContent_p_lt_zoneRight_IFrameAd_panelAd, #page-ad-container-TopLeft, #page-ad-top, #page-advert-3rdrail, #page-advertising, #page-header-ad, #page-top-ad, #pageAdDiv, #pageAdds, #pageAds, #pageAdsDiv, #pageAdvert, #pageBannerAd, #pageLeftAd, #pageOwnershipAd_side, #pageRightAd, #page_ad, #page_ad_top, #page_content_top_ad, #page_top_ad, #pageads_top, #pagebottomAd, #pagelet_adbox, #pagelet_netego_ads, #pagelet_search_ads2, #pagelet_side_ads, #pagination-advert, #paidlistingAds, #panel-ad, #panelAd, #panoAdBlock, #parade_300ad, #parade_300ad2, #partner-ad, #partnerAd, #partnerMedRec, #partnerSitesBannerAd, #partner_ads, #pause-ad, #pauseAd, #pb_adbanner, #pb_report_ad, #pcworldAdBottom, #pcworldAdTop, #pencil-ad, #pencil-ad-container, #perm_ad, #permads, #persistentAd, #pf-dialog-ads, #pg-ad-160x600, #pg-ad-item-160x600, #pgAdWrapper, #pgFooterAd, #pgHeaderAd, #pgSquareAd, #pgad_Bottom3, #photoAdvert, #photoAndAdBox, #photo_ad_google, #picad_div, #pinball_ad, #pixAd, #plAds, #player-advert, #player-advertising, #player-below-advert, #player-midrollAd, #playerAd, #playerAdsRight, #player_ad, #player_ads, #player_middle_ad, #player_top_ad, #playerad, #playvideotopad, #pmad-in1, #pnAd2, #pnlADS, #pnlRedesignAdvert, #pnl_BannerAdServed, #pod-ad-video-page, #pof_ads_Wrapper, #pop_ad, #popadwrap, #popback-ad, #popoverAd, #popular-column-ad, #populate_ad_bottom, #populate_ad_left, #populate_ad_textupper, #populate_ad_textupper_textlink, #popupAd, #popupBottomAd, #popup_domination_lightbox_wrapper, #popupadunit, #portlet-advertisement-left, #portlet-advertisement-right, #pos_ContentAd2, #post-ad, #post-ad-hd, #post-ad-layer, #post-ads, #post-adsense-top-banner, #post-bottom-ads, #post-page-ad, #post-promo-ad, #post5_adbox, #postAd, #postNavigationAd, #post_ad, #post_addsense, #post_adsense, #post_adspace, #post_advert, #post_id_ad_bot, #postpageaddiv, #ppcAdverts, #pr_ad, #pr_advertising, #pre-adv, #pre-footer-ad, #pre_advertising_wrapper, #pregame_header_ad, #premSpons, #premier-ad-space, #preminumAD, #premiumAdTop, #premium_ad, #premium_ad_inside, #premiumad, #premiumads, #premiumsponsorbox, #prerollAd, #preroll_compainion_ad, #priceGrabberAd, #primary_mpu_placeholder, #prime-ad-space, #print-advertisement, #print-header-ad, #print_ads, #printads, #privateadbox, #privateads, #pro_ads_custom_widgets-2, #pro_ads_custom_widgets-3, #pro_ads_custom_widgets-5, #pro_ads_custom_widgets-7, #pro_ads_custom_widgets-8, #product-adsense, #profileAdHeader, #proj-bottom-ad, #promo-ad, #promoAds, #promoFloatAd, #promo_ads, #ps-ad-iframe, #ps-top-ads-sponsored, #ps-vertical-ads, #psmpopup, #pswp_advert, #pub-right-bottom-ads, #pub-right-top-ads, #pub468x60, #publicGoogleAd, #publicidad, #publicidad-video, #publicidad_120, #publicidadeLREC, #pulse360_1, #pushAd, #pushDownAd, #pushdown-ad, #pushdownAdWrapper, #pushdown_ad, #pusher-ad, #pvadscontainer, #qaSideAd, #qadserve_728x90_StayOn_div, #qm-ad-big-box, #qm-ad-sky, #qm-dvdad, #qpon_big_ad-teaser, #qtopAd-graybg, #quads-ad2, #quads-ad2_widget, #quads-ad4, #quick_ads_frame_bottom, #quidgetad, #quigo, #quigo-ad, #quigo_ad, #quinAdLeaderboard, #r-ad-tag, #r-ads-listings, #r-ads-preview-top, #r1SoftAd, #r_ad3_ad, #r_adver, #radioProfileAds, #rafael_side_ads_widget-5, #rail-ad-wrap, #rail-bottom-ad, #railAd, #rail_ad, #rail_ad1, #rail_ad2, #rbAdWrapperRt, #rbAdWrapperTop, #rc_edu_span5AdDiv, #rd_banner_ad, #reader-ad-container, #realEstateAds, #rearad, #recommendedAdContainer, #rect-ad, #rectAd, #rect_ad, #rectad, #rectangle-ad, #rectangleAd, #rectangleAdSpace, #rectangleAdTeaser1, #rectangle_ad, #rectangle_ad_smallgame, #redirect-ad, #redirect-ad-modal, #redirect_ad_1_div, #redirect_ad_2_div, #reference-ad, #refine-300-ad, #refine-ad, #refreshable_ad5, #region-node-advert, #region-regions-ad-top, #region-top-ad, #reklam-728x90, #reklama, #reklama_big, #reklama_left_body, #reklama_left_up, #reklama_right_up, #related-ads, #related-projects-sponsor, #related_ad, #related_ads, #related_ads_box, #relatedvideosads2, #relocation_ad_container, #remove_ads_button1, #remove_ads_button2, #removeadlink, #responsive-ad, #resultSponLinks, #resultsAdsBottom, #resultsAdsSB, #resultsAdsTop, #rg_right_ad, #rh-ad, #rh-ad-container, #rh_tower_ad, #rhapsodyAd, #rhc_ads, #rhsBottomAd, #rhs_ads, #rhs_adverts, #rhsads, #rhsadvert, #richad, #right-ad, #right-ad-1, #right-ad-block, #right-ad-col, #right-ad-skin, #right-ad-title, #right-ad1, #right-adds, #right-ads, #right-ads-3, #right-ads-4, #right-advert, #right-bar-ad, #right-box-ad, #right-col-ad-600, #right-featured-ad, #right-mpu-1-ad-container, #right-uppder-adverts, #right-uppder-adverts-container, #right1-ad, #right160x600ads_part, #right2Ad_Iframe, #rightAD, #rightAd, #rightAd1, #rightAd160x600, #rightAd160x600two, #rightAd300x250, #rightAd300x250Lower, #rightAdBar, #rightAdColumn, #rightAdContainer, #rightAdDiv1, #rightAdDiv2, #rightAdDiv3, #rightAdHideLinkContainer, #rightAdHolder, #rightAd_Iframe, #rightAd_rdr, #rightAds, #rightAdsDiv, #rightBanner-ad, #rightBlockAd, #rightBottomAd, #rightBoxAdvertisement, #rightBoxAdvertisementLast, #rightColAd, #rightColumnAds, #rightColumnMpuAd, #rightColumnSkyAd, #rightDoubleClick, #rightMortgageAd, #rightSideAd, #rightSideAdvert, #rightSideSquareAdverts, #right_Ads2, #right_ad, #right_ad_2, #right_ad_box, #right_ad_container, #right_ad_top, #right_ad_wrapper, #right_ads, #right_ads_box, #right_adsense, #right_adv1-v2, #right_advert, #right_advertisement, #right_advertising, #right_adverts, #right_bg_ad, #right_block_ads, #right_column_ad, #right_column_ad_container, #right_column_ads, #right_column_adverts, #right_column_internal_ad_container, #right_column_top_ad_unit, #right_gallery_ad, #right_global_adspace, #right_mini_ad, #right_panel_ads, #right_player_ad, #right_rail_ad_header, #right_side_bar_ami_ad, #right_sidebar_ads, #right_top_ad, #right_top_gad, #rightad, #rightad1, #rightad2, #rightadBorder, #rightadBorder1, #rightadBorder2, #rightadContainer, #rightadcell, #rightadd300, #rightadg, #rightadhome, #rightadpat, #rightads, #rightadsarea, #rightadvertbar-doubleclickads, #rightbar-ad, #rightbar_ad, #rightcol_mgid, #rightcol_sponsorad, #rightcolhouseads, #rightcollongad, #rightcolumn_300x250ad, #rightcolumn_ad_gam, #rightforumad, #rightgoogleads, #rightinfoad, #rightrail-ad, #rightrail-ad-1, #rightrail_ad-0, #rightside-ads, #rightside_ad, #rightskyad, #righttop-adverts, #righttop-adverts-container, #ringtone-ad-bottom, #ringtone-ad-top, #rm_ad_text, #rmx-ad-cta-box, #roadsheet-advertising, #rockmelt-ad-top, #rolldown-ad, #ros_ad, #rotate_textads_1, #rotating-ad-display, #rotating-ads-wrap, #rotating_ad, #rotatingads, #row-ad, #row2AdContainer, #rowAdv, #rprightHeaderAd, #rpuAdUnit-0, #rrAdWrapper, #rr_MSads, #rr_ad, #rr_gallery_ad, #rside_ad, #rside_adbox, #rt-ad, #rt-ad-top, #rt-ad468, #rtAdvertisement, #rtMod_ad, #rt_side_top_google_ad, #rtcol_advert_1, #rtcol_advert_2, #rtm_div_562, #rtm_html_226, #rtm_html_920, #rtmm_right_ad, #rtmod_ad, #rtn_ad_160x600, #rubicsTextAd, #rxgcontent, #rxgfooter, #rxgheader, #rxgleftbar, #rxgrightbar, #sAdsBox, #s_ads_header, #say-center-contentad, #sb-ad-sq, #sb_ad_links, #sb_advert, #sbads-top, #scoreAD, #script_ad_0, #scroll-ad, #scroll_ad, #scroll_banner_ad, #scrollingads, #sct_side_ads, #sdac_bottom_ad_widget-3, #sdac_footer_ads_widget-3, #sdac_skyscraper_ad_widget-3, #sdac_top_ad_widget-3, #search-ad, #search-ads1, #search-google-ads, #search-sponsor, #search-sponsored-links, #search-sponsored-links-top, #searchAd, #searchAdFrame, #searchAdSenseBox, #searchAdSenseBoxAd, #searchAdSkyscraperBox, #searchAds, #searchGoogleAdBottom, #searchPaneGoogleAd, #search_ad, #search_ads, #search_result_ad, #searchresult_advert_right, #searchsponsor, #sec_adspace, #second-adframe, #second-adlayer, #second-right-ad-tray, #second-story-ad, #secondBoxAd, #secondBoxAdContainer, #second_ad_div, #secondad, #secondary_ad_inventory, #secondaryad, #secondrowads, #sect-ad-300x100, #sect-ad-300x250, #sect-ad-300x250-2, #section-ad, #section-ad-1-728, #section-ad-300-250, #section-ad-4-160, #section-ad-bottom, #section-blog-ad, #section-container-ddc_ads, #section-footer-ribbonad, #section-pagetop-ad, #section-sub-ad, #section_ad, #section_advertisements, #section_advertorial_feature, #sector-widget__tiny-ad, #self-ad, #self_serve_ads, #sensis_island_ad_1, #sensis_island_ad_1_column, #sensis_island_ad_2, #sensis_island_ad_2_column, #sensis_island_ad_3, #sensis_island_ad_3_column, #serveAd1, #serveAd2, #serveAd3, #servfail-ads, #sew-ad1, #sew_advertbody, #sgAdHeader, #sgAdScGp160x600, #shellnavAd, #shoppingads, #shortads, #shortnews_advert, #show-ad, #show-player-right-ad, #showAd, #show_ads, #showads, #showcaseAd, #sic_superBannerAd-loader, #sic_superBannerAdTop, #side-ad, #side-ad-container, #side-ads, #side-ads-box, #side-banner-ad, #side-big-ad-bottom, #side-big-ad-middle, #side-boxad, #side-content-ad-1, #side-content-ad-2, #side-halfpage-ad, #side-skyscraper-ad, #sideABlock, #sideABlockHeader, #sideAD, #sideAd, #sideAd1, #sideAd2, #sideAdArea, #sideAdLarge, #sideAdSmall, #sideAdSub, #sideAds, #sideAdsBis, #sideBannerAd, #sideBar-ads, #sideBarAd, #sideBySideAds, #sideSponsors, #side_ad, #side_ad_call, #side_ad_container_A, #side_ad_module, #side_ad_wrapper, #side_ads, #side_ads_by_google, #side_adv_2, #side_adverts, #side_longads, #side_sky_ad, #side_skyscraper_ad, #side_sponsors, #sidead, #sidead1, #sidead1mask, #sideadbox, #sideads, #sideads_container, #sideadscol, #sideadtop-to, #sideadvert, #sideadzone, #sidebar-125x125-ads, #sidebar-125x125-ads-below-index, #sidebar-ad, #sidebar-ad-300, #sidebar-ad-block, #sidebar-ad-boxes, #sidebar-ad-holdd, #sidebar-ad-holdd-middle, #sidebar-ad-loader, #sidebar-ad-middle, #sidebar-ad-space, #sidebar-ad-wrap, #sidebar-ad1, #sidebar-ad2, #sidebar-ad3, #sidebar-ad_dbl, #sidebar-ads, #sidebar-ads-content, #sidebar-ads-narrow, #sidebar-ads-wide, #sidebar-ads-wrapper, #sidebar-adspace, #sidebar-adv, #sidebar-advertise-text, #sidebar-advertisement, #sidebar-banner300, #sidebar-corner-ad, #sidebar-feed-ad, #sidebar-left-ad, #sidebar-long-advertise, #sidebar-main-ad, #sidebar-post-120x120-banner, #sidebar-post-300x250-banner, #sidebar-scroll-ad-container, #sidebar-sponsor-link, #sidebar-sponsors, #sidebar-top-ad, #sidebar-top-ads, #sidebar2-ads, #sidebar2ads, #sidebarAd, #sidebarAd1, #sidebarAd2, #sidebarAdSense, #sidebarAdSpace, #sidebarAdUnitWidget, #sidebarAds, #sidebarAdvert, #sidebarSponsors, #sidebarTextAds, #sidebarTowerAds, #sidebar_ad, #sidebar_ad_1, #sidebar_ad_2, #sidebar_ad_3, #sidebar_ad_adam, #sidebar_ad_container, #sidebar_ad_top, #sidebar_ad_widget, #sidebar_ad_wrapper, #sidebar_adblock, #sidebar_ads, #sidebar_ads_180, #sidebar_box_add, #sidebar_mini_ads, #sidebar_sponsoredresult_body, #sidebar_topad, #sidebar_txt_ad_links, #sidebarad, #sidebarad_300x600-33, #sidebarad_300x600-4, #sidebaradpane, #sidebaradsense, #sidebaradver_advertistxt, #sidebaradverts, #sidebard-ads-wrapper, #sidebargooglead, #sidebargoogleads, #sidebarrectad, #sideline-ad, #sidepad-ad, #simple_ads_manager_ad_widget-2, #simple_ads_manager_widget-3, #simple_ads_manager_widget-4, #simplyhired_job_widget, #single-ad, #single-ad-2, #single-adblade, #single-mpu, #singleAd, #singleAdsContainer, #single_ad_above_content, #singlead, #site-ad-container, #site-ads, #site-header__ads, #site-leaderboard-ads, #site-sponsor-ad, #site-sponsors, #siteAdHeader, #site_body_header_banner_ad, #site_bottom_ad_div, #site_content_ad_div, #site_top_ad, #sitead, #sitemap_ad_left, #skcolAdSky, #skin-ad, #skinTopAd, #skin_ADV_DIV, #skin_adv, #skinad-left, #skinad-right, #skinmid-ad, #skinmid-ad_iframe, #skinningads, #sky-ad, #sky-ads, #sky-left, #sky-right, #sky-top-ad, #skyAd, #skyAdContainer, #skyAdNewsletter, #skyScraperAd, #skyScrapperAd, #skyWrapperAds, #sky_ad, #sky_advert, #skyads, #skyadwrap, #skybox-ad, #skyline_ad, #skyscrapeAd, #skyscraper-ad, #skyscraper-ad-1, #skyscraper-ad-2, #skyscraperAd, #skyscraperAdContainer, #skyscraperAdWrap, #skyscraperAds, #skyscraperWrapperAd, #skyscraper_ad, #skyscraper_advert, #skyscraperadblock, #skyscrapper-ad, #slide_ad, #slidead, #slideboxad, #slider-ad, #sliderAdHolder, #slider_ad, #slideshow-middle-ad, #slideshowAd, #slideshow_ad_300x250, #sm-banner-ad, #smallAd, #smallBannerAdboard, #small_ad, #small_ad_banners_vertical, #small_ads, #smallad, #smallads, #smallerAd, #smoozed-ad, #smxTextAd, #socialAD, #socialBarAd, #socialBarAdMini, #some-ads, #some-ads-holder, #some-more-ads, #sortsite1-bottom-ad, #source_ad, #source_content_ad, #spec_offer_ad2, #special-deals-ad, #specialAd_one, #specialAd_two, #special_ads, #specialadfeatures, #specialadvertisingreport_container, #specials_ads, #speed_ads, #speeds_ads, #speeds_ads_fstitem, #speedtest_mrec_ad, #sphereAd, #sphereAd-wrap, #spl_ad, #spnAds, #spnslink, #sponBox, #sponLinkDiv_1, #sponLinkDiv_2, #spon_links, #sponlink, #sponlinks, #sponsAds, #sponsLinks, #spons_links, #sponseredlinks, #sponsor-flyout-wrap, #sponsor-links, #sponsor-sidebar-container, #sponsorAd, #sponsorAd1, #sponsorAd2, #sponsorAdDiv, #sponsorBanners32, #sponsorBar, #sponsorBorder, #sponsorContainer0, #sponsorFooter, #sponsorLinkDiv, #sponsorLinks, #sponsorResults, #sponsorSpot, #sponsorTab, #sponsorText, #sponsorTextLink, #sponsor_300x250, #sponsor_ad, #sponsor_ads, #sponsor_banderole, #sponsor_bar, #sponsor_bottom, #sponsor_box, #sponsor_deals, #sponsor_div, #sponsor_footer, #sponsor_header, #sponsor_link, #sponsor_no, #sponsor_partner_single, #sponsor_posts, #sponsor_right, #sponsored-bucket, #sponsored-features, #sponsored-inline, #sponsored-links, #sponsored-links-container, #sponsored-links-list, #sponsored-links-media-ads, #sponsored-listings, #sponsored-message, #sponsored-not, #sponsored-products-dp_feature_div, #sponsored-recommendations, #sponsored-resources, #sponsored-text-links, #sponsored-widget, #sponsored1, #sponsoredAdvertisement, #sponsoredBottom, #sponsoredBox1, #sponsoredBox2, #sponsoredFeaturedHoz, #sponsoredHoz, #sponsoredLinks, #sponsoredLinksBox, #sponsoredLinks_Bottom, #sponsoredLinks_Top, #sponsoredList, #sponsoredResults, #sponsoredResultsWide, #sponsoredSiteMainline, #sponsoredSiteSidebar, #sponsoredTop, #sponsoredWd, #sponsored_ads, #sponsored_ads_v4, #sponsored_container, #sponsored_content, #sponsored_game_row_listing, #sponsored_head, #sponsored_label, #sponsored_link, #sponsored_link_bottom, #sponsored_links, #sponsored_native_ad, #sponsored_news, #sponsored_option, #sponsored_v12, #sponsoredads, #sponsoredlinks, #sponsoredlinks_cntr, #sponsoredlinks_left_wrapper, #sponsoredlinkslabel, #sponsoredresultsBottom_body, #sponsoredresults_top, #sponsoredwellcontainerbottom, #sponsoredwellcontainertop, #sponsorlink, #sponsors-block, #sponsors-home, #sponsorsBox, #sponsorsContainer, #sponsors_right_container, #sponsors_top_container, #sponsorsads1, #sponsorsads2, #sponsorship-box, #sponsorshipBadge, #sporsored-results, #sports_only_ads, #spotadvert, #spotadvert1, #spotadvert2, #spotadvert3, #spotadvert5, #spotlight-ad-container-block, #spotlight-ad_iframe, #spotlight-ads, #spotlightAds, #spotlight_ad, #spotlightad, #spr_ad_bg, #spreadly-advertisement-container, #sprint_ad, #sqAd, #sq_ads, #square-ad, #square-ad-box, #square-ad-slider-wrapper, #square-ad-space, #square-ad-space_btm, #square-ads, #square-sponsors, #squareAd, #squareAdBottom, #squareAdSpace, #squareAdTop, #squareAdWrap, #squareAds, #squareGoogleAd, #square_ad, #square_lat_adv, #squaread, #squareadAdvertiseHere, #squareadvert, #squared_ad, #srp_adsense-top, #ss-ad-container, #ss-ad-overlay, #ss-ads-container, #st_topads, #stageAds, #starad, #start_middle_container_advertisment, #static_textads_1, #stationad, #sticky-ad, #sticky-ad-container, #sticky-top-ad-spacer, #sticky-top-ad-wrap, #stickyAdBlock, #stickyBottomAd, #stickySkyAd, #sticky_adv_container, #stickyad, #stickyads, #stickyleftad, #stickyrightad, #stopAdv, #stopAdvt, #story-90-728-area, #story-ad, #story-ad-a, #story-ad-b, #story-ad-top, #story-ad-wrap, #story-leaderboard-ad, #story-page-leaderboard-ad, #story-sponsoredlinks, #storyAd, #storyAdWrap, #story_ad, #story_ads, #story_main_mpu, #story_unseen_ad, #storyad2, #storyblock-ad, #stripadv, #style_ad_bottom, #subAdsFooter, #subbgad, #subheaderAd, #submenu-ads, #subpage-ad-right, #subpage-ad-top, #subpageAd, #subpage_234x60ad, #sugarad-stitial-overlay, #super_ad, #svp-ad, #swads, #sway-banner-ad, #sway-banner-ad-container, #sway-banner-ad1, #sweep_right_ad, #sweep_top_ad, #swfAd1, #swfAd5, #syn_headerad_zone, #synced-ad, #synch-ad, #systemad_background, #t7ad, #tabAdvertising, #table_ads, #taboola-ad, #taboola-adverts, #taboola-below, #taboola-below-article-thumbnails-3rd, #taboola-content, #taboola-footer-ad, #taboola-right-rail-stream-2nd, #taboola-right-rail-thumbnails-1st, #taboola_related, #tailResultAd, #takeover-ad, #takeover_ad, #takeoverad, #targetWeeklyAd, #targetWeeklyAdLogo, #targeted-ads, #tblAd, #tblReklama2, #tbl_googlead, #tbo_headerads, #tcwAd, #td-GblHdrAds, #td-applet-ads_2_container, #td-applet-ads_container, #tdAds, #tdBannerTopAds, #tdGoogleAds, #td_adunit1, #td_adunit1_wrapper, #td_adunit2, #td_sponsorAd, #teaser-adtag-left, #teaser-adtag-right, #temp-ads, #template_ad_leaderboard, #template_affiliates, #tertiary_advertising, #test_adunit_160_article, #text-ad, #text-ads, #text-link-ads, #text-linkAD, #textAd, #textAd1, #textAds, #textAdsTop, #text_ad, #text_ads, #text_advert, #textad, #textad3, #textad_block, #textads_right_container, #textlink-advertisement, #textlink_ads_placeholder, #textsponsor, #tf_page_ad_content_bottom, #tgAD_imu_2, #tgAD_imu_3, #tgAD_imu_4, #tgt1-Col2-0-ComboAd-Proxy, #tgt1-Col2-1-ComboAd-Proxy, #the-last-ad-standing, #theAd, #theadsADT3, #thefooterad, #thelistBottomAd, #themis-ads, #thheaderadcontainer, #third_party_ads, #thisisnotanad, #thistad, #thread-ad, #ti-sway-ad, #tile-ad, #tileAds, #tilia_ad, #tippytop-ad, #title-sponsor-banner, #title-wide-sponsored-by, #tmcomp_ad, #tmgAd_div_mpu_1, #tmglBannerAd, #tmn_ad_1, #tmn_ad_2, #tmn_ad_3, #tmp2_promo_ad, #tnt_ad_column, #toaster_ad, #tobsideAd, #today_ad_bottom, #toolbarSlideUpAd, #top-ad, #top-ad-970x250, #top-ad-banner, #top-ad-container, #top-ad-content, #top-ad-desktop, #top-ad-google, #top-ad-left-spot, #top-ad-menu, #top-ad-position-inner, #top-ad-rect, #top-ad-right-spot, #top-ad-unit, #top-ad-wrapper, #top-adblock, #top-adds, #top-ads, #top-ads-1, #top-ads-contain, #top-ads-tabs, #top-adspot, #top-advert, #top-advertisement, #top-advertisements, #top-banner-ad, #top-dfp, #top-leaderboard-ad, #top-left-ad, #top-middle-add, #top-right-ad, #top-search-ad-wrapper, #top-sidebar-ad-300x250, #top-sponsor-ad, #top-story-ad, #top100_ad300right, #top100_ad300rightbottom, #top2_ads, #top300x250ad, #top3_ads, #top728ad, #topAD, #topAd, #topAd300x250_, #topAd728x90, #topAdArea, #topAdBanner, #topAdBar, #topAdBox, #topAdContainer, #topAdDropdown, #topAdHolder, #topAdSenseDiv, #topAdShow, #topAdSpace, #topAdSpace_div, #topAdWrapper, #topAdcontainer, #topAds, #topAds1, #topAds2, #topAdsContainer, #topAdsDiv, #topAdsG, #topAdv, #topAdvBox, #topAdvert, #topAdvert-09, #topBanner-ad, #topBannerAd, #topBannerAdContainer, #topContentAdTeaser, #topImgAd, #topLBAd, #topLeaderAdAreaPageSkin, #topLeaderboardAd, #topMPU, #topMpuContainer, #topNavLeaderboardAdHolder, #topOpenXAdSlot, #topOverallAdArea, #topRightBlockAdSense, #topSponsoredLinks, #top_AD, #top_ad, #top_ad-sense, #top_ad_area, #top_ad_banner, #top_ad_block, #top_ad_box, #top_ad_container, #top_ad_game, #top_ad_inventory, #top_ad_parent, #top_ad_strip, #top_ad_td, #top_ad_unit, #top_ad_widget_area, #top_ad_wrapper, #top_ad_zone, #top_adblock_fix, #top_add, #top_ads, #top_ads_container, #top_ads_region, #top_ads_wrap, #top_adsense_cont, #top_adspace, #top_adv, #top_adv-v2, #top_adv_220, #top_adv_728, #top_advert, #top_advert_box, #top_advertise, #top_advertising, #top_container_ad, #top_content_ad_inner_container, #top_google_ad_container, #top_google_ads, #top_header_ad_wrapper, #top_mpu, #top_mpu_ad, #top_rectangle_ad, #top_right_ad, #top_span_ad, #top_sponsor_ads, #top_sponsor_text, #top_wide_ad, #topad, #topad-728x90, #topad-wrap, #topad1, #topad2, #topad728, #topad_holder, #topad_left, #topad_right, #topad_table, #topadbanner, #topadbanner2, #topadbar, #topadblock, #topadcell, #topadcontainer, #topaddwide, #topadh, #topadone, #topads-spacer, #topads-wrapper, #topadsblock, #topadsdiv, #topadsense, #topadspace, #topadvert, #topadvertisements, #topadvertisementwrapper, #topadwrap, #topadz, #topadzone, #topbanner_ad, #topbanner_sponsor, #topbannerad, #topbanneradtitle, #topbar-ad, #topbarAd, #topbar_Adc1_AdContainer, #topbarads, #topcustomad, #topheader_ads, #topicPageAdsense, #topleaderAd, #topleaderboardad, #topnav-ad-shell, #topnavad, #toppannonse, #topright-ad, #toprightAdvert, #toprightad, #toprow-ad, #topsidebar-ad, #topsponad, #topsponsorads, #topsponsored, #toptextad, #tour300Ad, #tour728Ad, #tourSponsoredLinksContainer, #tower1ad, #towerAdContainer, #towerad, #tr-ad, #tr-ad-mpu01, #tr-ad-mpu02, #tr-adv-banner, #trafficrevenue2, #transparentad, #travel_ad, #trc_google_ad, #trendex-sponsor-ad, #trib2-footer-ad-back, #trib2-leaderboard-ad-back, #tripleAdInner, #tripleAdOuter, #ts-ad_module, #tsad1, #tsad2, #ttp_ad_slot1, #ttp_ad_slot2, #tube_ad, #turnAD, #tut_ads, #tvd-ad-top, #twogamesAd, #txfPageMediaAdvertVideo, #txtAdcontainer2, #txtTextAd, #txt_link_ads, #txtads, #ucfooterad, #ugly-ad, #ui-about-these-ads-img, #ultraWideAdContainer, #underPlayerAd, #under_content_ad, #under_story_ad, #undergameAd, #universalAdContainer, #uploadMrecAd, #upper-ads, #upperAdvertisementImg, #upperMpu, #upperRightAds, #upper_adbox, #upper_advertising, #upper_small_ad, #upperad, #urban_contentad_1, #urban_contentad_2, #urban_contentad_article, #usa_ad_728x90, #usenetAdsTable, #uvp_ad_container, #uzcrsite, #vListAds, #v_ad, #vap_adsense-top, #variant_adsLazyLoad, #vc_side_ad, #vdiAd, #vdls-adv, #vdls-advs, #vert-ads, #vertAd2, #vert_ad, #vert_ad_placeholder, #vertad1, #verticalAds, #vertical_ad, #vertical_ads, #vhDivAdSlot300x250, #vid-left-ad, #vid-right-ad, #vidAdBottom, #vidAdRight, #vidAdTop, #video-ad, #video-ad-companion-rectangle, #video-adv, #video-adv-300, #video-adv-wrapper, #video-coverage-ad-300x250, #video-embed-ads, #video-header-advert, #video-in-player-ad, #video-in-player-ad-container, #video-under-player-ad, #videoAd, #videoAdvert, #videoCompanionAd, #videoPauseAd, #videoPlayerAdLayer, #video_ads_background, #video_ads_overdiv, #video_adv, #video_advert, #video_advert2, #video_advert3, #video_advert_top, #video_cnv_ad, #video_embed_ads, #video_hor_bottom_ads, #video_overlay_ad, #video_vert_right_ads, #videoadlogo, #videoads, #videopageadblock, #view-photo-ad, #viewAd1, #view_ads_bottom_bg, #view_ads_bottom_bg_middle, #view_ads_content_bg, #view_ads_top_bg, #view_ads_top_bg_middle, #view_adtop, #viewer-ad-bottom, #viewer-ad-top, #viewer_ads_wrapper, #viewportAds, #viewvid_ad300x250, #visual-ad, #votvAds_inner, #vsw-ads, #vsw_ad, #vuukle_ads_square2, #wTopAd, #wXcds12-ad, #wallAd, #wall_advert, #wallpaper-ad-link, #wallpaperAd_left, #wallpaperAd_left3, #wallpaperAd_right, #wallpaperAd_right2, #wallpaperAd_right2_1, #wallpaper_flash_ad, #wallpaper_header_ad, #walltopad, #watch-now-ad, #watch7-sidebar-ads, #watch_sponsored, #weather-ad, #weather_sponsor, #weatherad, #weblink_ads_container, #websearchAdvert, #welcomeAdsContainer, #welcome_ad, #welcome_ad_mrec, #welcome_advertisement, #wf_ContentAd, #wf_FrontSingleAd, #wf_SingleAd, #wf_bottomContentAd, #wg_ads, #wgtAd, #wh_ad_4, #whatsnews_footer_ad, #whatsnews_top_ad, #whitepaper-ad, #whoisRightAdContainer, #whoisRightAdContainerBottom, #whoisRightAdContainerTop, #wibiyaAdRotation, #wibiyaToolbarAdUnitFlash, #wide-ad, #wideAdd, #wide_ad_unit, #wide_ad_unit2, #wide_ad_unit_2, #wide_ad_unit_top, #wide_ad_unit_up, #wide_adv, #wide_right_ad, #wideskyscraper_160x600_left, #wideskyscraper_160x600_right, #widget-ads-3, #widget-ads-4, #widget-adv-12, #widget-box-ad-1, #widget-box-ad-2, #widget-style-ad, #widgetADT3, #widget_Adverts, #widget_ad, #widget_advertisement, #widget_thrive_ad_default-2, #widget_thrive_ad_default-4, #widgetwidget_adserve2, #wl-pencil-ad, #wog-300x250-ads, #wow-ads, #wp-insert-ad-widget-1, #wp-topAds, #wp125adwrap_2c, #wp_ad_marker, #wp_ads_gpt_widget-16, #wp_ads_gpt_widget-17, #wp_ads_gpt_widget-18, #wp_ads_gpt_widget-19, #wp_ads_gpt_widget-21, #wp_ads_gpt_widget-4, #wp_ads_gpt_widget-5, #wp_pro_ad_system_ad_zone, #wrapAd, #wrapAdRight, #wrapAdTop, #wrapCommentAd, #wrapperAdsTopLeft, #wrapperAdsTopRight, #wrapperRightAds, #wrapper_ad_Top, #wrapper_ad_island2, #wrapper_sponsoredlinks, #wsAdWrapper, #x-ad-item-themed-skyscraper-placekeeper, #x-houseads, #x01-ad, #x300_ad, #xColAds, #xadtop, #xlAd, #xybrad, #y-ad-units, #y708-ad-expedia, #y708-ad-lrec, #y708-ad-partners, #y708-ad-ysm, #y708-advertorial-competitions, #y708-advertorial-marketplace, #yahoo-ads, #yahoo-ads-content, #yahoo-sponsors, #yahooAdsBottom, #yahooSponsored, #yahoo_ad, #yahoo_ad_contanr, #yahoo_ads, #yahoo_sponsor_links, #yahoo_sponsor_links_title, #yahoo_text_ad, #yahooad-tbl, #yahooads, #yan-advert-north, #yan-advert-nt1, #yan-question-advert, #yan-sponsored, #yatadsky, #ybf-ads, #yfi-sponsor, #yfi_ads_4x4, #yfi_fp_ad_fx, #yfi_fp_ad_mort, #yfi_fp_ad_nns, #yfi_pf_ad_mort, #ygrp-sponsored-links, #yieldaddiv, #ylf-lrec, #ylf-lrec2, #ymap_adbanner, #yn-gmy-ad-lrec, #yom-ad-tbs-as, #ypaAdWrapper-BottomAds, #ypaAdWrapper-TopAds, #yrail_ads, #yreSponsoredLinks, #ysm_ad_iframe, #yt-adsfull-widget-2, #yt-adsfull-widget-3, #yw-sponsoredad, #zMSplacement1, #zMSplacement2, #zMSplacement3, #zMSplacement4, #zMSplacement5, #zMSplacement6, #zag_square_ad, #zoneAdserverMrec, #zoneAdserverSuper, #zoneAdvertisment, #zone_a_ad, #zone_b_ad, #zone_c_ads, #zztextad, .AD-POST, .AD-RC-300x250, .AD-Rotate, .AD-label300x250, .AD300, .AD300Block, .AD300x600-wrapper, .AD355125, .AD728, .ADBAR, .ADBnrArea, .ADBox, .ADCLOUD, .ADFooter, .ADITION, .ADInfo, .ADLeader, .ADMiddle1, .ADPod, .ADS-Content-Sidebar, .ADS-MainContent, .ADServer, .ADStyle, .ADTextSingle, .ADV-Space, .AD_2, .AD_300x100, .AD_300x250, .AD_300x265, .AD_302x252, .AD_ALBUM_ITEMLIST, .AD_MOVIE_ITEM { display: none !important; } </style><style type="text/css">.AD_MOVIE_ITEMLIST, .AD_MOVIE_ITEMROW, .AD_area, .AD_mid300, .AD_textinfo, .ADbox, .ADmid, .ADouter_div, .ADwidget, .A__smallSuperbannerAdvert-main, .Accordion_ad, .Ad--sidebar, .Ad-300x100, .Ad-Container, .Ad-Container-976x166, .Ad-Header, .Ad-IframeWrap, .Ad-MPU, .Ad-Wrapper-300x100, .Ad-label, .Ad120x600, .Ad160x600, .Ad160x600left, .Ad160x600right, .Ad247x90, .Ad300x, .Ad300x250, .Ad300x250L, .Ad300x250_top, .Ad728x90, .AdBar, .AdBorder, .AdBox, .AdBox160, .AdBox7, .AdBox728, .AdBoxStyle, .AdBoxStyleHome, .AdCaption, .AdCommercial, .AdContainer160x600, .AdContainerBottom, .AdContainerBox308, .AdContainerModule, .AdFrameLB, .AdGraph, .AdGrayBox, .AdHeader, .AdHere, .AdHolder, .AdIndicator, .AdInfo, .AdInjectContainer, .AdInline, .AdInline_left, .AdLeft1, .AdLeft2, .AdLeftbarBorderStyle, .AdMedium, .AdMessage, .AdModule, .AdModule_Content, .AdModule_ContentLarge, .AdModule_Hdr, .AdMultiPage, .AdPanel, .AdPlaceHolder, .AdProS728x90Container, .AdProduct, .AdRight1, .AdRight2, .AdRingtone, .AdScriptBox, .AdSectionHeader, .AdSense, .AdSenseLeft, .AdSense_Header, .AdSense_Sidebar, .AdSidebar, .AdSlot, .AdSlotHeader, .AdSlot__Commercial, .AdSpace, .AdTextSmallFont, .AdTitle, .AdTop, .AdUnit, .AdUnit300, .AdUnit300x250, .AdUnitBox, .AdWidget_ImageWidget, .AdZone120, .AdZone316, .Ad_120x600, .Ad_120x600_holder, .Ad_160x600_holder, .Ad_160x600_inner, .Ad_300x250, .Ad_300x250_holder, .Ad_468x60, .Ad_728x90, .Ad_728x90_holder, .Ad_C, .Ad_D, .Ad_D_Wrapper, .Ad_E_Wrapper, .Ad_Label, .Ad_Label_foursquare, .Ad_Right, .Ad_Tit, .Ad_container, .Adbuttons, .Adbuttons-sidebar, .AdnetBox, .Ads-768x90, .Ads2x1000, .AdsBottom, .AdsBottom336X280, .AdsBoxBottom, .AdsBoxSection, .AdsBoxTop, .AdsLeft_list, .AdsLinks1, .AdsLinks2, .AdsPlayRight_list, .AdsRec, .Ads_3, .Ads_4, .Ads_forum, .Adsense, .AdsenseBox, .AdsenseBoxCenter, .AdsenseDivFooter, .AdsenseDownload, .AdsenseForum, .AdsenseLarge, .AdsenseTechsupport, .Adspottop, .Adtext, .Adv300x250, .Adv300x250Box, .Adv468, .AdvBoxSidebar, .Adv_Left, .Advert300x250, .AdvertContainer, .AdvertMidPage, .AdvertiseWithUs, .Advertisehere2, .AdvertisementText, .AdvertisementTextTag, .AdvertisementTop, .Advertisment, .AdvertorialTeaser, .Advman_Widget, .Advrt, .Advrt_desktop, .AdvtNews, .AdvtSample, .AdvtSample2, .AdvtSample4, .AffAD, .AffiliateAds, .AmazonSimpleAdmin_widget, .ArticleAd, .ArticleInlineAd, .ArticleLeaderboard_ad, .BCA_Advertisement, .BGoogleAds300, .BOT-ADS, .Banner300x250, .Banner468X60, .BannerAD728, .BannerAd, .Banner_Group, .Banner_Group_Ad_Label, .BigBoxAd, .BigBoxAdLabel, .BlockAd, .BlueTxtAdvert, .BottomAdContainer, .BottomAffiliate, .BottomGoogleAds, .BoxAd, .BoxAdWrap, .BoxSponsorBottom, .BtmAd, .BtmSponsAd, .ButtonAd, .CG_adkit_leaderboard, .CG_details_ad_dropzone, .CWReviewsProdInfoAd, .Cheat__footer-ad-container, .Cheat__outbrain, .CollisionAdMarker, .ComAread, .CommentAd, .CommentGoogleAd, .ContentAd, .ContentAd2, .ContentAds, .DAWRadvertisement, .DartAdvert, .DeptAd, .DetachedAd, .DetailAds, .DisplayAd, .DomAdsDiv, .DoubleClickRefreshable, .EzAdsLUPro, .EzAdsSearchPro, .EzAdsWidget, .FT_Ad, .FeaturedAdIndexAd, .FlatAds, .FlowersAdContainer, .FooterAdContainer, .FooterAds, .FooterTileAdOuter_Div, .Footer_AD_Links_DIV, .Footer_Default_AD_Message_DIV, .GAME_Ad160x600, .GOOGLE_AD, .G_ads, .G_ads_m, .GalleryViewerAdSuppress, .GetRightAds, .GoogleAd, .GoogleAdInfo, .GoogleAdSencePanel, .GoogleAdSenseBottomModule, .GoogleAdSenseRightModule, .GoogleAdWords_container, .GoogleAdsBox, .GoogleAdsItem, .GoogleAdv, .Googleads728, .GreenHomeAd, .GridHouseAdRight, .HGLoneAdTitleFrame, .HPG_Ad_B, .HPNewAdsBannerDiv, .HPRoundedAd, .HeaderAd, .HeaderAds, .HeaderBannerAd, .HeaderLeaderAd, .HeadingAdSpace, .HomeAd1Label, .HomeAds, .HomeContentAd, .HomePageAD, .HomeSidebarAd, .Hotels-Results-InlineAd, .IABAdSpace, .IM_ad_unit, .InArticleAd, .IndexRightAd, .InternalAdPanel1, .JobListMidAd, .LL_Widget_Advertorial, .LN_Related_Posts_bottom_adv, .LargeOuterBoxAdsense, .LargeRightAd, .LastAd, .LazyLoadAd, .LeaderAd, .LeaderAdvertisement, .LeaderBoardAd, .LeaderboardAdTagWidget, .LeftAd, .LeftButtonAdSlot, .LeftTowerAd, .LeftWideSkyscraperAdPanel, .Left_Content_Google_Ad, .Ligatus, .Loge_AD, .LoungeAdsBottomLinks, .M2Advertisement, .MBoxAdM, .MBoxAdMain, .MBoxAdR, .MBoxAdRight, .MDCadSummary, .MD_adZone, .MOS-ad-hack, .MPUHolder, .MPUTitleWrapperClass, .MPUad, .MREC_ads, .M__leaderboardAdvert-image, .MadClose, .MainAdCont, .Main_right_Adv_incl, .MarketGid_container, .MasterLeftContentColumnThreeColumnAdLeft, .MbanAd, .MedRecAD-border, .MediumRectangleAdPanel, .MiddleAd, .MiddleAdContainer, .MiddleAdvert, .MiddleRightRadvertisement, .MspAd, .NAPmarketAdvert, .NGOLocalFooterAd, .NavBarAd, .NewsAds, .OAS_position_TopLeft, .OSOasAdModule, .OSProfileAdSenseModule, .OpaqueAdBanner, .OpenXad, .OuterAdvertisingContainer, .PERFORMANCE_AD_COMPLETE, .PERFORMANCE_AD_RELATED, .PU_DoubleClickAdsContent, .PencilAd, .Post5ad, .Post8ad, .Post9ad, .PostSidebarAd, .PremiumObitAdBar, .ProductAd, .PushDownAdPane, .PushdownAd, .RBboxAd, .RC-AD, .RGAdBoxMainDiv, .RHR-ADS, .RR_ad, .RW_ad300, .RectangleAd, .RelatedAds, .ResponsiveAd, .Right-Column-AD-Container, .Right300x250AD, .RightAd, .RightAd1, .RightAd2, .RightAdvertiseArea, .RightAdvertisement, .RightGoogleAFC, .RightGoogleAd, .RightRailAd, .RightRailAdbg, .RightRailAdtext, .RightRailTop300x250Ad, .RightSponsoredAdTitle, .RightTowerAd, .SIM_ad_140x140_homepage_tv_promo, .SRPads, .STR_AdBlock, .SecondaryAd, .SecondaryAdLink, .SectionSponsor, .ShootingAd, .ShootingAdLeft, .ShowAdDisplay, .SideAdCol, .SideAds, .SidebarAd, .SidebarAdvert, .SidebarMiddleAdContainer, .SidekickItem-Ads, .SimpleAcceptableTextAds, .SimpleAcceptebleTextAds, .SitesGoogleAdsModule, .Sitewide_AdLabel, .SkyAdContainer, .SkyAdContent, .SkyScraperAd, .SkyscraperAD-border, .SmartAdZoneList, .Sponsor-container, .SponsorAds, .SponsorHeader, .SponsorIsland, .SponsorLink, .SponsoredAdTitle, .SponsoredArticleAd, .SponsoredContent, .SponsoredLinkItemTD, .SponsoredLinks, .SponsoredLinksGrayBox, .SponsoredLinksModule, .SponsoredLinksPadding, .SponsoredLinksPanel, .SponsoredResults, .Sponsored_link, .SponsorshipText, .SquareAd, .Squareadspot, .StandardAdLeft, .StandardAdRight, .TOP-ADS, .TRADING_AD_RELATED, .TRU-onsite-ads-leaderboard, .TTButtAd, .Tadspacemrec, .TextAd, .TextAdds, .TheEagleGoogleAdSense300x250, .ThreeAds, .TimelineAd, .TmnAdsense, .TopAd, .TopAdContainer, .TopAdL, .TopAdR, .TopAds, .TopBannerAd, .TopLeaderboardAdPanel, .TopRightRadvertisement, .Top_Ad, .TrafficAd, .UFSquareAd, .UIStandardFrame_SidebarAds, .UIWashFrame_SidebarAds, .UnderAd, .UpperAdsContainer, .VerticalAd, .Video-Ad, .VideoAd, .WPBannerizeWidget, .WP_Widget_Ad_manager, .WideAdContainer, .WideAdTile, .WideAdsLeft, .WidgetAdvertiser, .WiredWidgetsDartAds, .WiredWidgetsGoogleAds, .WithAds, .XEad, .YEN_Ads_120, .YEN_Ads_125, .ZventsSponsoredLabel, .ZventsSponsoredList, .a-ad, .a-d-container, .a160x600, .a300x250, .a468x60, .a728x90, .aa_AdAnnouncement, .aa_ad-160x600, .aa_ad-728x15, .aa_sb_ad_300x250, .aadsection_b1, .aadsection_b2, .ab-prompt, .abAdArea, .abAdPositionBoxB, .abBoxAd, .ablock300, .ablock468, .ablock728, .about_adsense, .above-header-advert, .aboveCommentAdBladeWrapper, .aboveCommentAds, .aboveCommentAdsWrapper, .above_discussion_ad, .above_miniscore_ad, .abovead, .absoluteAd_wss, .ac_adbox, .acm_ad_zones, .ad--300, .ad--468, .ad--468-60, .ad--728x90, .ad--article-top, .ad--b, .ad--bottom-label, .ad--bottommpu, .ad--c, .ad--dart, .ad--e, .ad--footer, .ad--google, .ad--homepage-top, .ad--inner, .ad--large, .ad--leaderboard, .ad--mpu, .ad--noscroll, .ad--pushdown, .ad--scroll, .ad--showmob, .ad--square-rectangle, .ad--top-label, .ad--top-leaderboard, .ad--top-slot, .ad-1, .ad-120-60, .ad-120-600-inner, .ad-120x60, .ad-120x600, .ad-120x90, .ad-125, .ad-125x125, .ad-140x45-2, .ad-150, .ad-160, .ad-160-160, .ad-160-600, .ad-160x600, .ad-160x600-gallery, .ad-160x600-home, .ad-160x600-wrap, .ad-160x600x1, .ad-160x600x2, .ad-160x600x3, .ad-194, .ad-2, .ad-200, .ad-200-big, .ad-200-small, .ad-200x200, .ad-228x94, .ad-230x90, .ad-234, .ad-246x90, .ad-250, .ad-250x125, .ad-250x300, .ad-260x60, .ad-270x100, .ad-300, .ad-300-250, .ad-300-250-600, .ad-300-600, .ad-300-b, .ad-300-b-absolute, .ad-300-block, .ad-300-blog, .ad-300-dummy, .ad-300-flex, .ad-300x, .ad-300x100, .ad-300x200, .ad-300x250, .ad-300x250-first, .ad-300x250-home, .ad-300x250-right0, .ad-300x250-section, .ad-300x250-singlepost, .ad-300x250_600x250, .ad-300x600, .ad-300x70, .ad-300x75, .ad-319x128, .ad-336x280, .ad-336x280B, .ad-350, .ad-355x75, .ad-3x1, .ad-4, .ad-468, .ad-468x120, .ad-468x60, .ad-5, .ad-544x250, .ad-560, .ad-6, .ad-600, .ad-635x40, .ad-7, .ad-720-affiliate, .ad-728, .ad-728-90, .ad-728-banner, .ad-728x90, .ad-728x90-1, .ad-728x90-top, .ad-728x90-top0, .ad-728x90_forum, .ad-768, .ad-88-60, .ad-88-text, .ad-88x31, .ad-90x600, .ad-970, .ad-970x50, .ad-970x90, .ad-BANNER, .ad-CUSTOM, .ad-E, .ad-LREC, .ad-LREC2, .ad-Leaderboard, .ad-MPU, .ad-MediumRectangle, .ad-PENCIL, .ad-RR, .ad-S, .ad-Square, .ad-SuperBanner, .ad-TOPPER, .ad-W, .ad-a, .ad-abc, .ad-above-header, .ad-adSense, .ad-adcode, .ad-adlink-bottom, .ad-adlink-side, .ad-adsense-block-250, .ad-after-content, .ad-alsorectangle, .ad-alternative, .ad-amongst-container, .ad-area, .ad-area-small, .ad-article-breaker, .ad-atf, .ad-atf-medRect, .ad-b, .ad-background, .ad-background-intra-body, .ad-banner, .ad-banner-300, .ad-banner-bkgd, .ad-banner-container, .ad-banner-image, .ad-banner-label, .ad-banner-leaderboard, .ad-banner-placeholder, .ad-banner-smaller, .ad-banner-top, .ad-banner-top-wrapper, .ad-banner-vertical, .ad-banner-wrapper, .ad-banner728-top, .ad-banr, .ad-bar, .ad-below-images, .ad-below-player, .ad-belowarticle, .ad-bg, .ad-big, .ad-big-box, .ad-bigbox, .ad-bigboxSub, .ad-bigsize, .ad-billboard, .ad-bline, .ad-block, .ad-block-240x400, .ad-block-300-widget, .ad-block-300x250, .ad-block-big, .ad-block-bottom, .ad-block-clear-back, .ad-block-holder, .ad-block-in-post, .ad-block-square, .ad-block-wide, .ad-blog2biz, .ad-blogads, .ad-board, .ad-body, .ad-boombox, .ad-border, .ad-bordered, .ad-borderless, .ad-bot, .ad-bottom, .ad-bottom-container, .ad-bottom728x90, .ad-bottomLeft, .ad-bottomleader, .ad-bottomline, .ad-box-300x250, .ad-box-adsea, .ad-box-caption, .ad-box-container, .ad-box-up, .ad-box1, .ad-box2, .ad-box3, .ad-boxbottom, .ad-boxes, .ad-boxtop, .ad-break, .ad-breaker, .ad-breakout, .ad-browse-rectangle, .ad-bt, .ad-btn, .ad-btn-heading, .ad-bug-300w, .ad-button, .ad-buttons, .ad-cad, .ad-calendar, .ad-call-300x250, .ad-callout, .ad-caption, .ad-card-container, .ad-cat, .ad-catfish, .ad-cell, .ad-center, .ad-chartbeatwidget, .ad-choices, .ad-circ, .ad-click, .ad-cluster, .ad-cluster-container, .ad-codes, .ad-col, .ad-col-02, .ad-column, .ad-comment, .ad-companion, .ad-contain, .ad-contain-300x250, .ad-contain-top, .ad-container--featured_videos, .ad-container--stripe, .ad-container--taboola, .ad-container-160x600, .ad-container-300x250, .ad-container-728, .ad-container-728x90, .ad-container-994x282, .ad-container-LEADER, .ad-container-bot, .ad-container-bottom, .ad-container-dk, .ad-container-embedded, .ad-container-leaderboard, .ad-container-left, .ad-container-responsive, .ad-container-right, .ad-container-side, .ad-container-tool, .ad-container-top, .ad-container-topad, .ad-container__ad-slot, .ad-container_row, .ad-content, .ad-content-area, .ad-content-rectangle, .ad-context, .ad-curtain, .ad-custom-size, .ad-d, .ad-desktop, .ad-desktop-only, .ad-dfp-column, .ad-dfp-row, .ad-disclaimer, .ad-display, .ad-div, .ad-diver, .ad-divider, .ad-dt, .ad-e, .ad-enabled, .ad-engage, .ad-entry-wrapper, .ad-exchange, .ad-expand, .ad-external, .ad-f-monster, .ad-fadein, .ad-feature-content, .ad-feature-sponsor, .ad-feature-text, .ad-feedback, .ad-field, .ad-filler, .ad-fix, .ad-flag, .ad-flex, .ad-footer, .ad-footer-empty, .ad-footer-leaderboard, .ad-force-center, .ad-forum, .ad-full-width, .ad-fullbanner, .ad-fullbanner-btf-container, .ad-google, .ad-google-contextual, .ad-gpt, .ad-gpt-breaker, .ad-gpt-container, .ad-gpt-main, .ad-gpt-vertical, .ad-graphic-large, .ad-gray, .ad-grey, .ad-grid-125, .ad-group, .ad-grp, .ad-hdr, .ad-head, .ad-header, .ad-header-container, .ad-header-pencil, .ad-header-sidebar, .ad-heading, .ad-headliner-container, .ad-here, .ad-hide-mobile, .ad-hideable, .ad-hldr-tmc, .ad-hold, .ad-holder, .ad-home-bottom, .ad-home-right, .ad-homeleaderboard, .ad-homepage, .ad-homepage-1, .ad-homepage-2, .ad-homepage-one, .ad-hor, .ad-horizontal, .ad-horizontal-top, .ad-hpto, .ad-iab-txt, .ad-icon, .ad-identifier, .ad-iframe, .ad-imagehold, .ad-img, .ad-img300X250, .ad-in-300x250, .ad-in-content-300, .ad-in-post, .ad-in-results, .ad-incontent-ad-plus-bottom, .ad-incontent-ad-plus-middle, .ad-incontent-ad-plus-middle2, .ad-incontent-ad-plus-middle3, .ad-incontent-ad-plus-top, .ad-incontent-wrap, .ad-index, .ad-index-main, .ad-indicator-horiz, .ad-inline, .ad-inner, .ad-innr, .ad-insert, .ad-inserter, .ad-inserter-widget, .ad-integrated-display, .ad-internal, .ad-interruptor, .ad-interstitial, .ad-island, .ad-item, .ad-item-related, .ad-label, .ad-lable, .ad-landscape, .ad-large-game, .ad-layer, .ad-lazy-support-yes, .ad-lb, .ad-lead, .ad-lead-bottom, .ad-leader, .ad-leader-bottom, .ad-leader-plus-top, .ad-leader-top, .ad-leader-wrap, .ad-leader-wrapper, .ad-leaderboard, .ad-leaderboard-companion, .ad-leaderboard-container, .ad-leaderboard-marquee, .ad-leaderboard-top, .ad-leaderboard_river, .ad-leaderbody, .ad-leaderheader, .ad-leadtop, .ad-left, .ad-left3, .ad-leftrail, .ad-line, .ad-link, .ad-link-label, .ad-link-left, .ad-link-right, .ad-links, .ad-links-text, .ad-loaded, .ad-location, .ad-location-container, .ad-location-header, .ad-lock, .ad-lock-content, .ad-lower_rec, .ad-lower_river, .ad-lowerboard, .ad-lrec, .ad-mad, .ad-main, .ad-manager-ad, .ad-marker, .ad-marketplace, .ad-marketplace-horizontal, .ad-marketswidget, .ad-marquee, .ad-med, .ad-med-rec, .ad-med-rect, .ad-med-rect-tmp, .ad-medRec, .ad-media-marquee, .ad-media-marquee-btn, .ad-medium, .ad-medium-rectangle, .ad-medium-two, .ad-medrect, .ad-megaboard, .ad-message, .ad-messaging, .ad-mid-article-container, .ad-midleader, .ad-mobile, .ad-mobile-banner, .ad-mod, .ad-module, .ad-mpl, .ad-mpu, .ad-mpu-bottom, .ad-mpu-container, .ad-mpu-middle, .ad-mpu-middle2, .ad-mpu-placeholder, .ad-mpu-plus-top, .ad-mpu-top, .ad-mpu__aside, .ad-mpufixed, .ad-mrec, .ad-mrect, .ad-msg, .ad-msgunit, .ad-msn, .ad-national-1, .ad-new, .ad-no-style, .ad-noBorderAndMargin, .ad-noline, .ad-note, .ad-notice, .ad-notice-small, .ad-on, .ad-one, .ad-other, .ad-outlet, .ad-output-middle, .ad-output-wrapper, .ad-outside, .ad-overlay, .ad-packs, .ad-padding, .ad-page-leader, .ad-page-medium, .ad-pagehead, .ad-panel, .ad-panorama, .ad-parallax-wrap, .ad-parent-hockey, .ad-passback-o-rama, .ad-pb, .ad-peg, .ad-permalink, .ad-personalise, .ad-place-active, .ad-place-holder, .ad-placeholder, .ad-placement, .ad-plea, .ad-pos-top, .ad-position, .ad-position-1, .ad-post, .ad-post300X250, .ad-postText, .ad-poster, .ad-prevent-jump, .ad-primary, .ad-primary-sidebar, .ad-priority, .ad-pro70, .ad-promo, .ad-promoted-game, .ad-pushdown, .ad-r, .ad-rail, .ad-rect, .ad-rect-atf-01, .ad-rect-top-right, .ad-rectangle, .ad-rectangle-banner, .ad-rectangle-container, .ad-rectangle-long, .ad-rectangle-long-sky, .ad-rectangle-text, .ad-rectangle-wide, .ad-rectangle-xs, .ad-refresh, .ad-region-delay-load, .ad-region__top, .ad-related, .ad-relatedbottom, .ad-responsive-wide, .ad-rh, .ad-ri, .ad-right, .ad-right-header, .ad-right-txt, .ad-right1, .ad-right2, .ad-right3, .ad-roadblock, .ad-rotation, .ad-row, .ad-row-viewport, .ad-s, .ad-s-rendered, .ad-sample, .ad-scl, .ad-script-processed, .ad-scroll, .ad-scrollpane, .ad-search-grid, .ad-section, .ad-section-body, .ad-sense, .ad-sep, .ad-served, .ad-shifted, .ad-show-label, .ad-show-text, .ad-showcase, .ad-side, .ad-side-one, .ad-sidebar, .ad-sidebar-180-150, .ad-sidebar-300-250, .ad-sidebar-ad-message, .ad-sidebar-border, .ad-sidebar-outer, .ad-sidebar300, .ad-sidebar_right_above, .ad-sidebar_right_below, .ad-siderail, .ad-signup, .ad-sitewide, .ad-sky, .ad-skyscr, .ad-skyscraper, .ad-skyscraper-label, .ad-skyscraper1, .ad-skyscraper2, .ad-skyscraper3, .ad-slider, .ad-slot, .ad-slot--inline, .ad-slot--mpu-banner-ad, .ad-slot-1, .ad-slot-2, .ad-slot-234-60, .ad-slot-300-250, .ad-slot-728-90, .ad-slot-a, .ad-slot-banner, .ad-slot-container, .ad-slot-sidebar, .ad-slot-sidebar-b, .ad-slot-tall, .ad-slot-top-728, .ad-slot__label, .ad-slot__oas, .ad-slug, .ad-smallBP, .ad-source, .ad-sp, .ad-space, .ad-space-mpu-box, .ad-space-topbanner, .ad-spacer, .ad-span, .ad-speedbump, .ad-splash, .ad-sponsor, .ad-sponsor-large-container, .ad-sponsor-text, .ad-sponsored-feed-top, .ad-sponsored-links, .ad-sponsored-post, .ad-sponsors, .ad-spot, .ad-spotlight, .ad-square, .ad-square2-container, .ad-square300, .ad-squares, .ad-stack, .ad-statement, .ad-sticky, .ad-story-inject, .ad-story-top, .ad-strip, .ad-subnav-container, .ad-subtitle, .ad-superbanner, .ad-t, .ad-table, .ad-tabs, .ad-tag, .ad-tag-square, .ad-tall, .ad-target2-wrapper, .ad-text, .ad-text-blockA01, .ad-text-blockB01, .ad-text-label, .ad-text-link, .ad-text-links, .ad-text-placeholder-3, .ad-textG01, .ad-textads, .ad-textlink, .ad-thanks, .ad-ticker, .ad-tile, .ad-tl1, .ad-top, .ad-top-300x250, .ad-top-728, .ad-top-728x90, .ad-top-banner, .ad-top-box-right, .ad-top-in, .ad-top-lboard, .ad-top-left, .ad-top-mpu, .ad-top-rectangle, .ad-top-wrapper, .ad-top1, .ad-top2, .ad-topbanner, .ad-topleader, .ad-topright, .ad-total, .ad-total1, .ad-tower, .ad-towers, .ad-txt, .ad-type, .ad-type1, .ad-type10, .ad-type2, .ad-type3, .ad-unit, .ad-unit-300, .ad-unit-300-wrapper, .ad-unit-anchor, .ad-unit-container, .ad-unit-horisontal, .ad-unit-inline-center, .ad-unit-label, .ad-unit-medium-retangle, .ad-unit-mpu, .ad-unit-top, .ad-unit-wrapper, .ad-update, .ad-upper_rec, .ad-us, .ad-v2, .ad-vert, .ad-vertical, .ad-vertical-container, .ad-vertical-stack-ad, .ad-vtu, .ad-w300, .ad-wallpaper-container, .ad-wallpaper-panorama-container, .ad-warning, .ad-wgt, .ad-wide, .ad-wide-bottom, .ad-widget, .ad-widget-area, .ad-widget-list, .ad-width-300, .ad-width-728, .ad-windowshade-full, .ad-wings__link, .ad-with-background, .ad-with-us, .ad-wrap, .ad-wrap--leaderboard, .ad-wrap--mrec, .ad-wrapper, .ad-x10x20x30, .ad-x31-full, .ad-zone, .ad-zone-container, .ad-zone-s-q-l, .ad.super, .ad01, .ad02, .ad03, .ad04, .ad08sky, .ad1-left, .ad1-right, .ad10, .ad100, .ad1000, .ad1001, .ad100x100, .ad120, .ad120_600, .ad120x120, .ad120x240GrayBorder, .ad120x240backgroundGray, .ad120x60, .ad120x600, .ad125, .ad125x125, .ad125x125a, .ad125x125b, .ad140, .ad160, .ad160600, .ad160_blk, .ad160_l, .ad160_r, .ad160x160, .ad160x600, .ad160x600GrayBorder, .ad160x600box, .ad170x30, .ad18, .ad180, .ad185x100, .ad19, .ad1Image, .ad1_bottom, .ad1_latest, .ad1_top, .ad1b, .ad1left, .ad1x1, .ad200, .ad200x60, .ad220x50, .ad230, .ad233x224, .ad234, .ad234x60, .ad236x62, .ad240, .ad250, .ad250-h1, .ad250-h2, .ad250_250, .ad250c, .ad250wrap, .ad250x250, .ad250x300, .ad260x60, .ad284x134, .ad2content_box, .ad300, .ad300-hp-top, .ad3001, .ad300250, .ad300Block, .ad300Wrapper, .ad300X250, .ad300_2, .ad300_250, .ad300_bg, .ad300_ver2, .ad300b, .ad300banner, .ad300mrec1, .ad300shows, .ad300top, .ad300w, .ad300x-placeholder, .ad300x100, .ad300x111, .ad300x120, .ad300x150, .ad300x250, .ad300x250-1, .ad300x250-2, .ad300x250-home, .ad300x250-hp-features, .ad300x250-inline, .ad300x250-stacked, .ad300x2501, .ad300x250GrayBorder, .ad300x250Module, .ad300x250Right, .ad300x250Top, .ad300x250_box, .ad300x250_container, .ad300x250a, .ad300x250b, .ad300x250box, .ad300x250box2, .ad300x250flex, .ad300x250s, .ad300x40, .ad300x50-right, .ad300x600, .ad300x77, .ad300x90, .ad310, .ad315, .ad320x250, .ad336, .ad336x250, .ad336x280, .ad336x362, .ad343x290, .ad350, .ad350r, .ad360, .ad400, .ad400right, .ad400x40, .ad450, .ad468, .ad468_60, .ad468x60, .ad468x60Wrap, .ad468x60_main, .ad470x60, .ad530, .ad540x90, .ad590, .ad590x90, .ad5_container, .ad600, .ad612x80, .ad620x70, .ad626X35, .ad640x480, .ad640x60, .ad644, .ad650x140, .ad652, .ad670x83, .ad728, .ad72890, .ad728By90, .ad728_90, .ad728_blk, .ad728_cont, .ad728_wrap, .ad728cont, .ad728h, .ad728x90, .ad728x90-1, .ad728x90-2, .ad728x90-main_wrap, .ad728x90WithLabel, .ad728x90_2, .ad728x90_container, .ad728x90_wrap, .ad728x90box, .ad728x90btf, .ad728x90container, .ad768x90, .ad90, .ad90x780, .ad940x30, .ad954x60, .ad960, .ad960x185, .ad960x90, .ad970x30, .ad970x90, .ad980, .ad980x120, .ad980x50box, .ad987, .adAgate, .adAlert, .adAlone300, .adArea, .adArea674x60, .adAreaLC, .adArticleBanner, .adArticleBody, .adArticleRecommend, .adArticleSidetile, .adArticleTopText, .adAuto, .adBGcolor, .adBan, .adBanner, .adBanner300x250, .adBanner728x90, .adBannerTyp1, .adBannerTypSortableList, .adBannerTypW300, .adBar, .adBarCenter, .adBarLeft, .adBarRight, .adBelt, .adBgBottom, .adBgClick, .adBgMId, .adBgTop, .adBigBoxFirst, .adBigBoxSecond, .adBigBoxThird, .adBillboard, .adBkgd, .adBlock, .adBlock-300-250, .adBlock160x600Spot1, .adBlock728, .adBlockBottom, .adBlockBottomBreak, .adBlockNext, .adBlockSpacer, .adBlockSpot, .adBlock_1, .adBlock_14, .adBlock_15, .adBlock_17, .adBlock_2, .adBlock_3, .adBlock_6, .adBlock_8, .adBlock_9, .adBodyBlockBottom, .adBorder, .adBorders, .adBottomBoard, .adBottomLink, .adBottomboxright, .adBox, .adBox-mr, .adBox1, .adBox2, .adBox230X96, .adBox250, .adBox3b, .adBox5, .adBox6, .adBox728, .adBox728X90, .adBox728X90_header, .adBoxBody, .adBoxBorder, .adBoxContainer, .adBoxContent, .adBoxFooter, .adBoxHeader, .adBoxInBignews, .adBoxSidebar, .adBoxSingle, .adBoxTitle, .adBox_1, .adBox_3, .adBrandpanel, .adBtm, .adBuyRight, .adBwrap, .adCMRight, .adCMSlide, .adCall, .adCaptionText, .adCell, .adCenter, .adCenterAd, .adCentered, .adCentertile, .adChoice, .adChoiceLogo, .adChoicesLogo, .adClm, .adClose, .adCode, .adColBgBottom, .adColumn, .adColumnLeft, .adComponent, .adCont, .adContRight, .adContTop, .adContainer1, .adContainerRectangle, .adContainerSide, .adContainer_125x125, .adContainer_728x90, .adContainerg6, .adContent, .adContentAd, .adContour, .adCopy, .adCreative, .adCs, .adCube, .adDefRect, .adDialog, .adDingT, .adDiv, .adDivSmall, .adElement, .adEmployment, .adFender3, .adFooterLinks, .adFrame, .adFrameCnt, .adFrameContainer, .adFrames, .adFtr, .adFull, .adFullWidth, .adFullWidthBottom, .adFullWidthMiddle, .adGlobalHeader, .adGogleBox, .adGoogle, .adGroup, .adHead, .adHeader, .adHeaderAdbanner, .adHeaderText, .adHeaderblack, .adHeadline, .adHeadlineSummary, .adHed, .adHolder, .adHolder2, .adHoldert, .adHome300x250, .adHorisontal, .adHorisontalNoBorder, .adHorizontalTextAlt, .adHplaceholder, .adHz, .adIMm, .adIframe, .adIframeCount, .adImg, .adImgIM, .adInArticle, .adInNews, .adInner, .adInnerLeftBottom, .adInteractive, .adIsland, .adItem, .adLabel, .adLabel160x600, .adLabel300x250, .adLabelLine, .adLabels, .adLargeRec, .adLargeRect, .adLat, .adLeader, .adLeaderForum, .adLeaderboard, .adLeft, .adLine, .adLine300x100, .adLine300x250, .adLine300x600, .adLink, .adLinkCnt, .adListB, .adLoaded, .adLoader, .adLocal, .adLocation, .adMPU, .adMPUHome, .adMarker, .adMarkerBlock, .adMastheadLeft, .adMastheadRight, .adMedRectBox, .adMedRectBoxLeft, .adMediaMiddle, .adMediumRectangle, .adMegaBoard, .adMeldGuts, .adMessage, .adMiddle, .adMiniTower, .adMinisLR, .adMkt2Colw, .adMod, .adModule, .adModule300, .adModuleAd, .adModule_square2, .adMpu, .adMpuHolder, .adMrginBottom, .adNarrow, .adNetPromo, .adNewsChannel, .adNoBorder, .adNoOutline, .adNone, .adNote, .adNotice, .adNotice90, .adNoticeOut, .adNotification, .adObj, .adOne, .adOuterContainer, .adOverlay, .adPageBorderL, .adPageBorderR, .adPanel, .adPanelContent, .adPlaceholder, .adPlaceholder35, .adPlaceholder54, .adPlaceholder_foot, .adPod, .adPosition, .adRecommend, .adRecommendRight, .adRect, .adRectangle, .adRectangleUnit, .adRegionSelector, .adRemove, .adReportsLink, .adResponsive, .adResult, .adResults, .adRight, .adRightSide, .adRotator, .adRow, .adRowTopWrapper, .adSKY, .adSTHomePage, .adSection, .adSection_rt, .adSelfServiceAdvertiseLink, .adSenceImagePush, .adSense, .adSepDiv, .adServer, .adSeven, .adSide, .adSide203, .adSide230, .adSidebarButtons, .adSidetileplus, .adSize_MedRec, .adSkin, .adSkinLayerConfig, .adSky, .adSky600, .adSkyOrMpu, .adSkyscaper, .adSkyscraper, .adSkyscraperHolder, .adSlice, .adSlide, .adSlot, .adSlotContainer, .adSlug, .adSpBelow, .adSpace, .adSpace300x250, .adSpace950x90, .adSpacer, .adSplash, .adSponsor, .adSponsorText, .adSpot, .adSpot-brought, .adSpot-mrec, .adSpot-searchAd, .adSpot-textBox, .adSpot-textBoxGraphicRight, .adSpot-twin, .adSpotIsland, .adSquare, .adStatementText, .adStyle, .adStyle1, .adSub, .adSubColPod, .adSummary, .adSuperboard, .adSupertower, .adTD, .adTXTnew, .adTab, .adTag, .adTag-wrap, .adText, .adTextPmpt, .adTicker, .adTileWrap, .adTiler, .adTitle, .adTitleR, .adTop, .adTopBanner_nomobile, .adTopBk, .adTopHome, .adTopLeft, .adTopLink, .adTopRight, .adTopboxright, .adTout, .adTower, .adTwo, .adTxt, .adType2, .adUnit, .adUnitHorz, .adUnitVert, .adUnitVert_noImage, .adVar, .adVertical, .adVideo, .adVideo2, .adVl, .adVplaceholder, .adWarning, .adWebBoard, .adWideSkyscraper, .adWideSkyscraperRight, .adWidget, .adWidgetBlock, .adWidgetSponsor, .adWithTab, .adWord, .adWrap, .adWrapLg, .adWrapper, .adZone, .adZoneRight, .ad_0, .ad_1, .ad_1000x90, .ad_100x100, .ad_1200, .ad_120x60, .ad_120x600, .ad_120x90, .ad_125, .ad_130x90, .ad_150x150, .ad_160, .ad_160_600, .ad_160x600, .ad_180x150, .ad_1day9, .ad_2, .ad_200, .ad_200x200, .ad_234x60, .ad_240, .ad_240x400, .ad_242_90_top, .ad_250, .ad_250x200, .ad_250x250, .ad_250x250_w, .ad_3, .ad_300, .ad_300250, .ad_300Home, .ad_300Side, .ad_300_120, .ad_300_250, .ad_300_250_1, .ad_300_250_2, .ad_300_250_cpv, .ad_300_250_wrapper, .ad_300_600, .ad_300s, .ad_300x100, .ad_300x240, .ad_300x250, .ad_300x250_box_right, .ad_300x250_live, .ad_300x50, .ad_300x500, .ad_300x60, .ad_300x600, .ad_320x250_async, .ad_320x360, .ad_326x260, .ad_330x110, .ad_336, .ad_336_gr_white, .ad_336x280, .ad_336x90, .ad_338_282, .ad_350x100, .ad_350x250, .ad_4, .ad_400x200, .ad_468, .ad_468x60, .ad_4_row, .ad_5, .ad_600, .ad_630x130, .ad_640x90, .ad_680x15, .ad_728, .ad_72890, .ad_72890_box, .ad_728Home, .ad_728_90, .ad_728_90_1, .ad_728_90_top, .ad_728_90b, .ad_728_in, .ad_728_top, .ad_728_unit, .ad_728_v2, .ad_728x90, .ad_728x90-1, .ad_728x90-2, .ad_728x90_top, .ad_728x90b, .ad_88x31, .ad_925x90, .ad_954-60, .ad_960, .ad_970_2, .ad_970x90_prog, .ad_980x260, .ad_CustomAd, .ad_Flex, .ad_Left, .ad_Right, .ad__centered, .ad__container, .ad__in-loop, .ad__in-loop--desktop, .ad__inline, .ad__label, .ad__leaderboard, .ad__mpu, .ad__placeholder, .ad__rectangle, .ad__wrapper, .ad_a, .ad_adInfo, .ad_ad_160, .ad_ad_300, .ad_adblade, .ad_adsense_spacer, .ad_adv, .ad_amazon, .ad_area, .ad_area_two, .ad_article_top_left, .ad_atf_300x250, .ad_atf_728x90, .ad_avu_300x250, .ad_back, .ad_background, .ad_bank_wrapper, .ad_banner, .ad_banner2, .ad_banner_2, .ad_banner_234, .ad_banner_250x250, .ad_banner_468, .ad_banner_728x90_inner, .ad_banner_border, .ad_banner_div, .ad_bar, .ad_below_content, .ad_belowmenu, .ad_bg, .ad_bg_300x250, .ad_bgskin, .ad_big_banner, .ad_bigbox, .ad_billboard, .ad_biz, .ad_blk, .ad_block, .ad_block_1, .ad_block_2, .ad_block_300x250, .ad_block_336, .ad_block_338, .ad_block__336_d1, .ad_block_leader2, .ad_bn, .ad_body, .ad_border, .ad_botbanner, .ad_bottom, .ad_bottom_728, .ad_bottom_leaderboard, .ad_bottom_left, .ad_bottom_mpu, .ad_bottom_space, .ad_bottomline, .ad_box, .ad_box1, .ad_box2, .ad_box300x250, .ad_box_2, .ad_box_ad, .ad_box_div, .ad_box_new, .ad_box_righ, .ad_box_right_120, .ad_box_spacer, .ad_box_title, .ad_box_top, .ad_boxright1, .ad_break, .ad_break_container, .ad_btf, .ad_btf_300x250, .ad_btf_728x90, .ad_buttom_banner, .ad_buttons_300, .ad_buttons_320, .ad_callout, .ad_caption, .ad_center, .ad_center_bottom, .ad_centered, .ad_cheat, .ad_choice, .ad_choices, .ad_cl, .ad_claim, .ad_click, .ad_code, .ad_col, .ad_col_a, .ad_column, .ad_column_box, .ad_column_hl, .ad_common, .ad_cont, .ad_cont_footer, .ad_contain, .ad_container, .ad_container_300x250, .ad_container_5, .ad_container_6, .ad_container_7, .ad_container_728x90, .ad_container_8, .ad_container_9, .ad_container__sidebar, .ad_container__top, .ad_container_body, .ad_content, .ad_content_wide, .ad_contents, .ad_custombanner, .ad_db, .ad_default, .ad_deferrable, .ad_description, .ad_descriptor, .ad_desktop, .ad_disclaimer, .ad_div_banner, .ad_embed, .ad_eniro, .ad_entry_title_under, .ad_entrylists_end, .ad_event_mast_wrapper, .ad_external, .ad_eyebrow, .ad_feature, .ad_filler, .ad_flash, .ad_flat-boxright10, .ad_flat-boxright6, .ad_flat-boxright9, .ad_float, .ad_floating_box, .ad_font, .ad_footer, .ad_for_layout, .ad_frame, .ad_framed, .ad_front_promo, .ad_full_click, .ad_fullwidth, .ad_gal, .ad_global_header, .ad_gpt, .ad_grid, .ad_gutter_top, .ad_half_page, .ad_halfpage, .ad_hat_728, .ad_hat_banner_300, .ad_hat_top, .ad_head, .ad_head_rectangle, .ad_head_wide, .ad_header, .ad_header_lb, .ad_header_left, .ad_header_noad, .ad_heading, .ad_headline, .ad_help_link, .ad_holder, .ad_home_block, .ad_honcode_label, .ad_horizontal_marker, .ad_hpm, .ad_hr, .ad_hyper_wrap, .ad_identifier, .ad_iframe2, .ad_ifrwrap, .ad_image, .ad_image_container, .ad_img, .ad_imgae_150, .ad_in_column, .ad_in_head, .ad_index02, .ad_indicator, .ad_info_block, .ad_inline, .ad_inset, .ad_island, .ad_island2_spacer, .ad_island_feedback, .ad_island_spacer, .ad_isolation, .ad_item, .ad_jnaught, .ad_js_deal_top, .ad_keywords_bot, .ad_keywords_bot_r, .ad_l, .ad_label, .ad_label1, .ad_label2a, .ad_label_centered, .ad_label_long, .ad_label_method, .ad_label_top, .ad_large, .ad_launchpad, .ad_leader, .ad_leader_bottom, .ad_leader_plus_top, .ad_leaderboard, .ad_leaderboard_atf, .ad_leaderboard_top, .ad_left_cell, .ad_left_column, .ad_lft, .ad_line, .ad_line2, .ad_link, .ad_link1, .ad_link_468, .ad_link_area, .ad_link_label, .ad_link_label_vert, .ad_links, .ad_linkunit, .ad_lnks, .ad_loc, .ad_long, .ad_lrec, .ad_lt, .ad_main, .ad_maintopad, .ad_margin, .ad_masthead, .ad_med, .ad_medium_rectangle, .ad_medrec, .ad_medrect, .ad_megabanner, .ad_message, .ad_microlen, .ad_middle, .ad_middle_banner, .ad_middle_hub_page, .ad_mobile, .ad_mod, .ad_module, .ad_movFocus, .ad_mp, .ad_mpu, .ad_mpu_top, .ad_mr, .ad_mrec, .ad_mrec_title_article, .ad_mrect, .ad_mrectangle, .ad_msg, .ad_new_box01, .ad_new_box02, .ad_news, .ad_newsstream, .ad_no_border, .ad_note, .ad_notice, .ad_nsRT_300_250, .ad_nsbd_300_250, .ad_on_article, .ad_one, .ad_outer, .ad_overlays, .ad_p360, .ad_pagebody, .ad_panel, .ad_panel_1, .ad_panel_2, .ad_partner, .ad_partners, .ad_perma-panorama, .ad_pic, .ad_placeholder, .ad_placement, .ad_placement_300x250, .ad_placement_small, .ad_plane_336, .ad_plus, .ad_policy_link_br, .ad_position, .ad_post, .ad_posttop, .ad_power, .ad_primary, .ad_promo, .ad_promo1, .ad_promo_spacer, .ad_r, .ad_r1_menu, .ad_rakuten, .ad_rakuten_wrapper, .ad_rec, .ad_rect, .ad_rect_contr, .ad_rectangle, .ad_rectangle_300_250, .ad_rectangle_medium, .ad_rectangular, .ad_regular1, .ad_regular2, .ad_regular3, .ad_reminder, .ad_report_btn, .ad_rightSky, .ad_right_cell, .ad_right_col, .ad_right_column, .ad_right_column160, .ad_rightside, .ad_row, .ad_row_bottom_item, .ad_rtg300, .ad_secondary, .ad_section_300x250, .ad_section_728x90, .ad_segment, .ad_sense_01, .ad_sense_footer_container, .ad_share_box, .ad_shuffling_text, .ad_side, .ad_sidebar, .ad_sidebar_bigbox, .ad_size_160x600, .ad_sky, .ad_skyscpr, .ad_skyscraper, .ad_skyscrapper, .ad_slider_out, .ad_slot, .ad_slot_right, .ad_slug, .ad_slug_font, .ad_slug_healthgrades, .ad_slug_table, .ad_small, .ad_sonar, .ad_space, .ad_space_300_250, .ad_space_730, .ad_space_holder, .ad_space_in, .ad_space_rgt, .ad_space_w300_h250, .ad_spacer, .ad_special_badge, .ad_spons_box, .ad_sponsor, .ad_sponsor_fp, .ad_sponsoredlinks, .ad_sponsoredsection, .ad_spot, .ad_spot_b, .ad_spot_c, .ad_square, .ad_square_r, .ad_square_r_top, .ad_square_top, .ad_station, .ad_story_island, .ad_stream_hd, .ad_strip_noline, .ad_sub, .ad_supersize, .ad_swf, .ad_tag, .ad_tag_middle, .ad_text, .ad_text_link, .ad_text_links, .ad_text_vertical, .ad_text_w, .ad_textlink_box, .ad_thumbnail_header, .ad_title, .ad_title_small, .ad_tlb, .ad_top, .ad_top1, .ad_top_1, .ad_top_2, .ad_top_3, .ad_top_banner, .ad_top_leaderboard, .ad_top_left, .ad_top_mpu, .ad_top_right, .ad_topic_content, .ad_topright, .ad_topshop, .ad_tower, .ad_trailer_header, .ad_trick_header, .ad_trick_left, .ad_ttl, .ad_txt2, .ad_type_1, .ad_type_adsense, .ad_type_dfp, .ad_under, .ad_under_royal_slider, .ad_unit, .ad_unit_300_x_250, .ad_unit_rail, .ad_url, .ad_v2, .ad_v3, .ad_v300, .ad_vertisement, .ad_w300i, .ad_w_us_a300, .ad_warn, .ad_warning, .ad_wid300, .ad_wide, .ad_widget, .ad_widget_200_100, .ad_widget_200_200, .ad_word, .ad_wrap, .ad_wrapper, .ad_wrapper_false, .ad_wrapper_fixed, .ad_wrapper_top, .ad_wrp, .ad_xrail_top, .ad_zone, .adamazon, .adarea, .adarea-long, .adb-728x90, .adback, .adbadge, .adban-hold-narrow, .adbanner, .adbanner-300-250, .adbanner-bottom, .adbanner1, .adbanner2nd, .adbannerbox, .adbanneriframe, .adbannerright, .adbannertop, .adbar, .adbase, .adbbox, .adbckgrnd, .adbetween, .adbkgnd, .adblade, .adblade-container, .adbladeimg, .adblk, .adblock-240-400, .adblock-300-300, .adblock-600-120, .adblock-bottom, .adblock-header, .adblock-header1, .adblock-main, .adblock-popup, .adblock-top, .adblock-top-left, .adblock-wide, .adblock300, .adblock300250, .adblock300x250Spot1, .adblock728x90, .adblock_noborder, .adblock_primary, .adblocks-topright, .adboard, .adborder, .adborderbottom, .adbordertop, .adbot, .adbot_postbit, .adbot_showthread, .adbottom, .adbottomright, .adbox-300x250, .adbox-468x60, .adbox-box, .adbox-outer, .adbox-rectangle, .adbox-slider, .adbox-title, .adbox-topbanner, .adbox-wrapper, .adbox1, .adbox160, .adbox2, .adbox300, .adbox300x250, .adbox336, .adbox600, .adbox728, .adboxVert, .adbox_300x600, .adbox_366x280, .adbox_468X60, .adbox_border, .adbox_bottom, .adbox_br, .adbox_cont, .adbox_largerect, .adbox_left, .adboxbg, .adboxbot, .adboxclass, .adboxcontent, .adboxcontentsum, .adboxes, .adboxesrow, .adboxlong, .adboxo, .adbreak, .adbrite2, .adbrite_post, .adbucks, .adbuddy-protected, .adbug, .adbutton, .adbutton-block, .adbuttons, .adbygoogle, .adcard, .adcasing, .adcenter, .adchange, .adchoices, .adchoices-link, .adclass, .adcode, .adcode2, .adcode_container, .adcodetop, .adcol1, .adcol2, .adcolumn, .adcolumn_wrapper, .adcomment, .adcont, .adcontainer300x250l, .adcontainer300x250r, .adcontent_box, .adcopy, .adctr, .add-column2, .add-header-area, .add-sidebar, .add300, .add300top, .add300x250, .add768, .addResources, .add_300_250, .add_300x250, .add_728x90_teckpage, .add_baner, .add_topbanner, .addarea, .addarearight, .addbanner, .addboxRight, .addisclaimer, .addiv, .adds2, .adds300x250, .adds620x90, .addtitle, .addvert, .addwide, .adengageadzone, .adenquire, .adexpl, .adf_tisers, .adfbox, .adfeedback, .adfeeds, .adfieldbg, .adfix, .adfix-300x250, .adflag, .adflexi, .adfloatleft, .adfloatright, .adfoot, .adfootbox, .adfooter, .adformobile, .adframe, .adframe2, .adframe_banner, .adframe_rectangle, .adfree, .adfront, .adfront-head, .adg_cell, .adg_row, .adg_table, .adg_table_cell, .adg_table_row, .adgear, .adgear-bb, .adgear_header, .adgeletti-ad-div, .adgoogle_block, .adhalfhome, .adhead, .adhead_h, .adhead_h_wide, .adheader, .adheader100, .adheader401, .adheader416, .adherebox, .adhi, .adhide, .adhint, .adholder, .adholder-300, .adholderban, .adhoriz, .adhref_box_ads, .adical_contentad, .adiframe, .adiframe250x250, .adinfo, .adinjwidget, .adinner, .adinpost, .adinsert, .adinsert-bdr, .adinsert160, .adinside, .adintext, .adintext-unten, .adintro, .adits, .adjimage2, .adjlink, .adkicker, .adkit, .adkit-advert, .adkit-lb-footer, .adkit_free_html, .adl125, .adlabel-horz, .adlabel-vert, .adlabel1, .adlabel2, .adlabel3, .adlabelleft, .adlarge, .adlarger, .adlayer, .adleader, .adleft1, .adlgbox, .adline, .adlink, .adlinkdiv, .adlinks, .adlinks-class, .adlist, .adlist1, .adlist2, .adlist__item--midstream, .adlnklst, .adlsot, .admain, .adman, .admarker, .admaster, .admediumred, .admedrec, .admeldBoxAd, .admessage, .admiddle, .admiddlesidebar, .administer-ad, .admods, .admodule, .admoduleB, .admpu, .admpu-small, .admz, .adnSpot, .adname, .adnation-banner, .adnet120, .adnet_area, .adnl_zone, .adnotecenter, .adnotice, .adocean728x90, .adonmedianama, .adops, .adp-AdPrefix, .adpacks, .adpacks_content, .adpad300, .adpad300spacer, .adpadding, .adpadtwo_div, .adpane, .adpic, .adplace, .adplace_center, .adplacement, .adplate-background, .adpod, .adpos-19, .adpos-20, .adpos-25, .adpos-26, .adpos-8, .adpost, .adproxy, .adrec, .adrechts, .adrect, .adrectangle, .adrectwrapper, .adright, .adright300, .adrightsm, .adrighttop, .adriverBanner, .adroot, .adrotate_top_banner, .adrotate_widget, .adrotate_widgets, .adrow, .adrow-post, .adrow1, .adrow1box1, .adrow1box3, .adrow1box4, .adrow2, .adrule, .ads--sidebar, .ads-1, .ads-120x600, .ads-125, .ads-125-widget, .ads-160-head, .ads-160x600, .ads-160x600-outer, .ads-166-70, .ads-180-65, .ads-2, .ads-220x90, .ads-250, .ads-290, .ads-3, .ads-300, .ads-300-250, .ads-300-box, .ads-300x250, .ads-300x300, .ads-300x80, .ads-301, .ads-336-197-qu, .ads-468, .ads-468x60-bordered, .ads-560-65, .ads-600-box, .ads-728-90, .ads-728by90, .ads-728x90, .ads-728x90-wrap, .ads-729, .ads-above-comments, .ads-ad, .ads-ads-top, .ads-advertorial, .ads-area, .ads-articlebottom, .ads-banner, .ads-banner-bottom, .ads-banner-js, .ads-banner-middle, .ads-banner-top-right, .ads-beforecontent, .ads-below-content, .ads-below-home, .ads-bg, .ads-bigbox, .ads-block, .ads-block-bottom-wrap, .ads-block-link-000, .ads-block-link-text, .ads-block-marketplace-container, .ads-block-menu-center, .ads-border, .ads-bottom, .ads-bottom-block, .ads-bottom-content, .ads-bottom-left, .ads-bottom-right, .ads-box, .ads-box-border, .ads-box-header, .ads-box-header-marketplace-right, .ads-box-header-pb, .ads-box-header-ws, .ads-box-header-wsl, .ads-btm, .ads-by, .ads-by-google-0, .ads-callback, .ads-card, .ads-cars-larger, .ads-cars-top2, .ads-categories-bsa, .ads-col, .ads-container-mediumrectangle, .ads-content, .ads-custom, .ads-div, .ads-divider, .ads-express, .ads-favicon, .ads-feed, .ads-fieldset, .ads-fif, .ads-flow, .ads-footer, .ads-full, .ads-google, .ads-half, .ads-header, .ads-header-left, .ads-header-right, .ads-here, .ads-holder, .ads-home-top-buttons-wrap, .ads-horizontal, .ads-horizontal-banner, .ads-inarticle, .ads-inline, .ads-inner, .ads-item, .ads-label, .ads-large, .ads-leaderboard, .ads-leaderboard-border, .ads-leaderboard-panel, .ads-left, .ads-line, .ads-link, .ads-links-general, .ads-long, .ads-main, .ads-margin, .ads-medium-rect, .ads-middle, .ads-middle-top, .ads-mini, .ads-module, .ads-movie, .ads-mpu, .ads-native-wrapper, .ads-note, .ads-outer, .ads-player-03, .ads-popup-corner, .ads-post, .ads-post-closing, .ads-post-full, .ads-profile, .ads-rectangle, .ads-right, .ads-right-min, .ads-rotate, .ads-scroller-box, .ads-section, .ads-side, .ads-sidebar, .ads-sidebar-boxad, .ads-single, .ads-site, .ads-sky, .ads-small, .ads-smartphone, .ads-sponsors, .ads-sponsors-125-left, .ads-sponsors-125-right, .ads-square, .ads-squares, .ads-static-video-overlay, .ads-story, .ads-stripe, .ads-styled, .ads-superbanner, .ads-text, .ads-title, .ads-top, .ads-top-content, .ads-top-left, .ads-top-right, .ads-top-spacer, .ads-txt, .ads-ul, .ads-wide, .ads-widget, .ads-widget-content, .ads-widget-partner-gallery, .ads-widget-sponsor-gallery, .ads-wrap, .ads-wrapper, .ads-zone, .ads01, .ads02, .ads03, .ads04, .ads05, .ads06, .ads07, .ads08, .ads09, .ads1, .ads10, .ads1000x100, .ads11, .ads12, .ads120_600, .ads120_600-widget, .ads120_80, .ads120x, .ads123, .ads125, .ads125-widget, .ads13, .ads14, .ads15, .ads160, .ads160-600, .ads160_600-widget, .ads160x600, .ads180x150, .ads1_250, .ads1_label, .ads24Block, .ads250, .ads250-250, .ads250_96, .ads3, .ads300, .ads300-200, .ads300-250, .ads300250, .ads300_250, .ads300_250-widget, .ads300_600-widget, .ads300box, .ads300n, .ads300nb, .ads300x, .ads300x100, .ads300x250, .ads300x250-thumb, .ads315, .ads320x100, .ads324-wrapper, .ads324-wrapper2ads, .ads336_280, .ads336x280, .ads4, .ads460, .ads460_home, .ads468, .ads468x60, .ads486x100, .ads486x100-1, .ads598x98, .ads5blocks, .ads667x100, .ads720x90, .ads728, .ads728_90, .ads728x90, .ads728x90-1, .ads728x90-thumb, .ads970, .adsArea, .adsBelowHeadingNormal, .adsBlock, .adsBot, .adsBottom, .adsBox, .adsBoxTop, .adsByTJ, .adsCap, .adsCategoryIcon, .adsCategoryTitleLink, .adsCell, .adsCombo02_1, .adsCombo02_2, .adsCombo02_3, .adsCombo02_4, .adsCombo02_5, .adsCombo02_6, .adsCombo02_7, .adsConfig, .adsCont, .adsDef, .adsDetailsPage, .adsDisclaimer, .adsDiv, .adsFixed, .adsFull, .adsHeader, .adsHeaderFlog, .adsHeading, .adsImages, .adsInner, .adsInsideResults_v3, .adsLabel, .adsLibrary, .adsLine, .adsMPU, .adsMiddle, .adsOuter, .adsOverPrimary, .adsPlaceHolder, .adsRectangleMedium, .adsRight, .adsRow, .adsSpace300x250, .adsSpace300x600, .adsSpace650x100, .adsSpacing, .adsTableBlox, .adsTag, .adsText, .adsTextHouse, .adsThema, .adsTop, .adsTopBanner, .adsTopCont, .adsTower2, .adsTowerWrap, .adsWidget, .adsWithUs, .adsWrap, .adsYN, .ads_1, .ads_120x60, .ads_120x60_index, .ads_125_square, .ads_160, .ads_180, .ads_2, .ads_3, .ads_300, .ads_300250_wrapper, .ads_300x100, .ads_300x239, .ads_300x250, .ads_300x600, .ads_305, .ads_320, .ads_320_100, .ads_330, .ads_337x280, .ads_350, .ads_3col, .ads_4, .ads_460up, .ads_468, .ads_468x60, .ads_672, .ads_728, .ads_728x90, .ads_ad_box, .ads_ad_box2, .ads_admeld, .ads_adsense1, .ads_after, .ads_after_more, .ads_amazon, .ads_amazon_outer, .ads_area, .ads_article, .ads_banner, .ads_banner_between, .ads_banner_between_string, .ads_banniere, .ads_bar, .ads_before, .ads_bg, .ads_big, .ads_big-half, .ads_big_right, .ads_big_right_code, .ads_bigrec, .ads_block, .ads_block250, .ads_border, .ads_box, .ads_box_headline, .ads_brace, .ads_by, .ads_by_tico, .ads_catDiv, .ads_catDivRight, .ads_center, .ads_code, .ads_column, .ads_container, .ads_container_top, .ads_content, .ads_der, .ads_disc_anchor, .ads_disc_leader, .ads_disc_lwr_square, .ads_disc_rectangle, .ads_disc_skyscraper, .ads_disc_square, .ads_div, .ads_entrymore, .ads_folat_left, .ads_foot, .ads_footer, .ads_footerad, .ads_frame_wrapper, .ads_google, .ads_h, .ads_header, .ads_header_bottom, .ads_holder, .ads_horizontal, .ads_infoBtns, .ads_inside2, .ads_item, .ads_layout_sky, .ads_lb, .ads_leader, .ads_leaderboard, .ads_left, .ads_linkb_728, .ads_loc_bottom, .ads_loc_side, .ads_lr_wrapper, .ads_lr_wrapper2, .ads_main, .ads_main_hp, .ads_medium, .ads_medium_rectangle, .ads_medrect, .ads_middle, .ads_middle_container, .ads_mpu, .ads_mpu_small, .ads_obrazek, .ads_outer, .ads_outline, .ads_post, .ads_post_end, .ads_post_end_code, .ads_post_start, .ads_post_start_code, .ads_qc1, .ads_qc2, .ads_r, .ads_rectangle, .ads_rem, .ads_remove, .ads_right, .ads_rightbar_top, .ads_sc_bl, .ads_sc_bl_i, .ads_sc_ls_i, .ads_sc_tb, .ads_sc_tl_i, .ads_sep, .ads_show_if, .ads_side, .ads_sideba, .ads_sidebar, .ads_sidebar_360, .ads_sidebar_360_b, .ads_singlepost, .ads_slice, .ads_small_rectangle, .ads_space_long, .ads_spacer, .ads_square, .ads_takeover, .ads_text, .ads_ticker_main, .ads_title, .ads_top, .ads_top_banner, .ads_top_both, .ads_top_promo, .ads_topbanner, .ads_topic_300, .ads_topic_after, .ads_topleft, .ads_topright, .ads_tower, .ads_tr, .ads_under_fileinfo, .ads_under_player, .ads_up, .ads_up_big2, .ads_upper_right_wrap, .ads_verticalSpace, .ads_vtlLink, .ads_vtlList, .ads_wide, .ads_widesky, .ads_without_height, .ads_wrapper, .ads_wrapperads_top, .adsafp, .adsanity-group, .adsanity-single, .adsarea, .adsbantop, .adsbar, .adsbg300, .adsblock, .adsblockvert, .adsbnr, .adsbody, .adsborder, .adsboth, .adsbottom, .adsbottombox, .adsbox, .adsbox-square, .adsboxBtn, .adsbox_300x250, .adsboxitem, .adsbttmpg, .adsbycircumventioncentral, .adsbygoogle, .adsbygoogle-box, .adsbygoogle2, .adsbysinodia, .adsbyyahoo, .adsc, .adscaleAdvert, .adscaleP6_canvas, .adscaleTop, .adscatalog, .adsclick, .adscontainer, .adscontent250, .adscontentcenter, .adscreen, .adsd_shift100, .adsdisplaygames, .adsdiv, .adsection_a2, .adsection_c2, .adsection_c3, .adsence-domain, .adsens, .adsense-250, .adsense-300x256-widget, .adsense-300x256-widget-2, .adsense-336, .adsense-468, .adsense-ad, .adsense-ads, .adsense-afterpost, .adsense-attribution, .adsense-block, .adsense-category, .adsense-category-bottom, .adsense-center, .adsense-code, .adsense-container, .adsense-content, .adsense-div, .adsense-float, .adsense-googleAds, .adsense-header, .adsense-heading, .adsense-image-detail, .adsense-left, .adsense-links, .adsense-links2, .adsense-midtext, .adsense-mod-border, .adsense-module, .adsense-overlay, .adsense-post, .adsense-review, .adsense-reviews-float, .adsense-right, .adsense-slot, .adsense-square, .adsense-sticky-slide, .adsense-title, .adsense-top, .adsense-top-bar, .adsense-topics-detail, .adsense-unit, .adsense-wide-background, .adsense-widget, .adsense-widget-horizontal, .adsense1, .adsense160x600, .adsense250, .adsense3, .adsense300, .adsense300_top, .adsense728, .adsense728x90, .adsenseAds, .adsenseBlock, .adsenseContainer, .adsenseGreenBox, .adsenseInPost, .adsenseLargeRectangle, .adsenseList, .adsenseRow, .adsenseSky, .adsenseWrapper, .adsense_200, .adsense_200x200, .adsense_336_280, .adsense_728x15_center, .adsense_afc_related_art, .adsense_bdc_v2, .adsense_block, .adsense_bottom, .adsense_box01, .adsense_container, .adsense_div_wrapper, .adsense_full_width, .adsense_leader, .adsense_left_lu, .adsense_mainbox01, .adsense_managed, .adsense_managed_, .adsense_media, .adsense_menu, .adsense_mpu, .adsense_rectangle, .adsense_results, .adsense_right, .adsense_sidebar, .adsense_single, .adsense_small_square, .adsense_top, .adsense_top_ad, .adsense_top_lu, .adsense_unit, .adsense_x88, .adsensebig, .adsenseblock_bottom, .adsenseblock_top, .adsensefloat, .adsenseformat, .adsenseframe, .adsenseleaderboard, .adsenselr, .adsensem_widget, .adsensemainpage, .adsensesky, .adsensesq, .adsensex336, .adsenvelope, .adsep, .adseparator, .adserve_728, .adserver_zone, .adserverad, .adserving, .adset, .adsforums, .adsghori, .adsgrd, .adsgvert, .adsh, .adshl, .adshome, .adshowcase, .adshp, .adside, .adside-box-index, .adside-box-single, .adsidebar, .adsidebox, .adsider, .adsincs2, .adsinfo, .adsingle, .adsitem, .adsize728, .adsizer, .adsleaderboard, .adsleaderboardbox, .adsleft, .adsleftblock, .adslibraryArticle, .adslider, .adslink, .adslist, .adslogan, .adslot, .adslot-banner, .adslot-billboard, .adslot-mpu, .adslot-rectangle, .adslot-widget, .adslot_1, .adslot_300, .adslot_728, .adslot_blurred, .adslot_bot_300x250, .adslot_side1, .adslothead, .adslotleft, .adslotright, .adslug, .adslx-bottom2015, .adslx2015, .adsmall, .adsmaller, .adsmalltext, .adsmanag, .adsmbody, .adsmedrect, .adsmedrectright, .adsmessage, .adsnippet_widget, .adsns, .adsonar-after, .adsonofftrigger, .adsoptimal-slot, .adspace, .adspace-300x600, .adspace-336x280, .adspace-728x90, .adspace-MR, .adspace-leaderboard, .adspace-mpu, .adspace-widget, .adspace1, .adspace180, .adspace2, .adspace728x90, .adspace_2, .adspace_bottom, .adspace_buysell, .adspace_rotate, .adspace_skyscraper, .adspace_top, .adspacer, .adspan, .adspanel, .adspecial390, .adspeed, .adsplash-160x600, .adsplat, .adsponsor, .adspost, .adspot, .adspot-title, .adspot1, .adspot200x90, .adspot468x60, .adspot728x90, .adspotGrey, .adspot_468x60, .adspot_728x90, .adsrecnode, .adsskyscraper, .adssmall, .adssquare, .adssquare2, .adstext, .adstextpad, .adstipt, .adstitle, .adstop, .adstory, .adstrip, .adstxt, .adstyle, .adsupperugo, .adsupperugo_txt, .adswidget, .adswitch, .adsxpls, .adsystem_ad, .adszone, .adt-300x250, .adt-300x600, .adt-728x90, .adtab, .adtable, .adtag, .adtech, .adtech-ad-widget, .adtech-banner, .adtech-boxad, .adtech_wrapper, .adtext_gray, .adtext_horizontal, .adtext_onwhite, .adtext_vertical, .adtext_white, .adtextleft, .adtextright, .adtexts, .adtile, .adtips, .adtips1, .adtoggle, .adtop, .adtop-border, .adtops, .adtower, .adtravel, .adtv_300_250, .adtxt, .adtxtlinks, .adult-adv, .adunit, .adunit-300-250, .adunit-active, .adunit-middle, .adunit-parent, .adunit-side, .adunit125, .adunit160, .adunit300x250, .adunit468, .adunit_210x509, .adunit_300x100, .adunit_300x250, .adunit_300x600, .adunit_607x110, .adunit_728x90, .adunit_content, .adunit_footer, .adunit_leaderboard, .adunit_maincol_right, .adunit_rectangle, .adv-160, .adv-200-200, .adv-250-250, .adv-300, .adv-300-1, .adv-300-250, .adv-300x250, .adv-300x250-generic, .adv-336-280, .adv-4, .adv-468-60, .adv-700, .adv-728, .adv-970, .adv-980x60, .adv-ad, .adv-background, .adv-banner, .adv-block, .adv-border, .adv-bottom, .adv-box, .adv-box-wrapper, .adv-click, .adv-comment--opened, .adv-comments, .adv-cont, .adv-cont1, .adv-container, .adv-dvb, .adv-format-1, .adv-google, .adv-halfpage, .adv-in-body, .adv-inset, .adv-intext, .adv-intext-label, .adv-key, .adv-label, .adv-leaderboard, .adv-leaderboard-banner, .adv-lshaped-wrapper, .adv-mid-rect, .adv-mpu, .adv-mpu-shoulder, .adv-outer, .adv-p, .adv-right, .adv-right-300, .adv-search-ad, .adv-sidebar, .adv-slide-block-wrapper, .adv-square-banner, .adv-squarebox-banner, .adv-teaser-divider, .adv-top, .adv-top-container, .adv-top-page, .adv-under-video, .adv-videoad, .adv-x61, .adv200, .adv200_border, .adv250, .adv300, .adv300-250, .adv300-250-2, .adv300-70, .adv300left, .adv300x100, .adv300x250, .adv300x70, .adv336, .adv350, .adv460x60, .adv468, .adv468x90, .adv728, .advBottom, .advBottomHome, .advBox, .advDesktop300x250, .advImagesbox, .advLB_PageMiddle, .advLeaderboard, .advSquare, .advText, .advTicker, .advVideobox, .advWrappers, .adv_1, .adv_120, .adv_120_600, .adv_120x240, .adv_120x600, .adv_160_600, .adv_160x600, .adv_2, .adv_250_250, .adv_300, .adv_300_300, .adv_300_top, .adv_300x250, .adv_336_280, .adv_468_60, .adv_630, .adv_728_90, .adv_728x90, .adv_90, .adv_PageTop, .adv__container--300x250, .adv__container--728x90, .adv__text, .adv_aff, .adv_amazon_single, .adv_banner, .adv_banner_hor, .adv_bg, .adv_blocker, .adv_box, .adv_box_narrow, .adv_cnt, .adv_code, .adv_default_box_container, .adv_flash, .adv_floater_left, .adv_floater_right, .adv_headerleft, .adv_headerright, .adv_hed, .adv_here, .adv_in_body_a, .adv_info_text, .adv_leaderboard, .adv_left, .adv_link, .adv_main_middle, .adv_main_middle_wrapper, .adv_main_right_down, .adv_main_right_down_wrapper, .adv_medium_rectangle, .adv_message, .adv_page_blocker_overlay, .adv_panel, .adv_pointer_home, .adv_pointer_section, .adv_right, .adv_sd_dx, .adv_side1, .adv_side2, .adv_sidebar, .adv_sidebar_300x250, .adv_standard_d, .adv_title, .adv_top, .adv_txt, .adv_under_menu, .adv_underpost, .adv_x_1, .adv_x_2, .advads-5, .advads_widget, .advart, .advbanner_300x250, .advbanner_300x600, .advbanner_970x90, .advbig, .advbptxt, .adver, .adver-left, .adver-text, .adverTag, .adverTxt, .adver_bot, .adver_cont_below, .adverdown, .adverhrz, .adverserve145, .adverstisement_right, .advert--background, .advert--banner-wrap, .advert--leaderboard, .advert--mpu, .advert--mpu--rhs, .advert--transition, .advert--vc, .advert--vc__wrapper, .advert-100, .advert-120x90, .advert-160x600, .advert-300, .advert-300-side, .advert-300x100-side, .advert-300x250-container, .advert-728, .advert-728-90, .advert-728x90, .advert-760, .advert-arch-top, .advert-article-bottom, .advert-banner, .advert-banner-holder, .advert-bannerad, .advert-bg-250, .advert-block, .advert-bloggrey, .advert-body-not-home, .advert-bot-box, .advert-box, .advert-bronze, .advert-bronze-btm, .advert-btm, .advert-center, .advert-center_468x60, .advert-col, .advert-col-center, .advert-competitions, .advert-container, .advert-content, .advert-content-item, .advert-detail, .advert-featured, .advert-footer, .advert-full-raw, .advert-gold, .advert-group, .advert-head, .advert-header-728, .advert-home-380x120, .advert-horizontal, .advert-iab-300-250, .advert-iab-468-60, .advert-image, .advert-info, .advert-label, .advert-leaderboard, .advert-leaderboard2, .advert-loader, .advert-lower-right, .advert-mini, .advert-mpu, .advert-mrec, .advert-note, .advert-overlay, .advert-pane, .advert-right, .advert-section, .advert-sidebar, .advert-silver, .advert-sky, .advert-skyscraper, .advert-stub, .advert-text, .advert-three, .advert-tile, .advert-title, .advert-top, .advert-top-footer, .advert-txt, .advert-under-hedaer, .advert-unit, .advert-wide, .advert-words, .advert-wrap, .advert-wrap1, .advert-wrap2, .advert-wrapper, .advert-wrapper_rectangle_aside, .advert1, .advert120, .advert1Banner, .advert2, .advert300, .advert300-home, .advert300x100, .advert300x250, .advert300x300, .advert300x440, .advert300x600, .advert350ih, .advert4, .advert5, .advert728_90, .advert728x90, .advert8, .advertAreaFrame, .advertBanner, .advertBar, .advertBlock, .advertBottom, .advertBox, .advertCaption, .advertColumn, .advertCont, .advertContainer, .advertContent, .advertDownload, .advertFullBanner, .advertGenerator, .advertHeadline, .advertIslandWrapper, .advertLink, .advertLink1, .advertMiddle, .advertRight, .advertSideBar, .advertSign, .advertSuperBanner, .advertText, .advertTh, .advertThInnBg, .advertTitleSky, .advertWrapper, .advert_300x250, .advert_336, .advert_468x60, .advert__container, .advert__mpu, .advert__tagline, .advert_area, .advert_back_160x600, .advert_back_300x250, .advert_back_300xXXX, .advert_banner, .advert_block, .advert_box, .advert_caption, .advert_cont, .advert_container, .advert_div, .advert_djad, .advert_google_content, .advert_google_title, .advert_header, .advert_home_300, .advert_img, .advert_in_post, .advert_label, .advert_leaderboard, .advert_line, .advert_list, .advert_main, .advert_main_bottom, .advert_mpu, .advert_mpu_body_hdr, .advert_nav, .advert_note, .advert_rectangle_aside, .advert_small, .advert_societe_general, .advert_source, .advert_span, .advert_surr, .advert_top, .advert_txt, .advert_wrapper, .advertasingtxt, .advertbar, .advertbox, .advertheader-red, .adverthome, .advertis-left, .advertis-right, .advertise-box, .advertise-here, .advertise-homestrip, .advertise-horz, .advertise-info, .advertise-inquiry, .advertise-leaderboard, .advertise-link, .advertise-link-post-bottom, .advertise-list, .advertise-small, .advertise-square, .advertise-top, .advertise-vert, .advertiseBlack, .advertiseContainer, .advertiseHere, .advertiseLabel234x60, .advertiseLabel300x250, .advertiseText, .advertise_ads, .advertise_box, .advertise_box1, .advertise_box4, .advertise_here, .advertise_link, .advertise_link_sidebar, .advertise_links, .advertise_sec, .advertise_txt, .advertise_verRight, .advertisebtn, .advertisedBy, .advertisement-1, .advertisement-160-600, .advertisement-2, .advertisement-234-60, .advertisement-250, .advertisement-300, .advertisement-300-250, .advertisement-300x250, .advertisement-300x600, .advertisement-728-90, .advertisement-728x90, .advertisement-750-60, .advertisement-BottomRight, .advertisement-after, .advertisement-background, .advertisement-banner, .advertisement-before, .advertisement-bkg, .advertisement-block, .advertisement-bottom, .advertisement-caption, .advertisement-cell, .advertisement-comment, .advertisement-container, .advertisement-content, .advertisement-copy, .advertisement-dashed, .advertisement-header, .advertisement-information-link, .advertisement-label, .advertisement-label-up-white, .advertisement-layout, .advertisement-leader-board, .advertisement-leader-board-second, .advertisement-leaderboard, .advertisement-nav, .advertisement-other, .advertisement-placeholder, .advertisement-position1, .advertisement-right, .advertisement-right-rail, .advertisement-sidebar, .advertisement-space, .advertisement-sponsor, .advertisement-swimlane, .advertisement-tag, .advertisement-text, .advertisement-top, .advertisement-txt, .advertisement-wrapper, .advertisement1, .advertisement300x250, .advertisement468, .advertisementBackground, .advertisementBanner, .advertisementBannerVertical, .advertisementBar, .advertisementBlock, .advertisementBox, .advertisementCenterer, .advertisementColumnGroup, .advertisementContainer, .advertisementFull, .advertisementGif, .advertisementHeader, .advertisementImg, .advertisementLabel, .advertisementLabelFooter, .advertisementOutsider, .advertisementPanel, .advertisementReloadable, .advertisementRotate, .advertisementSmall, .advertisementText, .advertisementTop, .advertisement_160x600, .advertisement_300x250, .advertisement__label, .advertisement_article_center_bottom_computer, .advertisement_article_center_middle1_computer, .advertisement_article_center_middle4_computer, .advertisement_article_center_middle6_computer, .advertisement_article_center_top_computer, .advertisement_article_right_middle2_computer, .advertisement_article_right_top_computer, .advertisement_below_news_article, .advertisement_block_234_60, .advertisement_block_468_60, .advertisement_box, .advertisement_btm, .advertisement_caption, .advertisement_container, .advertisement_flag, .advertisement_flag_sky, .advertisement_g, .advertisement_header, .advertisement_horizontal, .advertisement_main_center_bottom_computer, .advertisement_main_right_middle2_computer, .advertisement_main_right_top_computer, .advertisement_post, .advertisement_river, .advertisement_sky, .advertisement_top, .advertisement_watchFooter, .advertisementonblue, .advertisementonwhite, .advertisements-link, .advertisements-right, .advertisementsOutterDiv, .advertisements_contain, .advertisementsubtitle, .advertiser, .advertiser-links, .advertisesingle, .advertisespace_div, .advertising-aside-top, .advertising-banner, .advertising-block, .advertising-box-top-teaser, .advertising-content, .advertising-fixed, .advertising-header, .advertising-inner, .advertising-leaderboard, .advertising-local-links, .advertising-lrec, .advertising-mention, .advertising-srec, .advertising-top, .advertising-top-box, .advertising-top-category, .advertising160, .advertising2, .advertising300_home, .advertising300x250, .advertising728, .advertising728_3, .advertisingBanner, .advertisingBlock, .advertisingBlocks, .advertisingLegend, .advertisingLrec, .advertisingSlide, .advertisingTable, .advertising_300x250, .advertising_banner, .advertising_block, .advertising_bottom_box, .advertising_box_bg, .advertising_hibu_lef, .advertising_hibu_mid, .advertising_hibu_rig, .advertising_images, .advertising_widget, .advertisingarea, .advertisingarea-homepage, .advertisingimage, .advertisingimage-extended, .advertisingimageextended, .advertisingimageextended-link, .advertisment, .advertisment-banner, .advertisment-label, .advertisment-left-panal, .advertisment-module, .advertisment-rth, .advertisment-top, .advertismentBox, .advertismentContainer, .advertismentContent, .advertismentText, .advertisment_300x250, .advertisment_bar, .advertisment_caption, .advertisment_full, .advertisment_two, .advertize, .advertize_here, .advertlabel, .advertleft, .advertnotice, .advertorial { display: none !important; } </style><style type="text/css">.advertorial-2, .advertorial-promo-box, .advertorial-wrapper, .advertorial2, .advertorial_728x90, .advertorial_red, .advertorialitem, .advertorialtitle, .advertorialview, .advertorialwidget, .advertplay, .adverts, .adverts-125, .adverts-inline, .adverts_RHS, .advertspace, .adverttext, .adverttop, .advfrm, .advg468, .advhere, .advimg160600, .advimg300250, .advoice, .advr, .advr-wrapper, .advr_top, .advr_txtcss, .advrectangle, .advslideshow, .advspot, .advt, .advt-banner-3, .advt-block, .advt-box, .advt-sec, .advt-text, .advt300, .advt720, .advtBlock, .advt_160x600, .advt_468by60px, .advt_indieclick, .advt_single, .advt_title, .advt_widget, .advtext, .advtimg, .advtitle, .advtop, .advtop-leaderbord, .advttopleft, .adwhitespace, .adwide, .adwidget, .adwolf-holder, .adword-box, .adword-structure, .adword-text, .adword-title, .adword1, .adwordListings, .adwords, .adwords-container, .adwordsHeader, .adwords_in_content, .adwrap, .adwrap-widget, .adwrapper-lrec, .adwrapper1, .adwrapper948, .adx-300x250-container, .adx-300x600-container, .adx-wrapper, .adxli, .adz2, .adz728x90, .adzone, .adzone-footer, .adzone-preview, .adzone-sidebar, .adzone_ad_5, .adzone_ad_6, .adzone_ad_7, .adzone_ad_8, .adzone_ad_9, .af-block-ad-wrapper, .afc-box, .afffix-custom-ad, .affiliate-ad, .affiliate-footer, .affiliate-link, .affiliate-mrec-iframe, .affiliate-sidebar, .affiliate-strip, .affiliateAdvertText, .affiliate_ad, .affiliate_header_ads, .affiliate_header_ads_container, .affiliates-sidebar, .affiliation728x90, .affinityAdHeader, .afns-ad-sponsor-logo, .afsAdvertising, .afsAdvertisingBottom, .afs_ads, .aft-top-728x90, .aftContentAdLeft, .aftContentAdRight, .after-first-post-ad-1, .after-post-ad, .after_ad, .after_comments_ads, .after_post_ad, .afterpostadbox, .agi-adsaleslinks, .agi-adtop, .aisle-ad, .aisoad, .ajaxads, .al-wss-ad, .alb-content-ad, .alignads, .allpages_ad_bottom, .allpages_ad_top, .alt-ad-box, .alt_ad, .alternatives_ad, .am-adContainer, .am-articleItem--bodyAds, .amAdvert, .am_ads, .amp-ad-container, .amsSparkleAdWrapper, .anchor-ad-wrapper, .anchorAd, .annonce_textads, .annons_themeBlock, .annonstext, .another_text_ad, .answer_ad_content, .aol-knot-fullscreen-right-ad, .aol-twist-flyout-ad, .aolSponsoredLinks, .aopsadvert, .ap_str_ad, .apiAdMarkerAbove, .apiAds, .apiButtonAd, .app-advertisements, .app_ad_unit, .app_advertising_skyscraper, .apxContentAd, .archive-ad, .archive-ads, .area1_2_ad1, .area5_ad, .areaAd, .area_ad03, .area_ad07, .area_ad09, .aroundAdUnit, .artAd, .artAdInner, .art_ad_aside, .art_ad_top, .art_ads, .art_aisde_ads, .art_new_ads_468_60, .artcl_promo_ad, .article-ad, .article-ad-300x250, .article-ad-align-left, .article-ad-blk, .article-ad-bottom, .article-ad-box, .article-ad-cont, .article-ad-left, .article-ad-main, .article-ad-primary, .article-ads, .article-advert, .article-advert-container, .article-aside-ad, .article-content-adwrap, .article-footer-ad-container, .article-footer__ad, .article-footer__ads, .article-google-adsense, .article-header-ad, .article-inline-ad, .article-news-videoad, .article-sidebar__advert, .article-v2-rail__advert, .articleAd, .articleAd300x250, .articleAdBlade, .articleAdSlot2, .articleAdTop, .articleAdTopRight, .articleAds, .articleAdsL, .articleAdvert, .articleEmbeddedAdBox, .articleFooterAd, .articleHeadAdRow, .articlePage3rdPartyContentStrip, .articleTopAd, .article_ad, .article_ad250, .article_ad_container2, .article_adbox, .article_ads_banner, .article_bottom-ads, .article_bottom_ad, .article_google-ad, .article_google_ads, .article_inline_ad, .article_inner_ad, .article_list_in_ad, .article_middle_ad, .article_mpu_box, .article_page_ads_bottom, .article_sponsored_links, .article_tower_ad, .articlead, .articleads, .articlebodyad, .articlepage_ads_1, .articlepage_ads_top, .artist-ad-wrapper, .as-admedia, .as_ad, .aseadn, .aside-ad, .aside-ad-wrapper, .aside-ads, .asideAd, .aside_AD01, .aside_AD02, .aside_AD06, .aside_AD08, .aside_AD09, .aside_banner_ads, .aside_google_ads, .associated-ads, .async-ad-container, .atf-ad-medRect, .atf-ad-medrec, .atfAds, .atf_ad_box, .attachment-advert_home, .attachment-dm-advert-bronze, .attachment-dm-advert-gold, .attachment-dm-advert-silver, .attachment-sidebar-ad, .attachment-sidebarAd, .attachment-sidebar_ad, .attachment-squareAd, .attachment-weather-header-ad, .auction-nudge, .autoshow-top-ad, .aux-ad-widget-1, .aux-ad-widget-2, .avertissement-download, .b-ad, .b-ad-footerBanner, .b-ad-topBanner, .b-ads728, .b-ads_300, .b-ads_gpt, .b-ads_iframe, .b-adsuniversal-wrap, .b-adv-art, .b-adv-mobi, .b-advert, .b-advert__grid, .b-aside-ads, .b-astro-sponsored-links_horizontal, .b-astro-sponsored-links_vertical, .b5-ad-pushdown, .b5_widget_skyscraper_ad, .b5ad_bigbox, .b5ad_skyscraper, .b_ad, .b_ads, .b_ads_cont, .b_ads_r, .b_ads_top, .back300ad, .backgroundAd, .badge-gag-ads-container, .bads300, .badxcn, .bam-dcRefreshableAd, .ban-720-container, .ban300side, .ban420x200, .ban420x260, .ban680x450, .ban728, .ban980x90, .bank-rate-ad, .banmanad, .banner-125, .banner-300, .banner-300x250, .banner-300x600, .banner-468, .banner-468-60, .banner-468x60, .banner-728, .banner-728x90, .banner-950x50, .banner-ad, .banner-ad-300x250, .banner-ad-container, .banner-ad-footer, .banner-ad-row, .banner-ad-space, .banner-ad-wrapper, .banner-ads, .banner-ads-300x250, .banner-ads-sidebar, .banner-adsense, .banner-adv, .banner-advert, .banner-adverts, .banner-buysellads, .banner-paid-ad-label, .banner-rectangleMedium, .banner-sidebar-300x250, .banner-top-ads, .banner-top-banner-728x90, .banner1-728x90, .banner120x600, .banner125x125, .banner160, .banner160x600, .banner250_250, .banner300, .banner300_250, .banner300by250, .banner300x84, .banner336, .banner336x280, .banner350, .banner468, .banner468by60, .banner728, .banner728-ad, .banner728-container, .banner728x90, .bannerADV, .bannerAd, .bannerAd3, .bannerAd300x250, .bannerAdContainer, .bannerAdLeaderboard, .bannerAdRectangle, .bannerAdSearch, .bannerAdSidebar, .bannerAdTower, .bannerAdWrap, .bannerAdWrapper300x250, .bannerAdWrapper730x86, .bannerAd_rdr, .bannerAds, .bannerAdvert, .bannerAside, .bannerGAd, .bannerRightAd, .bannerTopAdLeft, .bannerTopAdRight, .bannerWrapAdwords, .banner_160x600, .banner_234x90, .banner_250x250, .banner_300_250, .banner_300x250, .banner_300x250_2, .banner_300x250_3, .banner_468_60, .banner_468x60, .banner_728_90, .banner_728x90, .banner_ad, .banner_ad-728x90, .banner_ad_233x90, .banner_ad_300x250, .banner_ad_728x90, .banner_ad_footer, .banner_ad_full, .banner_ad_leaderboard, .banner_ads, .banner_ads1, .banner_ads_300x250, .banner_ads_home, .banner_adv, .banner_altervista_300X250, .banner_altervista_728X90, .banner_mpu_integrated, .banner_reklam, .banner_reklam2, .banner_slot, .bannerad, .bannerad-125tower, .bannerad-468x60, .bannerad3, .banneradbottomholder, .banneradd, .bannerads, .banneradv, .bannerandads, .bannergoogle, .bannergroup-ads, .banneritem-ads, .banneritem_ad, .bannerplace728, .bar_ad, .barkerAd, .barstool_ad_floater, .base-ad-mpu, .base_ad, .base_printer_widgets_AdBreak, .bb-ad-mrec, .bb-adv-160x600, .bb-adv-300x250, .bb-md-adv7, .bbccom-advert, .bbccom_advert, .bbsTopAd, .bcom_ad, .bean-advertisment, .bean-bag-ad, .bean-dfp-ad-unit, .beauty_ads, .before-comment-ad, .belowNavAds, .below_game_ad, .below_player_ad, .belowthread_advert, .belowthread_advert_container, .belt_ad, .bet_AdBlock, .bets-ads, .between_page_ads, .bex_ad, .bg-ad-link, .bg-ad-top, .bg-ads, .bgAdBlue, .bgadgray10px, .bgcolor_ad, .bgnavad, .big-ad, .big-ads, .big-box-ad, .big-right-ad, .bigAd, .bigAdContainer, .bigAds, .bigAdvBanner, .bigBoxAdArea, .bigCubeAd, .big_ad, .big_ads, .big_center_ad, .big_rectangle_page_ad, .bigad, .bigad1, .bigad2, .bigadleft, .bigadright, .bigads, .bigadtxt1, .bigbox-ad, .bigbox_ad, .bigboxad, .billboard-ad, .billboard300x250, .billboardAd, .billboard__advert, .billboard_ad, .bing-ads-wrapper, .biz-ad, .biz-ads, .biz-adtext, .biz-details-ad, .biz-list-ad, .bizCardAd, .bizDetailAds, .bkg-ad-browse, .bl_adv_right, .blacboard-ads-container, .blk_advert, .blocAdInfo, .bloc_ads_notice, .bloc_adsense_acc, .block--ad-superleaderboard, .block--ads, .block--bean-artadocean-splitter, .block--bean-artadocean-text-link-1, .block--bean-artadocean-text-link-2, .block--bean-artadocean300x250-1, .block--bean-artadocean300x250-3, .block--bean-artadocean300x250-6, .block--simpleads, .block--views-premium-ad-slideshow-block, .block-ad, .block-ad-header, .block-ad-leaderboard, .block-ad-masthead, .block-ad-middle, .block-ad-mpu, .block-ad-wrapper, .block-ad300, .block-ad_injector, .block-ad_tag, .block-admanager, .block-ads, .block-ads-bottom, .block-ads-eplanning, .block-ads-eplanning-300x250top-general, .block-ads-eplanning-300x600, .block-ads-home, .block-ads-top, .block-ads1, .block-ads2, .block-ads3, .block-ads_top, .block-adsense, .block-adsense-managed, .block-adsense_managed, .block-adspace-full, .block-adv, .block-advertisement, .block-advertising, .block-adzerk, .block-altads, .block-ami-ads, .block-bean-adocean, .block-bf_ads, .block-bg-advertisement, .block-bg-advertisement-region-1, .block-boxes-ad, .block-boxes-ga_ad, .block-deca_advertising, .block-dennis-adsense-afc, .block-display-ads, .block-doubleclick_ads, .block-ec_ads, .block-eg_adproxy, .block-fan-ad, .block-fc_ads, .block-fcc-advertising, .block-fcc-advertising-first-sidebar-ad, .block-featured-sponsors, .block-first-sidebar-ad, .block-gc_ad, .block-gg_ads, .block-google-admanager, .block-google-admanager-dfp, .block-google_admanager, .block-google_admanager2, .block-hcm-ads, .block-hcm_ads, .block-inner-adds, .block-maniad, .block-module-ad, .block-module-ad-300x250, .block-module-ad-300x600, .block-nmadition, .block-ohtdisplayad, .block-openads, .block-openadstream, .block-openx, .block-pm_doubleclick, .block-reklama, .block-simpleads, .block-skyscraper-ad, .block-sn-ad-blog-wrapper, .block-sponsor, .block-sponsored-links, .block-thirdage-ads, .block-vh-adjuggler, .block-wtg_adtech, .block-yt-ads, .block-zagat_ads, .block1--ads, .blockAd, .blockAd300x97, .blockAds, .blockAdvertise, .block_ad, .block_ad_floating_bar, .block_ad_middle, .block_ad_sb_text, .block_ad_sb_text2, .block_ad_sponsored_links, .block_ad_sponsored_links-wrapper, .block_ad_sponsored_links_localized, .block_ad_sponsored_links_localized-wrapper, .block_ad_top, .block_ads, .block_adslot, .block_adv, .block_advert, .blockad, .blocked-ads, .blockid_google-adsense-block, .blockrightsmallads, .blocsponsor, .blog-ad, .blog-ad-leader-inner, .blog-ads, .blog-ads-container, .blog-ads-top, .blog-advertisement, .blog-view-ads, .blog2AdIntegrated, .blogAd, .blogAdvertisement, .blogArtAd, .blogBigAd, .blog_ad, .blog_ad_continue, .blog_divider_ad, .blogads, .blogads-sb-home, .blogroll-ad-img, .blogs_2_square_ad, .blox3featuredAd, .blue-ad, .blxAdopsPlacement, .bmg-sidebar-ads-125, .bmg-sidebar-ads-300, .bn_advert, .bn_textads, .bnr_ad, .bo-top-ad-bottom, .bo-top-left-ad, .bo-top-right-ad, .bodaciousad, .body-ads, .body-adzone, .bodyAd, .body_ad, .body_sponsoredresults_bottom, .body_sponsoredresults_middle, .body_sponsoredresults_top, .body_width_ad, .bodyads, .bodyads2, .bodybannerad, .bodyrectanglead, .bomAd, .bonnier-ads, .bonnier-ads-ad-bottom, .bonnier-ads-ad-top, .bookad, .bookseller-header-advt, .booster-ad, .bostad, .bot-728x90-ad, .bot-affiliate, .botAd, .botRectAd, .bot_ad, .bot_ads, .botad2, .bottom-ad, .bottom-ad-banner, .bottom-ad-box, .bottom-ad-container, .bottom-ad-fr, .bottom-ad-large, .bottom-ad-placeholder, .bottom-ad-tagline, .bottom-ad-wrapper, .bottom-ad2, .bottom-ads, .bottom-ads-wrapper, .bottom-ads728, .bottom-banner-ad, .bottom-center-adverts, .bottom-game-ad, .bottom-large-google-ad, .bottom-leaderboard-adslot, .bottom-left-ad, .bottom-main-adsense, .bottom-mpu-ad, .bottom-right-advert, .bottom-rightadvtsment, .bottom-slider-ads, .bottom2-adv, .bottomAd, .bottomAdBlock, .bottomAds, .bottomAdsTitle, .bottomAdvTxt, .bottomAdvert, .bottomAdvertisement, .bottomAdvt, .bottomArticleAds, .bottomBannerAd, .bottomBannerAdsSmallBotLeftHolder, .bottomELAd, .bottomFriendsAds, .bottomReviewAd, .bottom_ad, .bottom_ad_block, .bottom_ad_placeholder, .bottom_ad_responsive, .bottom_adbreak, .bottom_ads, .bottom_ads_wrapper_inner, .bottom_adsense, .bottom_advert_728x90, .bottom_advertise, .bottom_banner_ad, .bottom_banner_advert_text, .bottom_bar_ads, .bottom_left_advert, .bottom_right_ad, .bottom_rightad, .bottom_side_ad, .bottom_sponsor, .bottomad, .bottomad-bg, .bottomadarea, .bottomads, .bottomadtop, .bottomadvert, .bottomadwords, .bottombarad, .bottomleader, .bottomleader-ad-wrapper, .bottomrightrailAd, .bottomvidad, .botton_advertisement, .box-ad, .box-ad-a, .box-ad-grey, .box-ad-mr1, .box-ad-unit-j, .box-ad-wsr, .box-ads, .box-ads-small, .box-adsense, .box-adv-300-home, .box-adv-social, .box-advert, .box-advert-sponsored, .box-advertisement, .box-adverts, .box-entry-ad-bottom-single, .box-footer-ad, .box-google-text-ad, .box-radvert, .box-recommend-ad, .box-sidebar-ad, .box-sidebar-ad-125, .box-sidebar-ad-160, .box-sidebar-ad-300, .box1-ad, .boxAd, .boxAdContainer, .boxAdFields, .boxAdMrec, .boxAds, .boxAdsInclude, .boxAdvertisement, .boxOuterAD, .boxSponsor, .box_ad, .box_ad_container, .box_ad_content, .box_ad_horizontal, .box_ad_spacer, .box_ad_wrap, .box_ads, .box_ads728x90_holder, .box_adv, .box_adv1, .box_adv2, .box_adv_728, .box_adv_hp, .box_adv_new, .box_advertising, .box_advertising_info, .box_advertisment_62_border, .box_content_ad, .box_content_ads, .box_publicidad, .box_sidebar-ads, .box_textads, .box_title_ad, .boxad, .boxad1, .boxad120, .boxadcont, .boxads, .boxadv, .boxcontentad, .boxsponsor2, .boxyads, .bps-ad-wrapper, .bps-advertisement, .bps-advertisement-inline-ads, .bps-advertisement-placeholder, .bps-search-chitika-ad, .bq_ad_320x250, .bq_adleaderboard, .bq_rightAd, .br-ad, .br-ad-text, .br-banner-ad, .br-right-rail-ad, .branding-ad-gallery, .branding-ad-wrapper, .breadads, .breadcumbad, .breakad_container, .breakerAd, .breakingNewsModuleSponsor, .breakthrough-ad, .broker-ad, .broker-ads, .broker-ads-center, .brokerad, .browse-ad-container, .browse-banner_ad, .browse-by-make-ad, .browser_boot_ad, .bs-ad, .bsAdvert, .bsa-in-post-ad-125-125, .bsa_ads, .bsa_it_ad, .bt_ad, .btf-ad-medRect, .btfAds, .btm_ad, .btm_ad_container, .btn-ad, .btn-newad, .btn_ad, .budget_ads_1, .budget_ads_2, .budget_ads_3, .budget_ads_bg, .bullet-sponsored-links, .bullet-sponsored-links-gray, .bump-ad, .bunyad-ad, .burstContentAdIndex, .businessads, .busrep_poll_and_ad_container, .button-ad, .button-ads, .buttonAd, .buttonAdSpot, .buttonAds, .button_ad, .button_ads, .button_advert, .buttonad, .buttonad_v2, .buttonadbox, .buttonads, .buySellAdsContainer, .buysellAds, .buysellAdsSmall, .buzzAd, .buzz_ad_block, .buzz_ad_wrap, .bx_ad, .bx_ad_right, .bxad, .bz-ad, .bzads-ic-ad-300-250-600, .c-adunit, .c-adunit--billboard, .c-adunit--first, .c-adunit__container, .c-advert-superbanner, .c-res-ad, .c300x250-advert, .c3_adverts, .cA-adStack, .cA-adStrap, .cColumn-TextAdsBox, .cLeftTextAdUnit, .c_adsky, .c_google_adsense_nxn, .c_ligatus_nxn, .calendarAd, .calloutAd, .can_ad_slug, .canoeAdvertorial, .carbonad, .carbonad-tag, .card--ad, .card-ad, .card-ads, .cards-categorical-list-ad, .care2_adspace, .careerAdviceAd1, .carouselbanner_advert, .carouselbannersad, .cat_context_ad, .catalog_ads, .catalyst-ads, .cate_right_ad, .category-ad, .category-advertorial, .categorySponsorAd, .category__big_game_container_body_games_advertising, .categoryfirstad, .categoryfirstadwrap, .categorypage_ad1, .categorypage_ad2, .catfish_ad, .cb-ad-banner, .cb-ad-container, .cb_ads, .cb_navigation_ad, .cbolaBannerStructure, .cbs-ad, .cbs-ad-unit, .cbs-ad-unit-wrapper, .cbstv_ad_label, .cbzadvert, .cbzadvert_block, .cc-advert, .cct-tempskinad, .cdAdContainer, .cdAdTitle, .cdLanderAd, .cdc-ad, .cde_ads_right_top_300x250, .cdmainlineSearchAdParent, .cdo-ad, .cdo-ad-section, .cdo-dicthomepage-btm-ad, .cdsidebarSearchAdParent, .center-ad, .center-ad-banner, .centerAd, .centerAdBar, .centerAds, .center_ad, .center_add, .center_ads, .center_adsense, .centerad, .centerads, .centeradv, .centered-ad, .centered_wide_ad, .cg_ad_slug, .ch_advertisement, .change-ad-h-btn, .change_AdContainer, .changeableadzone, .channel-adv, .chartad, .chitika-ad, .chitikaAdBlock, .chitikaAdCopy, .chrt-subheader__adv, .cinemabotad, .cl-ad-slot-post1, .cl-ad-slot-post2, .clHeader_Ad, .classifiedAdSplit, .classifiedAdThree, .clearerad, .client-ad, .close-ad-wrapper, .close2play-ads, .cm-ad, .cm-ad-row, .cm-hero-ad, .cm-rp01-ad, .cm-rp02-ad, .cm-take-a-break-ad-area, .cmAd, .cmAdCentered, .cmAdContainer, .cmAdFind, .cmAdSponsoredLinksBox, .cmBottomAdRight, .cmMediaRotatorAd, .cmMediaRotatorAdSponsor, .cmRecentOnAirAds, .cmTeaseAdSponsoredLinks, .cm_ads, .cmam_responsive_ad_widget_class, .cmg-ads, .cmi-content-3ads-horizontal, .cms-Advert, .cms-magazine-rightcol-adtag, .cn24-ads, .cn24-ads-160x600, .cn24-ads-300x250, .cn24-ads-600x290, .cnAdContainer, .cnAdDiv, .cnAdzerkDiv, .cnIframeAdvertisements, .cn_ad_placement, .cnbcHeaderAd, .cnbcRailAd, .cnbc_badge_banner_ad_area, .cnbc_banner_ad_area, .cnbc_leaderboard_ad, .cnn160AdFooter, .cnnAd, .cnnSearchSponsorBox, .cnnStoreAd, .cnnStoryElementBoxAd, .cnnWCAdBox, .cnnWireAdLtgBox, .cnn_728adbin, .cnn_adbygbin, .cnn_adcntr300x100, .cnn_adcntr728x90, .cnn_adcntr728x90t, .cnn_adspc300x100, .cnn_adspc336cntr, .cnn_adtitle, .cnn_fabcatad, .cnn_grpnadclk, .cnn_pt_ad, .cnn_sectprtnrbox_cb, .cnn_sectprtnrbox_grpn336, .cns-ads-stage, .cnt-half-page-ads, .cnt-header-ad, .cnt-right-box-ad, .cnt-right-vertical-ad, .cnt-right-vertical-ad-home, .cntAd, .cnt_ad, .cntrad, .cobalt-ad, .col-ad, .col-ad-hidden, .col-line-ad, .colRightAd, .col_ad, .col_header_ads_300x250, .colads, .colombiaAd, .column-ad, .column2-ad, .columnAdvert, .columnBoxAd, .columnRightAdvert, .column_3_ad, .com-ad-server, .comment-ad, .comment-ad-wrap, .comment-advertisement, .comment_ad, .comment_ad_box, .commentsFavoritesAd, .commentsbannerad, .commercialAd, .common-adv-box, .common_advertisement_title, .communityAd, .comp_AdsFrontPage_300x600, .companion-ad, .companion-ads, .companionAd, .companion_ad, .compareBrokersAds, .component-sponsored-links, .conTSponsored, .con_widget_advertising, .conductor_ad, .confirm_ad_left, .confirm_ad_right, .confirm_leader_ad, .consoleAd, .cont-ad, .contads_middle, .contained-ad-shaft, .container--ad, .container--bannerAd, .container--header-ads, .container-ad-600, .container-adbanner-global, .container-adbanner-list, .container-adbanner-mobile, .container-adds, .container-advMoreAbout, .container-adwords, .container-rectangle-ad, .container-top-adv, .containerAdsense, .containerSqAd, .container_ad, .container_row_ad, .container_serendipity_plugin_google_adsense, .contains-ad, .content-ad, .content-ad-article, .content-ad-box, .content-ad-outer-container, .content-ad-side, .content-ad-widget, .content-ad-wrapper, .content-advert, .content-advertisment, .content-box-inner-adsense, .content-cliff__ad, .content-cliff__ad-container, .content-footer-ad, .content-footer-ad-block, .content-header-ad, .content-item-ad-top, .content-list__ad-label, .content-result-ads, .content-unit-ad, .contentAd, .contentAd510, .contentAdBox, .contentAdContainer, .contentAdFoot, .contentAdIndex, .contentAds, .contentAdsCommon, .contentAdsWrapper, .contentAdvertisement, .contentTopAd, .contentTopAdSmall, .contentTopAds, .content_468_ad, .content_ad, .content_ad_728, .content_ad_head, .content_ad_side, .content_ads, .content_ads_index, .content_adsense, .content_adsq, .content_advert, .content_advertising, .content_bottom_adsense, .content_column2_ad, .content_inner_ad, .content_middle_adv, .content_tagsAdTech, .contentad, .contentad-home, .contentad300x250, .contentad_right_col, .contentadarticle, .contentadfloatl, .contentadleft, .contentads1, .contentads2, .contentadstartpage, .contentadstop1, .contentadvside, .contentleftad, .contentpage_searchad, .contents-ads-bottom-left, .contenttextad, .contentwellad, .contentwidgetads, .contest_ad, .context-ads, .contextualAds, .contextual_ad_unit, .convert-media-ad, .copy-adChoices, .core-adplace, .cornerBoxInnerWhiteAd, .cornerad, .cosmo-ads, .cp-adsInited, .cp_ad, .cpaAdPosition, .cpmstarHeadline, .cpmstarText, .cr_ad, .cranky-ads-zone, .create_ad, .credited_ad, .criAdv, .criteo-ad, .cross_delete_ads, .crumb-ad, .cs-adv-wrapper, .cs-mpu, .csPromoAd, .csa-adsense, .cscTextAd, .cse_ads, .csiAd_medium, .cspAd, .ct-ad-article, .ct-ad-article-wrapper, .ct-ads, .ct-bottom-ads, .ct_ad, .ctn-advertising, .ctnAdSkyscraper, .ctnAdSquare300, .ctn_ads_rhs, .ctn_ads_rhs_organic, .ctpl-duplicated-ad, .ctr-tss-ads, .cube-ad, .cubeAd, .cube_ad, .cube_ads, .cubead-widget, .currency_ad, .custom-ad, .custom-ad-container, .custom-ads, .custom-advert-banner, .custom-banner-leaderboard-ad, .customAd, .custom_ads, .custom_banner_ad, .custom_footer_ad, .customadvert, .customized_ad_module, .cwAdvert, .cwv2Ads, .cxAdvertisement, .cyads650x100, .da-custom-ad-box, .darla_ad, .dart-ad, .dart-ad-content, .dart-ad-grid, .dart-ad-taboola, .dart-ad-title, .dart-advertisement, .dart-leaderboard, .dart-leaderboard-top, .dart-medsquare, .dartAd300, .dartAd491, .dartAdImage, .dart_ad, .dart_tag, .dartad, .dartadbanner, .dartadvert, .dartiframe, .datafile-ad, .dc-ad, .dc-banner, .dc-half-banner, .dc-widget-adv-125, .dcAdvertHeader, .dd-ad, .dd-ad-container, .dda-ad, .ddc-table-ad, .deckAd, .deckads, .demo-advert, .desktop-ad, .desktop-ad-banner, .desktop-advert, .desktop-aside-ad, .desktop-aside-ad-hide, .desktop-postcontentad-wrapper, .desktop_ad, .desktoponlyad, .detail-ads, .detailMpu, .detailSidebar-adPanel, .detail_ad, .detail_article_ad, .detail_top_advert, .details-advert, .devil-ad-spot, .dfad, .dfad_first, .dfad_last, .dfad_pos_1, .dfad_pos_2, .dfad_pos_3, .dfad_pos_4, .dfad_pos_5, .dfad_pos_6, .dfads-javascript-load, .dfp-ad, .dfp-ad-advert_mpu_body_1, .dfp-ad-container, .dfp-ad-full, .dfp-ad-rect, .dfp-ad-unit, .dfp-ad-widget, .dfp-banner, .dfp-button, .dfp-leaderboard, .dfp-plugin-advert, .dfp-slot-wallpaper, .dfp-tag-wrapper, .dfp-top1, .dfp-top1-container, .dfp_ad, .dfp_ad_caption, .dfp_ad_content_bottom, .dfp_ad_content_top, .dfp_ad_footer, .dfp_ad_header, .dfp_ad_inner, .dfrads, .diggable-ad-sponsored, .discourse-google-dfp, .display-ad, .display-ads-block, .display-advertisement, .displayAd, .displayAd728x90Js, .displayAdCode, .displayAdSlot, .displayAdUnit, .displayAds, .display_ad, .display_ads_right, .div-google-adx, .divAd, .divAdright, .divAdsBanner, .divAdsLeft, .divAdsRight, .divAdvTopRight, .divGoogleAdsTop, .divMAD2, .divReklama, .divRepAd, .divSponsoredBox, .divSponsoredLinks, .divTopADBanner, .divTopADBannerWapper, .div_adv300, .div_adv620, .div_adv728, .div_advertisement, .div_advertorial, .div_advstrip, .div_banner468, .divad1, .divad2, .divad3, .divads, .divadsensex, .divider-ad, .divider-advert, .divider-full-width-ad, .divider_ad, .dlSponsoredLinks, .dm-ads-125, .dm-ads-350, .dmRosMBAdBox, .dm_ad-container, .dmco_advert_iabrighttitle, .dn-ad-small, .dn-ad-wide, .dod_ad, .double-ad, .double-ads, .double-click-ad, .double-square-ad, .doubleGoogleTextAd, .double_adsense, .double_click_widget, .doubleclick-ad, .doubleclick_adtype, .download-ad, .downloadAds, .download_ad, .download_adv_text_video, .download_link_sponsored, .downloadad, .drop-ad, .dropdownAds, .ds-ad, .ds-ad-300, .ds-ad-col-container, .ds-ad-container, .ds-ad-container-300, .ds-ad-container-728, .ds-ad-container-home, .ds-ad-container-ros, .ds-ad-home, .ds-ad-inner, .ds-ad-ros, .dsq_ad, .dualAds, .dvad1, .dvad2, .dvad3, .dvad3mov, .dvad4, .dvad4cont, .dvad5, .dvad5cont, .dvadevent, .dvadvhw, .dvcvmidads, .dvcvrgtad, .dwn_link_adv, .dynamic-ad-wrap-b, .dynamic-ads, .dynamicLeadAd, .dynamic_ad, .dynamic_adslot, .dynamicad1, .dynamicad2, .e-ad, .eads, .earAdv, .east_ad_bg, .east_ad_block, .easy-ads, .easyAdsBox, .easyAdsSinglePosition, .easyazon-block, .eb_ad280, .ebayads, .ec-ads, .ec-ads-remove-if-empty, .ec_ad_banner, .ecosia-ads, .editor_ad, .editorial-adsense, .editors-ads, .ehs-adbridge, .ej-advertisement-text, .element-ad, .element-adplace, .em-ad, .em-ads-widget, .em_ad_300x250, .em_ads_box_dynamic_remove, .embAD, .embed-ad, .embedded-article-ad, .embeddedAd, .embeddedAds, .emm-ad, .empty-ad, .endemic_ads, .eng_ads, .engagement_ad, .eniro_ad, .enterpriseAd, .entry-ad, .entry-ads, .entry-ads-110, .entry-body-ad, .entry-bottom-ad, .entry-injected-ad, .entry-top-ad, .entryAd, .entry_sidebar_ads, .entryad, .eol-ads, .epicgame-ads, .esp_publicidad, .et-single-post-ad, .etad, .eu-advertisment1, .eu-advertisment2, .eu-miniadvertisment, .event-ads, .event-ads-inside, .exec-advert-flash, .expanding-ad, .expertsAd, .ext-ad, .external-add, .externalAdComponent, .extrasColumnFuseAdLocal, .ez-ad, .ez-clientAd, .ezAdsWidget, .ezAdsense, .ezoic-ad, .fN-affiliateStrip, .f_Ads, .facebook-ad, .fbCalendarAds, .fbPhotoSnowboxAds, .fblockad, .fc_splash_ad, .fd-ad, .fd-display-ad, .fdDisplayAdGrid, .fdc_ad, .feat_ads, .featureAd, .feature_ad, .featured-ad, .featured-ads, .featured-sponsors, .featured-story-ad, .featuredAdBox, .featuredAds, .featuredBoxAD, .featured_ad, .featured_ad_item, .featured_advertisers_box, .featuredadvertising, .feed-ad, .feedBottomAd, .feeds-adblade, .ffz_bottom_ad, .fg_Ad, .fgc-advertising, .fi_adsense, .field-name-shared-ad-placement-landscape, .finpostsads, .fireplaceadleft, .fireplaceadright, .fireplaceadtop, .first-ad, .first-ad-wrap, .first_ad, .first_post_ad, .firstad, .firstpost_advert, .firstpost_advert_container, .fiveMinCompanionBanner, .fix-ad, .fixed-ad-160x600, .fixedAds, .fixedRightAd, .fl-adsense, .fl_adbox, .flagads, .flash-advertisement, .flashAd, .flash_ad, .flash_advert, .flashad, .flashadd, .flex-ad, .flexAd, .flexad, .flexadvert, .flexbanneritemad, .flexiad, .flipbook_v2_sponsor_ad, .floatad, .floatads, .floated-ad, .floated_right_ad, .floating-advert, .floatingAds, .fly-ad, .fm-badge-ad, .fnadvert, .fns_td_wrap, .fold-ads, .follower-ad-bottom, .foot-ad, .foot-ads, .foot-advertisement, .foot_adsense, .footad, .footer-300-ad, .footer-ad, .footer-ad-elevated, .footer-ad-full-wrapper, .footer-ad-section, .footer-ad-squares, .footer-ad1, .footer-ads, .footer-ads-wrapper, .footer-adsbar, .footer-adsense, .footer-advert, .footer-advert-large, .footer-advertisement, .footer-advertisement-container, .footer-advertisements, .footer-advertising-area, .footer-banner-ad, .footer-floating-ad, .footer-leaderboard-ad, .footer-ribbon-ad, .footer-text-ads, .footerAd, .footerAdModule, .footerAdUnit, .footerAdWrapper, .footerAds, .footerAdsWrap, .footerAdslot, .footerAdverts, .footerFullAd, .footerGoogleAdMainWarp, .footerTextAd, .footer_ad, .footer_ad336, .footer_ad_container, .footer_ads, .footer_adv, .footer_advertisement, .footer_banner_ad_container, .footer_block_ad, .footer_bottom_ad, .footer_bottomad, .footer_line_ad, .footer_text_ad, .footer_text_adblog, .footerad, .footerads, .footeradspace, .footertextadbox, .for-taboola, .foreign-ad01, .foreign-ad02, .forex_ad_links, .fortune-ad-unit, .forum-ad-2, .forum-topic--adsense, .forumAd, .forum_ad_beneath, .forumtopad, .four-ads, .four-six-eight-ad, .four_button_threeone_ad, .four_percent_ad, .fp-ads, .fp-right-ad, .fp-right-ad-list, .fp-right-ad-zone, .fp_ad_text, .frame_adv, .framead, .freedownload_ads, .freegame_bottomad, .freewheelDEAdLocation, .frn_adbox, .frn_cont_adbox, .frn_placeholder_google_ads, .frontads, .frontone_ad, .frontpage-google-ad, .frontpage-right-ad, .frontpage-right-ad-hide, .frontpage_ads, .fs-ad-block, .fs1-advertising, .fsAdContainer, .fs_ad_300x250, .fsrads, .ft-ad, .ftb-native-ads, .ftdAdBar, .ftdContentAd, .ftr_ad, .ftv-ad-sumo, .full-ad, .full-width-ad, .full-width-ad-container, .fullSizeAd, .full_ad_box, .full_ad_row, .full_width_ad, .fulladblock, .fullbannerad, .fusion-advert, .fusionAd, .fusionAdLink, .future_dfp-inline_ad, .fw-mod-ad, .fwAdTags, .g-ad, .g-ad-slot, .g-ad-slot-toptop, .g-adblock3, .g-advertisement-block, .g2-adsense, .g3-adsense, .g3rtn-ad-site, .gAdRows, .gAdSky, .gAds, .gAds1, .gAdsBlock, .gAdsContainer, .gAdvertising, .g_ad, .g_ad336, .g_ads_200, .g_ads_728, .g_adv, .g_ggl_ad, .ga-ad-split, .ga-ads, .ga-textads-bottom, .ga-textads-top, .gaTeaserAds, .gaTeaserAdsBox, .gabfire_ad, .gad_container, .gads300x250, .gads_cb, .gads_container, .gadsense, .gadstxtmcont2, .galleria-AdOverlay, .galleria-ad-2, .galleria-adsense, .gallery-ad, .gallery-ad-container, .gallery-ad-holder, .gallery-ad-wrapper, .gallery-sidebar-ad, .galleryAds, .galleryAdvertPanel, .galleryLeftAd, .galleryRightAd, .gallery_300x100_ad, .gallery__aside-ad, .gallery__bottom-ad, .gallery__footer-ad, .gallery_ad, .gallery_ads_box, .gallery_post--interstitial_ad, .galleryads, .gam-300x250-default-ad-container, .gam_ad_slot, .game-ads, .game-right-ad-container, .gameAd, .gameBottomAd, .game__adv_containerLeaderboard, .game_right_ad, .game_under_ad, .gamepage_boxad, .gamepageadBox, .gameplayads, .games-ad-wrapper, .games-ad300, .gamesPage_ad_container, .gamesPage_ad_content, .gamezebo_ad, .gamezebo_ad_info, .gbl_adstruct, .gbl_advertisement, .gdgt-header-advertisement, .gdgt-postb-advertisement, .gdm-ad, .geeky_ad, .gels-inlinead, .gemini-ad, .gen_side_ad, .general-adzone, .general_banner_ad, .generic-ad-module, .generic-ad-title, .generic_300x250_ad, .geoAd, .getridofAds, .getridofAdsBlock, .gfp-banner, .ggads, .ggadunit, .ggadwrp, .gglAds, .ggl_ads_row, .gglads300, .gl_ad, .glamsquaread, .glance_banner_ad, .globalAd, .globalAdLargeRect, .globalAdLeaderBoard, .global_banner_ad, .gm-ad-lrec, .gms-ad-centre, .gms-advert, .gn_ads, .go-ad, .go-ads-widget-ads-wrap, .goglad, .goog_ad, .googad, .googads, .google-ad, .google-ad-728-90, .google-ad-afc-header, .google-ad-block, .google-ad-bottom-outer, .google-ad-container, .google-ad-content, .google-ad-image, .google-ad-pad, .google-ad-side_ad, .google-ad-sidebar, .google-ad-space, .google-ad-space-vertical, .google-ad-square-sidebar, .google-ad-top-outer, .google-ad-widget, .google-ad-wrapper-ui, .google-ads, .google-ads-boxout, .google-ads-container, .google-ads-group, .google-ads-leaderboard, .google-ads-long, .google-ads-obj, .google-ads-responsive, .google-ads-right, .google-ads-rodape, .google-ads-sidebar, .google-ads-slim, .google-ads-widget, .google-ads-wrapper, .google-ads2, .google-adsbygoogle, .google-adsense, .google-advertisement, .google-advertisement_txt, .google-afc-wrapper, .google-csi-ads, .google-dfp-ad-label, .google-entrepreneurs-ad, .google-right-ad, .google-sponsored, .google-sponsored-ads, .google-sponsored-link, .google-sponsored-links, .google-text-ads, .google-user-ad, .google300x250, .google300x250BoxFooter, .google300x250TextDetailMiddle, .google300x250TextFooter, .google468, .google468_60, .google728x90, .google728x90TextDetailTop, .googleAd, .googleAd-content, .googleAd-list, .googleAd300x250, .googleAd300x250_wrapper, .googleAd728OuterTopAd, .googleAdBox, .googleAdContainer, .googleAdContainerSingle, .googleAdFoot, .googleAdSearch, .googleAdSense, .googleAdSenseModule, .googleAdTopTipDetails, .googleAdWrapper, .googleAd_160x600, .googleAd_1x1, .googleAd_728x90, .googleAd_body, .googleAdd, .googleAds, .googleAds336, .googleAds728, .googleAds_article_page_above_comments, .googleAdsense, .googleAdsense468x60, .googleAdv1, .googleBannerWrapper, .googleContentAds, .googleInsideAd, .googleLgRect, .googleProfileAd, .googleSearchAd_content, .googleSearchAd_sidebar, .googleSideAd, .googleSkyWrapper, .googleSubjectAd, .google_728x90, .google_ad, .google_ad3, .google_ad336, .google_ad_bg, .google_ad_btn, .google_ad_container, .google_ad_label, .google_ad_mrec, .google_ad_right, .google_ad_wide, .google_add, .google_add_container, .google_admanager, .google_ads, .google_ads_468x60, .google_ads_bom_block, .google_ads_bom_title, .google_ads_content, .google_ads_header11, .google_ads_sidebar, .google_ads_v3, .google_adsense, .google_adsense1, .google_adsense1_footer, .google_adsense_footer, .google_adsense_sidebar_left, .google_afc, .google_afc_ad, .google_afc_articleintext, .google_afc_categorymain, .google_top_adsense, .google_top_adsense1, .google_top_adsense1_footer, .google_top_adsense_footer, .google_txt_ads_mid_big_img, .googlead, .googlead-sidebar, .googleadArea, .googlead_idx_b_97090, .googlead_idx_h_97090, .googlead_iframe, .googlead_outside, .googleadbottom, .googleadcontainer, .googleaddiv, .googleaddiv2, .googleadiframe, .googleads, .googleads-bottommiddle, .googleads-container, .googleads-topmiddle, .googleads_300x250, .googleads_title, .googleadsense, .googleadsrectangle, .googleadvertisemen120x600, .googleadvertisement, .googleadwrap, .googleafc, .googlebanwide, .googleimagead1, .googleimagead2, .googlepostads, .googley_ads, .gp-advertisement-wrapper, .gpAdBox, .gpAdFooter, .gpAds, .gp_adbanner--bottom, .gp_adbanner--top, .gpadvert, .gpt-ad, .gpt-ads, .gr-adcast, .gradientAd, .graphic_ad, .grev-ad, .grey-ad-line, .grey-ad-notice, .greyAd, .greyad, .grid-ad, .grid-advertisement, .grid-item-ad, .gridAd, .gridAdRow, .gridSideAd, .gridad, .gridstream_ad, .group-ad-leaderboard, .group-google-ads, .group_ad, .grv_is_sponsored, .gsAd, .gsfAd, .gsl-ads, .gt_ad, .gt_ad_300x250, .gt_ad_728x90, .gt_adlabel, .gtadlb, .gtop_ad, .guide-ad, .gujAd, .gutter-ad-left, .gutter-ad-right, .gutter-ad-wrapper, .gutterAdHorizontal, .gw-ad, .gx_ad, .h-ad, .h-ad-728x90-bottom, .h-ad-remove, .h-ads, .h-large-ad-box, .h-top-ad, .h11-ad-top, .h_Ads, .h_ad, .half-ad, .halfPageAd, .half_ad_box, .halfpage_ad_container, .has-ad, .hasads, .hbPostAd, .hbox_top_sponsor, .hcf-ad, .hcf-ad-rectangle, .hcf-cms-ad, .hd-adv, .hdTopAdContainer, .hd_advert, .hd_below_player_ad, .hdr-ad, .hdr-ad-text, .hdr-ads, .hdrAd, .hdr_ad, .head-ads, .headAd, .head_ad, .head_ad_wrapper, .head_ads, .head_adv, .head_advert, .headad, .headadcontainer, .header--ad-space, .header-ad, .header-ad-area, .header-ad-banner, .header-ad-column, .header-ad-new-wrap, .header-ad-space, .header-ad-wrap, .header-ad-wrapper, .header-ad-zone, .header-ad234x60left, .header-ad234x60right, .header-adbox, .header-adplace, .header-ads, .header-ads-container, .header-ads-holder, .header-adsense, .header-adv, .header-advert, .header-advert-container, .header-article-ads, .header-banner-ad, .header-banner-ads, .header-bannerad, .header-google-ads, .header-menu-horizontal-ads, .header-menu-horizontal-ads-content, .header-sponsor, .header-taxonomy-image-sponsor, .header-top-ad, .header15-ad, .header3-advert, .header728-ad, .headerAd, .headerAd1, .headerAdArea, .headerAdCode, .headerAdWrapper, .headerAds, .headerAdspace, .headerAdvert, .headerTextAd, .headerTopAd, .headerTopAds, .header_ad, .header_ad_2, .header_ad_center, .header_ad_div, .header_ad_space, .header_ads, .header_ads_box, .header_ads_promotional, .header_adsense_banner, .header_advert, .header_advertisement, .header_advertisement_text, .header_advertisment, .header_classified_ads, .header_leaderboard_ad, .header_right_ad, .headerad, .headerad-720, .headerad-placeholder, .headeradarea, .headeradhome, .headeradinfo, .headeradright, .headerads, .heading-ad-space, .headline-ads, .headline_advert, .heatmapthemead_ad_widget, .hero-ad, .hi5-ad, .hidden-ad, .hide-ad, .hideAdMessage, .hideIfEmptyAd, .hidePauseAdZone, .hide_ad, .hide_internal_ad, .highlight-news-ad, .highlights-ad, .highlightsAd, .hioxInternalAd, .hl-ads-holder-0, .hl-post-center-ad, .hm-sec-ads, .hm_advertisment, .hm_top_right_google_ads, .hm_top_right_google_ads_budget, .hn-ads, .home-300x250-ad, .home-activity-ad, .home-ad, .home-ad-container, .home-ad-links, .home-ad1, .home-ad2, .home-ad3, .home-ad4, .home-ad728, .home-ads, .home-ads-container, .home-ads-container1, .home-advert, .home-area3-adv-text, .home-body-ads, .home-features-ad, .home-sidebar-ad, .home-sidebar-ad-300, .home-slider-ads, .home-sponsored-links, .home-sticky-ad, .home-top-of-page__top-box-ad, .home-top-right-ads, .homeAd, .homeAd1, .homeAd2, .homeAdBox, .homeAdBoxA, .homeAdBoxBetweenBlocks, .homeAdBoxInBignews, .homeAdFullBlock, .homeAdSection, .homeAddTopText, .homeCentreAd, .homeMainAd, .homeMediumAdGroup, .homePageAds, .homeSubAd, .homeTextAds, .home_ad, .home_ad720_inner, .home_ad_300x100, .home_ad_300x250, .home_ad_bottom, .home_ad_large, .home_adblock, .home_advert, .home_advertisement, .home_advertorial, .home_box_latest_ads, .home_mrec_ad, .home_offer_adv, .home_sidebar_ads, .home_sway_adv, .home_top_ad_slider, .home_top_ad_slides, .home_top_right_ad, .home_top_right_ad_label, .homead, .homeadnews, .homefront468Ad, .homepage-300-250-ad, .homepage-ad, .homepage-ad-block-padding, .homepage-ad-buzz-col, .homepage-ad-module, .homepage-advertisement, .homepage-footer-ad, .homepage-footer-ads, .homepage-right-rail-ad, .homepage-sponsoredlinks-container, .homepage300ad, .homepageAd, .homepageFlexAdOuter, .homepageMPU, .homepage__ad, .homepage__ad--middle-leader-board, .homepage__ad--top-leader-board, .homepage__ad--top-mrec, .homepage_ads, .homepage_block_ad, .homepage_middle_right_ad, .homepageinline_adverts, .homesmallad, .homestream-ad, .hor_ad, .hori-play-page-adver, .horisont_ads, .horiz_adspace, .horizontal-ad-holder, .horizontal-ad2, .horizontalAd, .horizontalAdText, .horizontalAdvert, .horizontal_ad, .horizontal_adblock, .horizontal_ads, .horizontalbtad, .horizontaltextadbox, .horizsponsoredlinks, .hortad, .house-ad, .house-ads, .houseAd, .houseAd1, .houseAdsStyle, .housead, .hover_300ad, .hover_ads, .hoverad, .hp-col4-ads, .hp-content__ad, .hp-inline-ss-service-ad, .hp-main__rail__footer__ad, .hp-slideshow-right-ad, .hp-ss-service-ad, .hp2-adtag, .hpPollQuestionSponsor, .hpPriceBoardSponsor, .hp_320-250-ad, .hp_ad_300, .hp_ad_box, .hp_ad_cont, .hp_ad_text, .hp_horizontal_ad, .hp_t_ad, .hp_w_ad, .hpa-ad1, .hr-ads, .hr_ad, .hr_advt, .hrad, .hss-ad, .hss-ad-300x250_1, .hss_static_ad, .hst-contextualads, .ht_ad_widget, .html-advertisement, .html-block-ads, .html-component-ad-filler, .html5-ad-progress-list, .hyad, .hype_adrotate_widget, .i360ad, .i_ad, .iab300x250, .iab728x90, .ib-adv, .ib-figure-ad, .ibm_ad_bottom, .ibm_ad_text, .ibt-top-ad, .ic-ads, .ico-adv, .icon-advertise, .icon-myindependentad, .iconAdChoices, .icon_ad_choices, .iconads, .id-Advert, .id-Article-advert, .idGoogleAdsense, .idMultiAd, .idc-adContainer, .idc-adWrapper, .idgGoogleAdTag, .iframe-ad, .iframe-ads, .iframeAd, .iframead, .iframeadflat, .im-topAds, .image-ad-336, .image-advertisement, .image-viewer-ad, .image-viewer-mpu, .imageAd, .imageAdBoxTitle, .imageAds, .imageGalleryAdHeadLine, .imagead, .imageads, .images-adv, .imagetable_ad, .img-advert, .img_ad, .img_ads, .imgad, .imgur-ad, .impactAdv, .import_video_ad_bg, .imuBox, .in-ad, .in-article-mpu, .in-between-ad, .in-content-ad, .in-node-ad-300x250, .in-page-ad, .in-story-ads, .in-story-text-ad, .inArticleAdInner, .inPageAd, .inStoryAd-news2, .in_article_ad, .in_content_ad_container, .in_content_advert, .in_up_ad_game, .incontentAd, .indEntrySquareAd, .indent-advertisement, .index-adv, .index-after-second-post-ad, .index_728_ad, .index_ad, .index_right_ad, .indexad, .indie-sidead, .indy_googleads, .inf-admedia, .inf-admediaiframe, .info-ads, .info-advert-160x600, .info-advert-300x250, .info-advert-728x90, .info-advert-728x90-inside, .infoBoxThreadPageRankAds, .ingameadbox, .ingameboxad, .ingridAd, .inhouseAdUnit, .inhousead, .injectedAd, .inline-ad, .inline-ad-placeholder, .inline-ad-wrap, .inline-ad-wrapper, .inline-adblock, .inline-advert, .inline-mpu, .inline-mpu-left, .inlineAd, .inlineAdContainer, .inlineAdImage, .inlineAdInner, .inlineAdNotice, .inlineAdText, .inlineAdTour, .inlineAd_content, .inlineAdvert, .inlineAdvertisement, .inlineSideAd, .inline_ad, .inline_ad_container, .inline_ad_title, .inline_ads, .inlinead, .inlinead-tagtop, .inlineadsense, .inlineadtitle, .inlist-ad, .inlistAd, .inner-ad, .inner-ad-disclaimer, .inner-advt-banner-3, .inner-post-ad, .inner468ad, .innerAdWrapper, .innerAds, .innerContentAd, .inner_ad, .inner_ad_advertise, .inner_big_ad, .innerad, .innerpostadspace, .inpostad, .ins_adwrap, .insert-advert-ver01, .insert-post-ads, .insertAd_AdSlice, .insertAd_Rectangle, .insertAd_TextAdBreak, .insert_ad, .insert_advertisement, .insertad, .insideStoryAd, .inside_ad, .inside_ad_box, .instructionAdvHeadline, .insurance-ad, .intad, .inteliusAd_image, .interbody-ad-unit, .interest-based-ad, .internal-ad, .internalAd, .internalAdSection, .internalAdsContainer, .internal_ad, .interstitial-ad, .interstitial-ad600, .interstitial468x60, .interstitial_ad_wrapper, .ion-ad, .ione-widget-dart-ad, .ipm-sidebar-ad-middle, .iprom-ad, .ipsAd, .iqadlinebottom, .is-sponsored, .is24-adplace, .isAd, .is_trackable_ad, .isad_box, .island-ad, .islandAd, .islandAdvert, .island_ad, .island_ad_right_top, .islandad, .isocket_ad_row, .item-ad, .item-ad-leaderboard, .item-ads, .item-advertising, .item-container-ad, .item-housead, .item-housead-last, .itemAdvertise, .item_ads, .itinerary-index-advertising, .ja-ads, .jalbum-ad-container, .jam-ad, .jc_ad_container, .jg-ad-5, .jg-ad-970, .jimdoAdDisclaimer, .job-ads-container, .jobAds, .jobkeywordads, .jobs-ad-box, .jobs-ad-marker, .joead728, .jp-advertisment-promotional, .js-ad, .js-ad--comment, .js-ad-doubleimu, .js-ad-dynamic, .js-ad-hideable, .js-ad-home, .js-ad-hover, .js-ad-imu, .js-ad-konvento, .js-ad-loaded, .js-ad-loader-bottom, .js-ad-prepared, .js-ad-primary, .js-ad-static, .js-ad-unit-bottom, .js-ad-wrapper, .js-advert, .js-advert--vc, .js-advert-upsell-popup, .js-billboard-advert, .js-dfp-ad, .js-dfpAdPosSR, .js-gptAd, .js-header-ad, .js-native-ad, .js-outbrain-container, .js-slim-nav-ad, .js-sticky-ad, .js-stream-ad, .js-stream-featured-ad, .js-toggle-ad, .js_adContainer, .js_contained-ad-container, .jsx-adcontainer, .juicyads_300x250, .jumboAd, .jw-ad, .jw-ad-label, .jw-ad-media-container, .jw-ad-visible, .kads-main, .kd_ads_block, .kdads-empty, .kdads-link, .keyword-ads-block, .kip-advertisement, .kip-banner-ad, .kitara-sponsored, .knowledgehub_ad, .kopa-ads-widget, .kw_advert, .kw_advert_pair, .l-350-250-ad-words, .l-ad-300, .l-ad-728, .l-adsense, .l-bottom-ads, .l-header-advertising, .l300x250ad, .l_ad_sub, .label-ad, .labelads, .labeled_ad, .landing-feed--ad-vertical, .landing-page-ads, .landingAdRail, .landing_adbanner, .large-btn-ad, .large-right-ad, .largeAd, .largeRecAdNewsContainerRight, .largeRectangleAd, .largeUnitAd, .large_ad, .large_add_container, .largesideadpane, .last-left-ad, .last-right-ad, .lastAdvertorial, .lastLiAdv, .lastRowAd, .lastads, .lastpost_advert, .layer-ad-bottom, .layer-ad-top, .layer-xad, .layer_text_ad, .layeradinfo, .layout-ad, .layout_communityad_right_ads, .lazy-ad, .lazy-adv, .lazyad, .lazyload_ad, .lazyload_ad_article, .lb-ad, .lb-adhesion-unit, .lbc-ad, .lbl-advertising, .lblAdvert, .lcontentbox_ad, .ld-ad, .ld-ad-inner, .lead-ad, .lead-ads, .lead-advert, .lead-board-ad-cont-home, .leadAd, .leader-ad, .leaderAd, .leaderAdSlot, .leaderAdTop, .leaderAdvert, .leaderBoardAdHolder, .leaderBoardAdvert, .leaderOverallAdArea, .leader_ad, .leader_aol, .leaderad, .leaderboard-ad, .leaderboard-ad-belt, .leaderboard-ad-container, .leaderboard-ad-green, .leaderboard-ad-grid, .leaderboard-ad-inner, .leaderboard-ad-main, .leaderboard-ad-module, .leaderboard-ad-unit, .leaderboard-adblock, .leaderboard-ads, .leaderboard-advert, .leaderboard-advertisement, .leaderboardAd, .leaderboardAdContainer, .leaderboardAdContainerInner, .leaderboardFooter_ad, .leaderboard_ad, .leaderboard_ad_top_responsive, .leaderboard_ad_unit, .leaderboard_ad_unit_groups, .leaderboard_ads, .leaderboard_adv, .leaderboard_banner_ad, .leaderboardad, .leaderboardadmiddle, .leaderboardadtop, .leaderboardadwrap, .leadgenads, .left-ad, .left-ad180, .left-ads, .left-advert, .left-column-rectangular-ad, .left-column-virtical-ad, .left-rail-ad, .left-rail-ad__wrapper, .left-rail-horizontal-ads, .left-sidebar-box-ads, .left-takeover-ad, .left-takeover-ad-sticky, .left120X600AdHeaderText, .leftAd, .leftAdColumn, .leftAdContainer, .leftAd_bottom_fmt, .leftAd_top_fmt, .leftAds, .leftAdvert, .leftCol_advert, .leftColumnAd, .leftPaneAd, .left_300_ad, .left_ad, .left_ad_160, .left_ad_areas, .left_ad_box, .left_ad_container, .left_adlink, .left_ads, .left_adsense, .left_advertisement_block, .left_col_ad, .left_google_add, .left_sidebar_wide_ad, .leftad, .leftadd, .leftadtag, .leftbar_ad_160_600, .leftbarads, .leftbottomads, .leftnavad, .leftrighttopad, .leftsidebar_ad, .lefttopad1, .legacy-ads, .legal-ad-choice-icon, .lgRecAd, .lg_ad, .liboxads, .ligatus, .lightad, .lijit-ad, .linead, .linkAD, .link_adslider, .link_advertise, .linkads, .linkedin-sponsor, .links_google_adx, .list-ad, .list-ads, .listAdvertGenerator, .listad, .listicle--ad-rail, .listing-content-ad-container, .listing-inline-ad, .listing-item-ad, .listingAd, .listings-ad-block, .listings-bottom-ad-w, .listings_ad, .little_vid_ads, .live-search-list-ad-container, .live_tv_sponsorship_ad, .liveads, .liveblog__highlights__ad, .livingsocial-ad, .ljad, .llsAdContainer, .lnad, .loadadlater, .local-ads, .localad, .location-ad, .log_ads, .logo-ad, .logoAd-hanging, .logoAds, .logo_AdChoices, .logoad, .logoutAd, .logoutAdContainer, .longAd, .longAdBox, .longAds, .longBannerAd, .long_ad, .longform-ad, .loop-ad, .loop_google_ad, .lottery-ad-container, .lower-ads, .lowerAd, .lowerAds, .lowerContentBannerAd, .lowerContentBannerAdInner, .lower_ad, .lp_az_billboard__via_content_header_ad_, .lpt_adsense_bottom_content, .lqm-ads, .lqm_ad, .lr-ad, .lr_skyad, .lsn-yahooAdBlock, .lt_ad_call, .luma-ad, .luxeAd, .lx_ad_title, .m-ContentAd, .m-ad, .m-ad--open, .m-ad-tvguide-box, .m-advertisement, .m-advertisement--container, .m-gallery-overlay--ad-top, .m-layout-advertisement, .m-mem--ad, .m-sponsored, .m4-adsbygoogle, .mTopAd, .m_ad1, .m_ad300, .m_banner_ads, .macAd, .macad, .mad_adcontainer, .madison_ad, .magad, .magazine_box_ad, .main-ad, .main-ads, .main-advert, .main-advertising, .main-column-ad, .main-footer-ad, .main-right-ads, .main-tabs-ad-block, .main-top-ad-container, .mainAd, .mainAdContainer, .mainAds, .mainEcoAd, .mainLeftAd, .mainLinkAd, .mainRightAd, .main_ad, .main_ad_adzone_5_ad_0, .main_ad_adzone_6_ad_0, .main_ad_adzone_7_ad_0, .main_ad_adzone_7_ad_1, .main_ad_adzone_8_ad_0, .main_ad_adzone_8_ad_1, .main_ad_adzone_9_ad_0, .main_ad_adzone_9_ad_1, .main_ad_bg, .main_ad_bg_div, .main_ad_container, .main_adbox, .main_ads, .main_adv, .main_intro_ad, .main_right_ad, .main_wrapper_upper_ad_area, .mainadWrapper, .mainadbox, .mantis-ad, .mantis__recommended__item--external, .mantis__recommended__item--sponsored, .manual-ad, .mapAdvertising, .map_google_ad, .map_media_banner_ad, .mapped-ad, .marginadsthin, .marginalContentAdvertAddition, .market-ad, .market-ad-small, .marketing-ad, .marketplace-ad, .marketplaceAd, .marketplaceAdShell, .markplace-ads, .marquee-ad, .master_post_advert, .masthead-ad, .masthead-ad-control, .masthead-ads, .mastheadAds, .masthead_ad_banner, .masthead_ads_new, .masthead_topad, .matador_sidebar_ad_600, .match-results-cards-ad, .mb-advert, .mb-advert__leaderboard--large, .mb-advert__mpu, .mb-advert__tweeny, .mb-block--advert-side, .mb-list-ad, .mcx-content-ad, .md-adv, .md-advertisement, .mdl-ad, .mdl-quigo, .medColModAd, .medRecContainer, .medRect, .med_ad_box, .media--ad, .media-ad-rect, .media-advert, .media-network-ad, .media-temple-ad-wrapper-link, .mediaAd, .mediaAdContainer, .mediaResult_sponsoredSearch, .media_ad, .mediamotive-ad, .medium-google-ad-container, .medium-rectangle-ad, .medium-rectangle-advertisement, .mediumRectagleAd, .mediumRectangleAd, .mediumRectangleAdvert, .medium_ad, .medium_rectangle_ad_container, .mediumad, .medo-ad-section, .medo-ad-wideskyscraper, .medrec-ad, .medrect-ad, .medrect-ad2, .medrectAd, .medrect_ad, .medrectadv4, .member-ads, .memberAdsContainer, .member_ad_banner, .meme_adwrap, .memrise_ad, .menu-ad, .menuAd, .menuAds-cage, .menuItemBannerAd, .menuad, .menueadimg, .merchantAdsBoxColRight, .mess_div_adv, .messageBoardAd, .message_ads, .metaRedirectWrapperBottomAds, .metaRedirectWrapperTopAds, .meta_ad, .metaboxType-sponsor, .mf-ad300-container, .mg_box_ads, .mgid-wrapper, .micro_ad, .mid-ad-wrapper, .mid-advert, .mid-page-2-advert, .mid-post-ad, .midAd, .mid_4_ads, .mid_ad, .mid_article_ad_label, .mid_banner_ad, .mid_page_ad, .mid_page_ad_big, .mid_right_ads, .mid_right_inner_id_ad, .midad, .middle-ad, .middle-ads, .middle-ads728, .middle-footer-ad, .middleAd, .middleAdLeft, .middleAdMid, .middleAdRight, .middleAds, .middleBannerAd, .middle_AD, .middle_ad, .middle_ad_responsive, .middle_ads, .middlead, .middleadouter, .midpost-ad, .min_navi_ad, .mini-ad, .mini-ads, .miniHeaderAd, .mini_ads, .mini_ads_bottom, .mini_ads_right, .miniad, .miniads, .misc-ad, .misc-ad-label, .miscAd, .ml-advert, .ml-adverts-sidebar-1, .ml-adverts-sidebar-2, .ml-adverts-sidebar-4, .ml-adverts-sidebar-bottom-1, .ml-adverts-sidebar-bottom-2, .ml-adverts-sidebar-bottom-3, .ml-adverts-sidebar-random, .mlaAd, .mm-ad-mpu, .mm-ad-sponsored, .mmc-ad, .mmc-ad-wrap-2, .mmcAd_Iframe, .mnopolarisAd, .mntl-gpt-adunit, .mo_googlead, .mobile-ad, .mobile-related-ad, .mobileAdWrap, .mobileAdvertInStreamHighlightText, .mobileAppAd, .mobile_ad_container, .mobile_featuredad, .mobile_featuredad_article, .mobileadbig, .mobilesideadverts, .mod-ad, .mod-ad-1, .mod-ad-2, .mod-ad-box, .mod-ad-lrec, .mod-ad-n, .mod-ad-risingstar, .mod-adblock, .mod-adcpc, .mod-adopenx, .mod-ads, .mod-big-ad-switch, .mod-big-banner-ad, .mod-google-ads, .mod-google-ads-container, .mod-horizontal-ad, .mod-sponsored-links, .mod-trbad, .mod-tss-ads-wrapper, .mod-vertical-ad, .mod_ad, .mod_ad_imu, .mod_ad_top, .mod_admodule, .mod_ads, .mod_openads, .modal-ad, .module--ad, .module-ad, .module-ad-small, .module-ads, .module-advert, .module-advertisement, .module-image-ad, .module-rectangleads, .module-sponsored-ads, .moduleAd, .moduleAdSpot, .moduleAdvert, .moduleAdvertContent, .moduleBannerAd, .module_ad, .module_ad_disclaimer, .module_box_ad, .module_header_sponsored, .modulegad, .moduletable-adsponsor, .moduletable-advert, .moduletable-bannerAd6, .moduletable-centerad, .moduletable-googleads, .moduletable-rectangleads, .moduletable_ad-right, .moduletable_ad160x600_center, .moduletable_ad300x250, .moduletable_adtop, .moduletable_advertisement, .moduletable_top_ad, .moduletableadvert, .moduletableexclusive-ads, .moduletablesquaread, .moduletabletowerad, .modulo-publicidade, .mom-ad, .momizat-ads, .moneyball-ad, .monitor-g-ad-300, .monitor-g-ad-468, .monsterad, .moreAdBlock, .mos-ad, .mosaicAd, .mostpop_sponsored_ad, .motherboard-ad, .mp-ad, .mpsponsor, .mpu-ad, .mpu-ad-con, .mpu-ad-top, .mpu-advert, .mpu-c, .mpu-container-blank, .mpu-footer, .mpu-fp, .mpu-holder, .mpu-leaderboard, .mpu-left, .mpu-mediatv, .mpu-right, .mpu-title, .mpu-top-left, .mpu-top-left-banner, .mpu-top-right, .mpu-unit, .mpu-wrapper, .mpu01, .mpu250, .mpu600, .mpuAd, .mpuAdArea, .mpuAdSlot, .mpuAdvert, .mpuArea, .mpuBox, .mpuContainer, .mpuMiddle, .mpuTextAd, .mpu_Ad, .mpu_ad, .mpu_advert, .mpu_advertisement_border, .mpu_container, .mpu_gold, .mpu_holder, .mpu_placeholder, .mpu_platinum, .mpu_side, .mpu_text_ad, .mpuad, .mpuads, .mpuholderportalpage, .mr-dfp-ad, .mrec_advert, .ms-ad-superbanner, .ms-ads-link, .ms_header_ad, .msat-adspace, .msfg-shopping-mpu, .msg-ad, .msgad, .mslo-ad, .mslo-ad-300x250, .mslo-ad-728x66, .mslo-ad-holder, .msnChannelAd, .msn_ad_wrapper, .mst_ad_top, .mt-ad-container, .mt-header-ads, .mt_adv, .mt_adv_v, .mtv-adChoicesLogo, .mtv-adv, .multiad2, .multiadwrapper, .multiple-ad-tiles, .mvAd, .mvAdHdr, .mvp_ad_widget, .mvp_block_type_ad_module, .mvw_onPageAd1, .mwaads, .mx-box-ad, .mxl_ad_inText_250, .my-ad250x300, .my-ads, .myAds, .myAdsGroup, .myTestAd, .mypicadsarea, .myplate_ad, .nSponsoredLcContent, .nSponsoredLcTopic, .n_ad, .naMediaAd, .nadvt300, .narrow_ad_unit, .narrow_ads, .native-ad, .native-ad-item, .native-ad-link, .native-ad-promoted-provider, .native-adv, .nativeAd, .nativeMessageAd, .nature-ad, .nav-ad, .nav-adWrapper, .navAdsBanner, .navBads, .nav_ad, .nav_textads, .navad, .navadbox, .navcommercial, .navi_ad300, .naviad, .nba300Ad, .nba728Ad, .nbaAdNotice, .nbaAroundAd2, .nbaT3Ad160, .nbaTVPodAd, .nbaTextAds, .nbaTwo130Ads, .nbc_Adv, .nbc_ad_carousel_wrp, .nc-dealsaver-container, .nc-exp-ad, .ndmadkit, .netPost_ad1, .netPost_ad3, .netads, .netshelter-ad, .network-ad-two, .new-ad-box, .new-ads-scroller, .newHeaderAd, .newPex_forumads, .newTopAdContainer, .new_ad1, .newad, .newad1, .newadsky-wrapper, .news-ad, .news-ad-block-a, .news-place-ad-info, .newsAd, .news_ad_box, .news_article_ad_google, .news_footer_ad_container, .newsad, .newsblock-ads, .newsfeed_adunit, .newsletter_ad, .newsstackedAds, .newstream_ad, .newsviewAdBoxInNews, .newsvinemsn_adtype, .nexusad, .nf-adbox, .ngs-adv-async, .ninemsn-footer-ad, .ninth-box-ad, .nl2ads, .nn-mpu, .no1postadvert, .noAdForLead, .noTitleAdBox, .node-ad, .node-content-ad, .node-left-ad-under-img, .node_ad_wrapper, .nomobilead, .non-empty-ad, .nonsponserIABAdBottom, .normalAds, .normalad, .northad, .not-an-ad-header, .note-advertisement, .npAdGoogle, .npSponsorTextAd, .nrAds, .nr_partners, .nrelate .nr_partner, .nsAdRow, .nscr300Ad, .nscrMidAdBlock, .nscrT1AdBlock, .ntnlad, .ntv-ad, .nu2ad, .nuffnangad, .nw-ad, .nw-ad-468x60, .nw-ad-label, .nw-taboola, .nw-top-ad, .nzs-ads, .o-ads, .o-ads--center, .oad-ad, .oas-ad, .oas-bottom-ads, .oas-leaderboard-ads, .oasInAds, .oas_ad, .oas_add, .oas_advertisement, .oas_sidebar_v7, .oasad, .oasads, .ob_ads_header, .ob_container .item-container-obpd, .ob_dual_right > .ob_ads_header ~ .odb_div, .ob_nm_paid, .oba_message, .ocp-sponsor, .odc-nav-ad, .ody-sponsor, .offer_sponsoredlinks, .oi_horz_ad_container, .oio-banner-zone, .oio-link-sidebar, .oio-openslots, .oio-zone-position, .old-advertorial-block, .omnitureAdImpression, .on-demand-ad, .on_single_ad_box, .one-ad, .oneColumnAd, .onethirdadholder, .onf-ad, .onsite-ads-728w, .opaAd, .openads, .openadstext_after, .openx, .openx-ad, .openx_10, .openx_11, .openx_15, .openx_16, .openx_17, .openx_3, .openx_4, .openx_ad, .openx_frame, .openxbuttons, .optional-ad, .os-advertisement, .osan-ads, .other-posts-ads, .other_adv2, .otherheader_ad, .otj_adspot, .outbrain_ad_li, .outbrain_dual_ad_whats_class, .outbrain_ul_ad_top, .outer-ad-container, .outerAdWrapper, .outerAd_300x250_1, .outeradcontainer, .outermainadtd1, .outgameadbox, .outside_ad, .ovAdLabel, .ovAdPromo, .ovAdSky, .ovAdartikel, .ov_spns, .ovadsenselabel, .overflow-ad, .overlay-ad, .overlay-ad-container, .overlay-ads, .overlay_ad, .ox-holder, .ox_ad, .ozadtop, .ozadtop3, .p2_right_ad, .p75_sidebar_ads, .pAdsBlock2, .p_adv, .p_topad, .pa_ads_label, .paddingBotAd, .pads2, .padvertlabel, .page-ad, .page-ad-container, .page-advert, .page-pencil-ad-container-bottom, .pageAds, .pageBottomGoogleAd, .pageFooterAd, .pageGoogleAd, .pageGoogleAdFlat, .pageGoogleAdSubcontent, .pageGoogleAds, .pageGoogleAdsContainer, .pageHeaderAd, .pageHeaderAds, .pageLeaderAd, .pageSkinAds, .page_ad, .page_content_right_ad, .pagead, .pagebuilder_ad, .pageclwideadv, .pagefair-acceptable, .pagenavindexcontentad, .pair_ads, .pan-ad-inline, .pan-ad-inline1, .pan-ad-inline2, .pan-ad-inline3, .pan-ad-sidebar-top, .pan-ad-sidebar1, .pan-ad-sidebar2, .pane-ad-ads-all, .pane-ad-block, .pane-ad-manager-bottom-right-rail-circ, .pane-ad-manager-middle, .pane-ad-manager-middle1, .pane-ad-manager-right, .pane-ad-manager-right1, .pane-ad-manager-right2, .pane-ad-manager-right3, .pane-ad-manager-shot-business-circ, .pane-ad-manager-subscribe-now, .pane-adonews-ad, .pane-ads, .pane-adv-manager, .pane-bzads-bzadwrapper-120x60-partner, .pane-bzads-fintech-300x250, .pane-dart-dart-tag-gfc-ad-rail-3, .pane-dfp-dfp-ad-atf-728x90, .pane-frontpage-ad-banner, .pane-frontpage-ad-banner-hk, .pane-mp-advertisement-rectangle, .pane-openx, .pane-site-ads, .pane-sponsored-links, .pane-textlinkads-26, .pane-tw-ad-master-ad-300x250a, .pane-tw-ad-master-ad-300x600, .pane-tw-adjuggler-tw-adjuggler-half-page-ad, .pane-two-column-ads, .pane_ad_wide, .panel-ad, .panel-ad-mr, .panel-advert, .panel-body-adsense, .panel__column--vc-advert, .panel__row--with-vc-advert, .panel_ad, .paneladvert, .partial-ad, .partner-ad, .partner-ads-container, .partner-adsonar, .partnerAd, .partnerAdTable, .partner_ads, .partnerad_container, .partnersTextLinks, .patronad, .pb-f-ad-flex, .pb-f-ad-leaderboard, .pb-f-ads-dfp-big-box-300x250, .pb-f-ads-dfp-box-300x450, .pb-f-ads-dfp-halfpage-300x600, .pb-f-ads-dfp-leaderboard-728x90, .pb-f-ads-taboola-article-well, .pb-f-ads-taboola-right-rail-alt, .pb-mod-ad-flex, .pb-mod-ad-leaderboard, .pc-ad, .pcads_widget, .pd-ads-mpu, .peg_ad, .pencil-ad, .pencil-ad-container, .pencil_ad, .performancingads_region, .pfAd, .pf_content_ad, .pf_sky_ad, .pf_top_ad, .pfad, .pfad2, .pfimgAds, .pg-ad-block, .pgAdSection_Home_MasterSponsers, .ph-ad, .ph-ad-desktop, .ph-ad-mediumrectangle, .photo-ad, .photoad, .photobox-adbox, .pics_detail_ad, .pics_footer_ad, .picto_ad, .pin-ad, .pixtrack-adcode, .pkgTemplateAdWrapper, .pl__superad, .pl_adv1, .pl_adv1_t, .pl_adv1_wr, .pl_adv1_wr2, .pla_ad, .place-ads, .placeholder-ad, .placeholderAd, .plainAd, .play-page-ads, .playAds1, .playAds2, .player-ads, .player-leaderboard-ad-wrapper, .player-under-ad, .playerAd, .playerAdv, .player_ad, .player_ad2, .player_ad_box, .player_hover_ad, .player_page_ad_box, .plistaList > .itemLinkPET, .plista_inimg_box, .plista_widget_i300x250, .plista_widget_retrescoAd_1, .plista_widget_retrescoAd_2, .pm-ad, .pm-ad-zone, .pm-banner-ad, .pmad-in2, .pmg-sponsoredlinks, .pn-ad, .pn_dfpads, .pnp_ad, .poac_ads_text, .pod-ad, .pod-ad-300, .pod-ad-box, .podRelatedAdLinksWidget, .podSponsoredLink, .poll_sponsor_ad, .pop-up-ad, .popAdContainer, .popadtext, .popunder-adv, .popup-ad, .popupAd, .popupAdOuter, .popupAdWrapper, .popup_ad, .portalCenterContentAdBottom, .portalCenterContentAdMiddle, .portalCenterContentAdTop, .portal_searchresultssponsoredlist, .portalcontentad, .pos_advert, .post-ad, .post-adsense-bottom, .post-advert, .post-advertisement, .post-full-ad, .post-full-ad-wrapper, .post-googlead, .post-load-ad, .post-nativeadcarousel, .post-sponsored, .postAd, .postWideAd, .post__ad, .post__body-ad-center, .post__inarticle-ad-template, .post_ad, .post_ads, .post_advert, .post_seperator_ad, .post_sponsor_unit, .post_sponsored, .postad, .postads, .postadsense, .postbit_ad_block, .postbit_adbit_register, .postbit_adcode, .postbit_adcode_old, .postbody_ads, .poster-ad-asset-module, .poster_ad, .postfooterad, .postgroup-ads, .postgroup-ads-middle, .power_by_sponsor, .ppp_interior_ad, .ppr_priv_sponsored_coupon_listing, .pq-ad, .pr-ad-tower, .pr-widget, .pre-roll-ad, .pre-title-ad, .prebodyads, .premium-ad, .premium-ads, .premium-adv, .premiumAdOverlay, .premiumAdOverlayClose, .premiumInHouseAd, .premium_ad_container, .premiumad, .preview-ad, .pricead-border, .primary-ad, .primary-advertisment, .primary_sidebar_ad, .printAds, .pro_ad_adzone, .pro_ad_system_ad_container, .pro_ad_zone, .prod_grid_ad, .product-ads, .product-bar-ads, .product-inlist-ad, .profile-ad-container, .profile_ad_bottom, .profile_ad_top, .promo-ad, .promo-box--ad, .promo-box--leaderboard-ad, .promo-class-brand-getprice, .promoAd, .promoAds, .promoAdvertising, .promo_ad, .promo_border, .promoad, .promoboxAd, .promotionTextAd, .promotional-feature-ads, .proof_ad, .propel-ad, .proper-ad-unit, .ps-ad, .ps-ligatus_placeholder, .pt_ad03, .pt_col_ad02, .pubDesk, .pub_300x250, .pub_300x250m, .pub_728x90, .publiboxright300, .publication-ad, .publicidadSuperior, .publicidad_horizontal, .publicidade, .publicidade-dotted, .publicidade-full-banner, .puff-ad, .puff-advertorials, .pull-ad, .pull_top_ad, .pullad, .pulse360ad, .pulsir-ad, .puppyAd, .purchad, .push--ad, .push-ad, .pushDownAd, .pushdown-ad, .pushdownAd, .pw_wb_ad_300x250, .pwgAdWidget, .pxz-ad-widget, .pxz-taskbar-anchor, .pyv-afc-ads-container, .qa_ad_left, .qm-ad, .qm-ad-content, .qm-ad-content-news, .quads-ad2, .quads-ad2_widget.first, .quads-ad4, .quads-location, .quick-tz-ad, .quicklinks-ad, .quigo, .quigo-ad, .quigoAdCenter, .quigoAdRight, .quigoMod, .quigoads, .quotead, .qzvAdDiv, .r-ad, .r7ad, .r_ad, .r_ad_1, .r_ad_box, .r_adbx_top, .r_ads, .r_col_add, .rad_container, .radium-ad-spot, .radium-builder-widget-ad-spot, .raff_ad, .rail-ad, .rail-article-sponsored, .rail__ad, .rail__mps-ad, .rail_ad, .railad, .railadspace, .ramsay-advert, .rbFooterSponsors, .rbRectAd, .rc_ad_300x100, .rc_ad_300x250, .rd_header_ads, .rdio-homepage-widget, .re-Ads-l, .readerads, .readermodeAd, .realtor-ad, .rec_ad, .recent-post-widget-ad, .recentAds, .recent_ad_holder, .recommend-ad-one, .recommend-ad-two, .rect-ad, .rect-ad-1, .rect_ad, .rect_ad_module, .rect_advert, .rectad, .rectadv, .rectangle-ad, .rectangle-ad-container, .rectangle-embed-ad, .rectangleAd, .rectangleAdContainer, .rectangle_ad, .rectanglead, .rectangleads, .redads_cont, .reedwan_adds300x250_widget, .referrerDetailAd, .refreshAds, .refreshable_ad, .region-ads, .region-ads-1, .region-banner-ad, .region-dfp-ad-content-bottom, .region-dfp-ad-content-top, .region-dfp-ad-footer, .region-dfp-ad-header, .region-footer-ad-full, .region-header-ad, .region-header-ads, .region-leader-ad-bottom, .region-leader-ad-top, .region-middle-ad, .region-regions-ad-top, .region-regions-ad-top-inner, .region-top-ad-position, .region-widget-ad-top-0, .regular_728_ad, .regularad, .reklam, .reklam-block, .reklam2, .reklam728, .reklama, .reklama-c, .reklama-vert, .reklama1, .reklame-right-col, .reklame-wrapper, .reklamka, .rel_ad_box, .related-ad, .related-ads, .related-al-ads, .related-al-content-w150-ads, .related-content-story__stories--sponsored-1, .related-content-story__stories--sponsored-2, .related-content-story__stories--sponsored-3, .related-guide-adsense, .relatedAds, .relatedContentAd, .related_post_google_ad, .relatesearchad, .remads, .remnant_ad, .remove-ads, .removeAdsLink, .removeAdsStyle, .reportAdLink, .resads-adspot, .residentialads, .resourceImagetAd, .respAds, .responsive-ad, .responsiveAdHiding, .responsiveAdsense, .result-ad, .result-sponsored, .resultAd, .result_ad, .result_item_ad-adsense, .resultad, .results-ads, .resultsAdsBlockCont, .results_sponsor_right, .rev_square_side_door, .revcontent-main-ad, .review-ad, .reviewMidAdvertAlign, .review_ad1, .reviewpage_ad2, .reviews-box-ad, .rf_circ_ad_460x205, .rg-ad, .rght300x250, .rgt-300x250-ad, .rgt-ad, .rgt_ad, .rh-ad, .rhads, .rhc-ad-bottom, .rhs-ad, .rhs-ads-panel, .rhs-advert-container, .rhs-advert-link, .rhs-advert-title, .rhs_ad_title, .rhsad, .rhsadvert, .ribbon-ad-container, .ribbon-ad-matte, .right-ad, .right-ad-300x250, .right-ad-block, .right-ad-container, .right-ad-holder, .right-ad-tagline, .right-ad2, .right-ads, .right-ads2, .right-adsense, .right-adv, .right-advert, .right-col-ad, .right-column-ad, .right-navAdBox, .right-rail-ad, .right-rail-ad-banner, .right-rail-ad-bottom-container, .right-rail-ad-top-container, .right-rail-broker-ads, .right-rail__ad, .right-rail__container--ad, .right-side-ad, .right-side-ads, .right-sidebar-box-ad, .right-sidebar-box-ads, .right-square-ad-blocks, .right-takeover-ad, .right-takeover-ad-sticky, .right-top-ad, .rightAD, .rightAd, .rightAd1, .rightAd2, .rightAdBox, .rightAdColumn, .rightAdContainer, .rightAd_bottom_fmt, .rightAd_top_fmt, .rightAds, .rightAds_ie_fix, .rightAdvert, .rightAdverts, .rightBoxAd, .rightBoxMidAds, .rightColAd, .rightColAdBox, .rightColumnAd, .rightColumnAdd, .rightColumnAdsTop, .rightColumnRectAd, .rightHeaderAd, .rightRailAd, .rightRailMiddleAd, .rightSecAds, .rightSideBarAd, .rightSideSponsor, .rightTopAdWrapper, .right_ad, .right_ad_160, .right_ad_box, .right_ad_box1, .right_ad_common_block, .right_ad_innercont, .right_ad_text, .right_ad_top, .right_ad_unit, .right_ads, .right_ads_column, .right_adsense_box_2, .right_adskin, .right_adv, .right_advert, .right_advertise_cnt, .right_advertisement, .right_block_advert, .right_box_ad, .right_box_ad_rotating_container, .right_col_ad, .right_col_ad_300_250, .right_column_ads, .right_content_ad, .right_content_ad_16, .right_google_ads, .right_hand_advert_column, .right_image_ad, .right_long_ad, .right_outside_ads, .right_picAd, .right_side-partyad, .right_side_ads, .right_side_box_ad, .right_sponsor_main, .rightad, .rightad250, .rightad300, .rightad600, .rightad_1, .rightad_2, .rightadbig, .rightadblock, .rightadbox1, .rightadd, .rightads, .rightadunit, .rightadv, .rightbigcolumn_ads, .rightbigcolumn_ads_nobackground, .rightbox_content_ads, .rightboxads, .rightcol-adbox, .rightcol-block-ads, .rightcol_boxad, .rightcol_div_openx2, .rightcolads, .rightcoladvert, .rightcoltowerad, .rightmenu_ad, .rightnav_adsense, .rightpanelad, .rightrail-ad-block, .rightrail_ads, .rightsideAd, .righttop-advt, .ringtone-ad, .risingstar-ad, .risingstar-ad-inner, .riverAdsLoaded, .riverSponsor, .rmx-ad, .rnav_ad, .rngtAd, .rockmelt-ad, .rockmeltAdWrapper, .rolloverad, .rot_ads, .rotating-ad, .rotating-ads, .rotatingAdvertisement, .rotatingBannerWidget, .rotatingadsection, .rotator_ad_overlay, .round_box_advert, .roundedCornersAd, .roundingrayboxads, .rowad, .rowgoogleads, .rr-300x250-ad, .rr-300x600-ad, .rr_ads, .rr_skyad, .rs_ad_bot, .rs_ad_top, .rside_adbox, .rtAdFtr, .rtAd_bx, .rtSideHomeAd, .rt_ad, .rt_ad1_300x90, .rt_ad_300x250, .rt_ad_call, .rt_advert_name, .rt_el_advert, .rtd_ads_text, .rtmad, .rtmm_right_ad, .runner-ad, .s-ad, .s-ads, .s-hidden-sponsored-item, .s2k_ad, .sType-ad, .s_ad, .s_ad2, .s_ad_160x600, .s_ad_300x250, .s_ads, .s_ads_label, .s_sponsored_ads, .sa_AdAnnouncement, .sadvert, .sam-ad, .sam_ad, .savvyad_unit, .say-center-contentad, .sb-ad, .sb-ad-margin, .sb-ad-sq-bg, .sb-ad2, .sb-ad3, .sb-ads, .sb-ads-here, .sb-top-sec-ad, .sbAd, .sbAdUnitContainer, .sbTopadWrapper, .sb_ad, .sb_ad_holder, .sb_adsN, .sb_adsNv2, .sb_adsW, .sb_adsWv2, .sc-ad, .sc_ad, .sc_iframe_ad, .scad, .scanAd, .scb-ad, .scc_advert, .schedule_ad, .sci-ad-main, .sci-ad-sub, .scoopads, .scraper_ad_unit, .script-ad { display: none !important; } </style><style type="text/css">.script_ad_0, .scroll-ads, .scrolling-ads, .search-ad, .search-ad-no-ratings, .search-advertisement, .search-message-container-ad, .search-results-ad, .search-sponsor, .search-sponsored, .searchAd, .searchAdTop, .searchAds, .searchCenterBottomAds, .searchCenterTopAds, .searchResultAd, .searchRightBottomAds, .searchRightMiddleAds, .searchSponsorItem, .searchSponsoredResultsBox, .searchSponsoredResultsList, .search_ad_box, .search_column_results_sponsored, .search_inline_web_ad, .search_results_ad, .search_results_sponsored_top, .searchad, .searchads, .sec-ad, .sec_headline_adbox, .second-post-ads-wrapper, .secondary-advertisment, .secondaryAdModule, .secondary_ad, .section-ad, .section-ad-related, .section-ad-wrapper, .section-ad2, .section-adbox-bottom, .section-adbox1, .section-ads, .section-adtag, .section-advert-banner, .section-aside-ad, .section-aside-ad2, .section-front__side-bar-ad, .section-front__top-ad, .section-sponsor, .section_ad, .section_ad_left, .section_mpu_wrapper, .section_mpu_wrapper_wrapper, .sector-widget__tiny-ad, .selection-grid-advert, .selfServeAds, .seoTopAds, .sepContentAd, .series-ad, .serp-adv-item, .serp-adv__head, .serp_sponsored, .servedAdlabel, .serviceAd, .servsponserLinks, .set_ad, .sex-party-ad, .sfsp_adadvert, .sgAd, .sh-ad-box, .sh-ad-section, .sh-leftAd, .shadvertisment, .shareToolsItemAd, .shift-ad, .shoppingGoogleAdSense, .shortads, .shortadvertisement, .showAd, .showAdContainer, .showAd_No, .showAd_Yes, .showad_box, .showcaseAd, .showcasead, .shunno_widget_sidebar_advert, .si-adRgt, .sidbaread, .side-ad, .side-ad-120-bottom, .side-ad-120-middle, .side-ad-120-top, .side-ad-160-bottom, .side-ad-160-middle, .side-ad-160-top, .side-ad-300, .side-ad-300-bottom, .side-ad-300-middle, .side-ad-300-top, .side-ad-big, .side-ad-blocks, .side-ad-container, .side-ad-inner, .side-ads, .side-ads-block, .side-ads-wide, .side-ads300, .side-advert, .side-bar-ad-position1, .side-bar-ad-position2, .side-mod-preload-big-ad-switch, .side-rail-ad-wrap, .side-sky-banner-160, .side-video-ads-wrapper, .sideAd, .sideAdLeft, .sideAdTall, .sideAdWide, .sideBannerAdsLarge, .sideBannerAdsSmall, .sideBannerAdsXLarge, .sideBarAd, .sideBarCubeAd, .sideBlockAd, .sideBoxAd, .sideBoxM1ad, .sideBoxMiddleAd, .sideBySideAds, .sideToSideAd, .side_300_ad, .side_ad, .side_ad2, .side_ad300, .side_ad_1, .side_ad_2, .side_ad_3, .side_ad_box_mid, .side_ad_box_top, .side_ad_top, .side_add_wrap, .side_ads, .side_adsense, .side_adv, .side_adv_01, .side_adv_left, .side_adv_right, .sidead, .sidead_150, .sidead_300, .sidead_300250_ht, .sidead_550125, .sideadmid, .sideads, .sideads_l, .sideadsbox, .sideadtable, .sideadvert, .sideadverts, .sidebar--mps_ad, .sidebar-350ad, .sidebar-above-medium-rect-ad-unit, .sidebar-ad, .sidebar-ad-300, .sidebar-ad-300x250-cont, .sidebar-ad-a, .sidebar-ad-b, .sidebar-ad-box, .sidebar-ad-box-caption, .sidebar-ad-c, .sidebar-ad-cont, .sidebar-ad-container, .sidebar-ad-container-1, .sidebar-ad-container-2, .sidebar-ad-container-3, .sidebar-ad-div, .sidebar-ad-rect, .sidebar-ad-slot, .sidebar-adbox, .sidebar-ads, .sidebar-adv-container, .sidebar-advertisement, .sidebar-atf-ad-wrapper, .sidebar-below-ad-unit, .sidebar-big-ad, .sidebar-block-adsense, .sidebar-box-ad, .sidebar-box-ads, .sidebar-content-ad, .sidebar-header-ads, .sidebar-paid-ad-label, .sidebar-skyscraper-ad, .sidebar-sponsors, .sidebar-square-ad, .sidebar-text-ad, .sidebar-top-ad, .sidebar300adblock, .sidebarAd, .sidebarAdBlock, .sidebarAdLink, .sidebarAdNotice, .sidebarAdUnit, .sidebarAds300px, .sidebarAdvert, .sidebarCloseAd, .sidebarNewsletterAd, .sidebar_ADBOX, .sidebar_ad, .sidebar_ad_1, .sidebar_ad_2, .sidebar_ad_3, .sidebar_ad_300, .sidebar_ad_300_250, .sidebar_ad_580, .sidebar_ad_container, .sidebar_ad_container_div, .sidebar_ad_holder, .sidebar_ad_leaderboard, .sidebar_ad_module, .sidebar_ads, .sidebar_ads-300x250, .sidebar_ads_336, .sidebar_ads_left, .sidebar_ads_right, .sidebar_ads_title, .sidebar_adsense, .sidebar_advert, .sidebar_advertising, .sidebar_box_ad, .sidebar_right_ad, .sidebar_skyscraper_ad, .sidebar_small_ad, .sidebar_sponsors, .sidebarad, .sidebarad160, .sidebarad_bottom, .sidebaradbox, .sidebaradcontent, .sidebarads, .sidebaradsense, .sidebarboxad, .sideheadnarrowad, .sideheadsponsorsad, .sidelist_ad, .sideskyad, .simple_ads_manager_block_widget, .simple_ads_manager_widget, .simple_ads_manager_zone_widget, .simple_adsense_widget, .simplead-container, .simpleads-item, .single-ad, .single-ad-anchor, .single-ad-wrap, .single-ads, .single-google-ad, .single-item-page-ads, .single-post-ad, .single-post-ads-750x90, .single-top-ad, .singleAd, .singleAdBox, .singleAdsContainer, .single_ad, .single_advert, .single_bottom_ad, .single_fm_ad_bottom, .single_post_ads_cont, .single_top_ad, .singlead, .singleads, .singleadstopcstm2, .singlepageleftad, .singlepostad, .singlepostadsense, .singpagead, .site-ad-block, .site-ads, .site-footer__ad-area, .site-head-ads, .site-nav-ad-inner, .site-top-ad, .siteWideAd, .site_ad, .site_ad_120_600, .site_ad_300x250, .site_sponsers, .sitesponsor, .sitesprite_ads, .six-ads-wrapper, .skinAd, .skinAdv02, .skin_ad_638, .skinad-l, .skinad-r, .skinny-sidebar-ad, .sky-ad, .sky-ad1, .skyAd, .skyAdd, .skyAdvert, .skyAdvert2, .skyCraper_bannerLong, .skyCraper_bannerShort, .sky_ad, .sky_ad_top, .sky_scraper_ad, .skyjobsadtext, .skyscraper-ad, .skyscraper-ad-container, .skyscraperAd, .skyscraper_ad, .skyscraper_bannerAdHome, .skyscraper_banner_ad, .sl-art-ad-midflex, .sl-header-ad, .sl_ad1, .sl_ad2, .sl_ad3, .sl_ad4, .sl_ad5, .sl_ad6, .sl_ad7, .sl_admarker, .sleekadbubble, .slide-ad, .slideAd, .slide_ad, .slider-right-advertisement-banner, .sliderad, .slideshow-ad, .slideshow-ad-container, .slideshow-ad-wrapper, .slideshow-ads, .slideshow-advertisement-note, .slideshowAd, .slideshow_ad_300, .slideshow_ad_note, .slot_728_ad, .slot_integrated_ad, .slpBigSlimAdUnit, .slpSquareAdUnit, .sm-ad, .sm-widget-ad-holder, .smAdText_r, .sm_ad, .small-ad, .small-ad-header, .small-ad-long, .small-ads, .smallAd, .smallAdContainer, .smallAds, .smallAdsContainer, .smallAdvertisments, .smallSkyAd1, .smallSkyAd2, .small_ad, .small_ad_bg, .small_ads, .small_sidebar_ad_container, .smallad, .smallad-left, .smalladblock, .smallads, .smalladscontainer, .smalladword, .smallbutton-adverts, .smallsideadpane, .smallsponsorad, .smart_ads_bom_title, .sml-item-ad, .sn-ad-300x250, .snarcy-ad, .sng_card_ads, .snoadnetwork, .social-ad, .softronics-ad, .southad, .sp-ad, .spLinks, .spaceAdds, .spc-ads-leaderboard, .spc-ads-sky, .specialAd175x90, .specialAdsContent, .specialAdsLabel, .specialAdsLink, .specialAdvertising, .specialHeaderAd, .special_ad_section, .specials_ads, .speedyads, .sphereAdContainer, .spl-ads, .spl_ad, .spl_ad2, .spl_ad_plus, .splitAd, .splitAdResultsPane, .splitter_ad, .splitter_ad_holder, .spn_links_box, .spnsrAdvtBlk, .spnsrCntnr, .spon-links, .spon125, .spon_link, .sponadbox, .sponlinkbox, .spons-link, .spons-wrap, .sponsBox, .sponsLinks, .sponsWrap, .spons_link_header, .spons_links, .sponser-link, .sponserIABAdBottom, .sponserLink, .sponsersads, .sponsertop, .sponslink, .sponsor-728, .sponsor-ad, .sponsor-ad-wrapper, .sponsor-ads, .sponsor-area, .sponsor-block, .sponsor-bottom, .sponsor-box, .sponsor-btns, .sponsor-inner, .sponsor-left, .sponsor-link, .sponsor-links, .sponsor-logo, .sponsor-module-target, .sponsor-post, .sponsor-promo, .sponsor-right, .sponsor-services, .sponsor-spot, .sponsor-text, .sponsor-text-container, .sponsor120x600, .sponsor728x90, .sponsorAd, .sponsorArea, .sponsorBannerWrapper, .sponsorBlock, .sponsorBottom, .sponsorBox, .sponsorBox_right_rdr, .sponsorLabel, .sponsorLink, .sponsorLinks, .sponsorMaskhead, .sponsorPanel, .sponsorPost, .sponsorPostWrap, .sponsorPuffsHomepage, .sponsorStrip, .sponsorText, .sponsorTitle, .sponsorTxt, .sponsor_ad, .sponsor_ad1, .sponsor_ad2, .sponsor_ad3, .sponsor_ad_area, .sponsor_advert_link, .sponsor_area, .sponsor_bar, .sponsor_block, .sponsor_button_ad, .sponsor_columns, .sponsor_div, .sponsor_div_title, .sponsor_footer, .sponsor_image, .sponsor_label, .sponsor_line, .sponsor_links, .sponsor_logo, .sponsor_placement, .sponsor_popup, .sponsor_units, .sponsorad, .sponsoradlabel, .sponsorads, .sponsoradtitle, .sponsored-ad, .sponsored-ad-label, .sponsored-ad-ob, .sponsored-ads, .sponsored-b, .sponsored-by-label, .sponsored-chunk, .sponsored-container-bottom, .sponsored-default, .sponsored-display-ad, .sponsored-editorial, .sponsored-features, .sponsored-header, .sponsored-headshop, .sponsored-inmail, .sponsored-inmail-legacy, .sponsored-link, .sponsored-links, .sponsored-links-alt-b, .sponsored-links-col, .sponsored-links-holder, .sponsored-links-right, .sponsored-links-tbl, .sponsored-offers-box, .sponsored-post, .sponsored-post_ad, .sponsored-result, .sponsored-result-row-2, .sponsored-results, .sponsored-right, .sponsored-right-border, .sponsored-rule, .sponsored-slot, .sponsored-tag, .sponsored-text, .sponsored-title, .sponsored-top, .sponsoredAd, .sponsoredAdLine, .sponsoredAds, .sponsoredBar, .sponsoredBottom, .sponsoredBox, .sponsoredEntry, .sponsoredFeature, .sponsoredInfo, .sponsoredInner, .sponsoredLabel, .sponsoredLeft, .sponsoredLink, .sponsoredLinks, .sponsoredLinks2, .sponsoredLinksBox, .sponsoredLinksGadget, .sponsoredLinksHead, .sponsoredLinksHeader, .sponsoredName, .sponsoredProduct, .sponsoredResults, .sponsoredSearch, .sponsoredShowcasePanel, .sponsoredSideInner, .sponsoredStats, .sponsoredTop, .sponsored_ad, .sponsored_ads, .sponsored_bar_text, .sponsored_box, .sponsored_box_search, .sponsored_by, .sponsored_content, .sponsored_glinks, .sponsored_link, .sponsored_links, .sponsored_links2, .sponsored_links_box, .sponsored_links_container, .sponsored_links_section, .sponsored_links_title_container, .sponsored_links_title_container_top, .sponsored_links_top, .sponsored_result, .sponsored_results, .sponsored_results-container, .sponsored_ss, .sponsored_text, .sponsored_well, .sponsoredby, .sponsoredibbox, .sponsoredlink, .sponsoredlinkHed, .sponsoredlinks, .sponsoredlinks-article, .sponsoredlinkscontainer, .sponsoredresults, .sponsoredtabl, .sponsoredtextlink_container_ovt, .sponsorheader, .sponsoring_link, .sponsoringbanner, .sponsorlink, .sponsorlink2, .sponsormsg, .sponsors-box, .sponsors-footer, .sponsors-module, .sponsors-widget, .sponsorsBanners, .sponsors_300x250, .sponsors_box_container, .sponsors_fieldset, .sponsors_links, .sponsors_spacer, .sponsorsbig, .sponsorship-box, .sponsorship-chrome, .sponsorship-container, .sponsorshipContainer, .sponsorship_ad, .sponsorshipbox, .sponsorwrapper, .sport-mpu-box, .spot-ad, .spotlight-ad, .spotlight-ad-left, .spotlightAd, .sprite-ad_label_vert, .sqAd2, .sq_ad, .square-ad, .square-ad--latest-video, .square-ad--neg-margin, .square-ad-1, .square-ad-container, .square-advt, .square-sidebar-ad, .square-sponsorship, .squareAd, .squareAdWrap, .squareAdd, .squareAddtwo, .squareAds, .square_ad, .square_ad_wrap, .square_ads, .square_advert_inner, .square_banner_ad, .square_button_ads, .squaread, .squaread-container, .squareads, .squared_ad, .sr-adsense, .sr-advert, .sr-in-feed-ads, .sr-side-ad-block, .sr_google_ad, .src_parts_gen_ad, .srp-grid-speed-ad3, .ss-ad-banner, .ss-ad-mpu, .ss-ad-thumbnail, .ss-ad-tower, .ss-ad_mrec, .ss_advertising, .stProAd, .stack-l-ad-center, .stackedads1, .stackedads2, .stand-alone-adzone, .standalone-ad-container, .standalone_txt_ad, .standard-ad, .star-ad, .start__advertising_container, .start__newest__big_game_container_body_games_advertising, .start_overview_adv_container, .statTop_adsense, .static-ad, .staticAd, .staticad, .staticad_mark125, .std_ad_container, .ste-ad, .sticky-ad, .sticky-ad-wrapper, .sticky-top-ad-wrap, .stickyAdLink, .sticky_ad_wrapper, .stickyadv, .stmAdHeightWidget, .stock-ticker-ad-tag, .stock_ad, .stocks-ad-tag, .store-ads, .story-ad, .story-ad-container, .story-inline-advert, .story-page-embedded-ad, .storyAdvert, .storyInlineAdBlock, .story_AD, .story_ad_div, .story_ads_right_spl, .story_ads_right_spl_budget, .story_body_advert, .story_right_adv, .storyad, .storyad300, .stpro_ads, .str-300x250-ad, .str-300x600-ad, .str-horizontal-ad-wrapper, .str-slim-nav-ad, .str-top-ad, .strawberry-ads, .stream-ad, .streamAd, .strip-ad, .stripad, .sub-feature-ad, .sub-header-ad, .subAdBannerArea, .subAdBannerHeader, .subNavAd, .sub_cont_AD01, .sub_cont_AD02, .sub_cont_AD04, .sub_cont_AD06, .sub_cont_AD07, .subad, .subadimg, .subcontent-ad, .subheadAdPanel, .subheaderAdlogo, .subheader_adsense, .subjects_ad, .submenu_ad, .subtitle-ad-container, .sugarad, .suit-ad-inject, .suitcase-ad, .super-ad, .super-leaderboard-advert, .superLeaderOverallAdArea, .supercommentad_left, .supercommentad_right, .supernews-ad-widget, .superscroll-ad, .supp-ads, .support-adv, .supportAdItem, .support_ad, .surveyad, .sweet-deals-ad, .syAd, .syHdrBnrAd, .sykscraper-ad, .syndicatedAds, .szoAdBox, .szoSponsoredPost, .t10ad, .tAd, .tabAd, .tabAds, .tab_ad, .tab_ad_area, .table-ad, .table_ad_bg, .tablebordersponsor, .taboola-ad, .taboola-container, .taboola-inbetweener, .taboola-item, .taboola-left-rail-wrapper, .taboola-partnerlinks-ad, .taboola-unit, .taboola-widget, .taboola_advertising, .taboola_blk, .taboola_lhs, .tadsanzeige, .tadsbanner, .tadselement, .takeOverAdLink, .tallAdvert, .tallad, .tangential-ad, .tblAds, .tblTopAds, .tbl_ad, .tbox_ad, .tc_ad_unit, .tckr_adbrace, .td-Adholder, .td-TrafficWeatherWidgetAdGreyBrd, .td-a-rec-id-custom_ad_1, .td-a-rec-id-custom_ad_2, .td-a-rec-id-custom_ad_3, .td-a-rec-id-event_bottom_ad, .td-a-rec-id-h12_obj_bottom_ad, .td-a-rec-id-h3_object_bottom_ad, .td-ad, .td-adspot-title, .td-header-ad-wrap, .td-header-sp-ads, .tdAdHeader, .tdBannerAd, .tdFeaturedAdvertisers, .td_ad, .td_footer_ads, .td_left_widget_ad, .td_leftads, .td_reklama_bottom, .td_reklama_top, .td_spotlight_ads, .td_topads, .tdad125, .tealiumAdSlot, .teaser-ad, .teaser-sponsor, .teaserAdContainer, .teaserAdHeadline, .teaser_adtiles, .teaser_advert_content, .testAd-holder, .text-ad, .text-ad-300, .text-ad-links, .text-ad-links2, .text-ad-sitewide, .text-ad-top, .text-ads, .text-advertisement, .text-g-advertisement, .text-g-group-short-rec-ad, .text-g-net-group-news-half-page-ad-300x600-or-300x250, .text-g-net-grp-google-ads-article-page, .text-g-nn-web-group-ad-halfpage, .text-g-sponsored-ads, .text-g-sponsored-links, .textAd, .textAd3, .textAdBG, .textAdBlock, .textAdBlwPgnGrey, .textAdBox, .textAdMinimum, .textAds, .textLinkAd, .textSponsor, .text_ad, .text_ad_description, .text_ad_title, .text_ad_website, .text_ads, .text_ads_2, .text_linkad_wrapper, .textad, .textadContainer, .textad_headline, .textadbox, .textadheadline, .textadlink, .textads, .textads_left, .textads_right, .textadscontainer, .textadsds, .textadsfoot, .textadtext, .textadtxt, .textadtxt2, .textbanner-ad, .textlink-ads, .textlinkads, .tf_page_ad_search, .tfagAd, .theAdvert, .the_list_ad_zone, .theads, .theleftad, .themeblvd-ad-square-buttons, .themidad, .themonic-ad2, .third-box-ad, .third-party-ad, .thirdAd160Cont, .thirdAdBot, .thirdAdHead, .thirdage_ads_300x250, .thirdage_ads_728x90, .thisIsAd, .thisIsAnAd, .this_is_an_ad, .thisisad, .thread-ad, .thread-ad-holder, .threadAdsHeadlineData, .three-ads, .three-promoted-ads, .thumb-ads, .thumbnailad, .tibu_ad, .ticket-ad, .tile--ad, .tile-ad, .tile-ad-container, .tileAdContainer, .tileAdWrap, .tileAds, .tile_AdBanner, .tile_ad_container, .tips_advertisement, .title-ad, .title_adbig, .tj_ad_box, .tj_ad_box_top, .tjads, .tl-ad, .tl-ad-dfp, .tl-ad-display-3, .tl-ad-render, .tm-ads, .tm_ad200_widget, .tm_topads_468, .tm_widget_ad200px, .tmg-ad, .tmg-ad-300x250, .tmg-ad-mpu, .tmnAdsenseContainer, .tmz-dart-ad, .tncms-region-ads, .tnt-ads-container, .toggle-adinmap, .toolad, .toolbar-ad, .toolsAd, .toolssponsor-ads, .top-300-ad, .top-ad, .top-ad-anchor, .top-ad-area, .top-ad-bloc, .top-ad-block, .top-ad-center, .top-ad-container, .top-ad-content, .top-ad-horizontal, .top-ad-inside, .top-ad-multiplex, .top-ad-right, .top-ad-sidebar, .top-ad-slot, .top-ad-space, .top-ad-sticky, .top-ad-unit, .top-ad-wrap, .top-ad-wrapper, .top-ad1, .top-adbox, .top-ads, .top-ads-bottom-bar, .top-ads-wrapper, .top-adsense, .top-adsense-banner, .top-adspace, .top-adv, .top-adverbox, .top-advert, .top-advertisement, .top-banner-468, .top-banner-ad, .top-banner-ad-container, .top-banner-ad-wrapper, .top-banner-add, .top-bar-ad-related, .top-box-right-ad, .top-content-adplace, .top-half-page-ad, .top-header-ad, .top-horiz-ad, .top-item-ad, .top-large-google-ad, .top-leaderboard-ad, .top-left-nav-ad, .top-menu-ads, .top-outer-ad-container, .top-primary-sponsored, .top-right-ad, .top-right-advert, .top-rightadvtsment, .top-sidebar-adbox, .top-treehouse-ad, .top-wide-ad-container, .top300ad, .topAD, .topAd728x90, .topAdBanner, .topAdCenter, .topAdContainer, .topAdIn, .topAdLeft, .topAdRight, .topAdWrap, .topAdWrapper, .topAdd, .topAds, .topAdvBox, .topAdvert, .topAdvertisement, .topAdvertistemt, .topAdverts, .topArticleAds, .topBannerAd, .topBannerAdSectionR, .topBarAd, .topBoxAdvertisement, .topHeaderLeaderADWrap, .topLeaderboardAd, .topNavRMAd, .topPC-adWrap, .topPagination_ad, .topRailAdSlot, .topRightAd, .top_Ad, .top_ad, .top_ad1, .top_ad_336x280, .top_ad_728, .top_ad_728_90, .top_ad_banner, .top_ad_big, .top_ad_disclaimer, .top_ad_div, .top_ad_holder, .top_ad_inner, .top_ad_label, .top_ad_list, .top_ad_long, .top_ad_post, .top_ad_responsive, .top_ad_seperate, .top_ad_short, .top_ad_wrap, .top_ad_wrapper, .top_adbox1, .top_adbox2, .top_adh, .top_ads, .top_adsense, .top_adv, .top_adv_content, .top_advert, .top_advertisement, .top_advertising_lb, .top_advertizing_cnt, .top_bar_ad, .top_big_ads, .top_container_ad, .top_corner_ad, .top_header_ad, .top_header_ad_inner, .top_right_ad, .top_rightad, .top_sponsor, .topad-area, .topad-bar, .topad-bg, .topad1, .topad2, .topadbar, .topadblock, .topadbox, .topadrow, .topads, .topads-spacer, .topadsection, .topadspace, .topadspot, .topadtara, .topadtxt, .topadtxt120, .topadtxt300, .topadtxt428, .topadtxt728, .topadvertisementsegment, .topbar-ad-unit, .topboardads, .topcontentadvertisement, .topfootad, .topicDetailsAdRight, .topic_inad, .topnavSponsor, .topratedBoxAD, .topsidebarad, .topstoriesad, .toptenAdBoxA, .tourFeatureAd, .tout-ad-embed, .tower-ad, .tower-ad-abs, .tower-ads-container, .towerAd, .towerAdLeft, .towerAds, .tower_ad, .tower_ad_disclaimer, .towerad, .tp-ad-label, .tp_ads, .tr-ad-adtech, .tr-ad-adtech-placement, .tr-ad-inset, .tr-sponsored, .trSpAD1, .track_adblock, .trafficAdSpot, .trafficjunky-ad, .trb_ar_sponsoredmod, .trb_gptAd, .trb_header_adBanner_combo, .trb_header_adBanner_large, .trb_masthead_adBanner, .trb_pageAdHolder, .trc-content-sponsored, .trc-content-sponsoredUB, .treeAdBlockWithBanner_right, .trending__ad, .tribal-ad, .trip_ad_center, .trueads, .ts-ad, .ts-ad-leaderboard, .ts-ad_unit_bigbox, .ts-banner_ad, .ts-featured_ad, .ts-sponsored-links, .ts-top-most-ads, .tsmAd, .tt_ads, .ttlAdsensel, .tto-sponsored-element, .tucadtext, .tvkidsArticlesBottomAd, .tvs-mpu, .twitter-ad, .two-col-ad-inArticle, .twoColumnAd, .two_ads, .twoadcoll, .twoadcolr, .tx-aa-adverts, .tx_smartadserver_pi1, .txt-ads, .txtAd, .txtAd5, .txtAds, .txt_ad, .txt_ads, .txtad_area, .txtadvertise, .tynt-ad-container, .type_ads_default, .type_adscontainer, .type_miniad, .type_promoads, .tz_ad300_widget, .tz_ad_widget, .uds-ad, .uds-ads, .ui-ad, .ukAds, .ukn-banner-ads, .ukn-inline-advert, .ult_vp_videoPlayerAD, .unSponsored, .under-player-ads, .under_ads, .undertimyads, .uniAdBox, .uniAds, .uniblue-text-ad, .unit-ad, .universalboxADVBOX01, .universalboxADVBOX03, .universalboxADVBOX04a, .unspoken-adplace, .upcloo-adv-content, .upper-ad-space, .urban-ad-rect, .urban-ad-top, .us-advertisement, .us-txt-ad, .useful_banner_manager_banners_rotation, .useful_banner_manager_rotation_widget, .useful_banner_manager_widget, .usenext, .v5rc_336x280ad, .vAd_160x600, .vAds, .v_ad, .vadvert, .variableHeightAd, .vbox-verticalad, .vce-header-ads, .ve2_post_adsense, .vert-ad, .vert-ad-ttl, .vert-ads, .vert-adsBlock, .vertad, .vertical-adsense, .verticalAd, .verticalAdText, .vertical_ad, .vertical_ads, .verticalad, .verysmallads, .vhs_small_ad, .vidadtext, .video-about-ad, .video-ad-short, .video-ads, .video-ads-container, .video-ads-wrapper, .video-adtech-mpu-ad, .video-innerAd-320x250, .video-player-ad-center, .videoAd-wrapper, .videoBoxAd, .videoPauseAd, .video_ad, .video_ad_fadein, .video_ads, .video_ads_overdiv, .video_ads_overdiv2, .video_advertisement_box, .video_detail_box_ads, .video_top_ad, .videoadbox, .videos-ad, .videos-ad-wrap, .view-Advertisment, .view-ad, .view-advertisements, .view-advertisements-300, .view-advertorials, .view-adverts, .view-advt-story-bottom, .view-custom-advertisement, .view-display-id-ads_all, .view-id-Advertisment, .view-id-ad, .view-id-advertisements, .view-id-advertisements_300, .view-id-advt_story_bottom, .view-id-custom_advertisement, .view-image-ads, .view-promo-mpu-right, .view-site-ads, .view-video-advertisements, .viewContentItemAd, .view_ad, .view_ads_advertisements, .view_ads_bottom_bg, .view_ads_bottom_bg_middle, .view_ads_content_bg, .view_ads_top_bg, .view_ads_top_bg_middle, .view_rig_ad, .views-field-field-ad, .views-field-field-adbox-1, .views-field-field-adbox-2, .views-field-field-advertisement-image, .views-field-field-image-ad, .vip-club-ad, .virgin-mpu, .visor-breaker-ad, .visuaAD400, .visuaAD900, .vl-ad-item, .vmp-ad, .vod_ad, .vs-advert-300x250, .vs_dfp_standard_postbit_ad, .vsw-ads, .vswAdContainer, .vt_h1_ad, .vuukle-ad-block, .vuukle-ads, .vw-header-ads-leader-board, .vw-header-ads-wrapper, .vw-single-header-ads, .vxp_ad300x250, .w-ad-box, .w-content--ad, .wAdvert, .w_AdExternal, .wa_adsbottom, .wahAd, .wahAdRight, .wallAd, .wall_ad, .wall_ad_hd, .wallad, .wantads, .waterfall-ad-anchor, .wazi-ad-link, .wd-adunit, .wdca_ad_item, .wdca_custom_ad, .wdp_ad, .wdp_adDiv, .wdt_ads, .weather-ad-wrapper, .weather-sponsor-ad, .weather-sponsorDiv, .weatherAdSpot, .weather_ad, .weatherad, .web-result-sponsored, .webad-cnt, .webads336x280, .webadvert-container, .webit-ads, .webpart-wrap-advert, .well-ad, .wfb-ad, .wg-ad-square, .wh_ad, .white-ad-block, .wide-ad, .wide-ad-container, .wide-ad-outer, .wide-ad2015, .wide-advert, .wide-footer-ad, .wide-header-ad, .wide-skyscraper-ad, .wideAd, .wideAdTable, .widePageAd, .wide_ad, .wide_ad_unit, .wide_ad_unit_top, .wide_ads, .wide_google_ads, .wide_grey_ad_box, .wide_sponsors, .widead, .wideadbox, .widget-ad, .widget-ad-codes, .widget-ad-sky, .widget-ad-zone, .widget-ad300x250, .widget-adcode, .widget-ads, .widget-adsense, .widget-adv, .widget-advert-728, .widget-advert-970, .widget-advertisement, .widget-ami-newsmax, .widget-entry-ads-160, .widget-gpt2-ami-ads, .widget-group-Ads, .widget-highlight-ads, .widget-pane-section-ad-content, .widget-sponsor, .widget-text-ad, .widget1-ad, .widget10-ad, .widget4-ad, .widget6-ad, .widget7-ad, .widgetAD, .widgetAdScrollContainer, .widgetYahooAds, .widget_ad, .widget_ad-widget, .widget_ad125, .widget_ad300, .widget_ad_300x250_atf, .widget_ad_300x250_btf, .widget_ad_300x250_btf_b, .widget_ad_boxes_widget, .widget_ad_rotator, .widget_ad_widget, .widget_admanagerwidget, .widget_adrotate_widgets, .widget_ads, .widget_adsblock, .widget_adsensem, .widget_adsensewidget, .widget_adsingle, .widget_adv_location, .widget_advert, .widget_advert_content, .widget_advert_widget, .widget_advertisement, .widget_advertisements, .widget_advertisment, .widget_advwidget, .widget_adwidget, .widget_appmanager_sponsoredpostswidget, .widget_bestgoogleadsense, .widget_boss_banner_ad, .widget_catchbox_adwidget, .widget_cevo_contentad, .widget_cpxadvert_widgets, .widget_customad_widget, .widget_customadvertising, .widget_cxad, .widget_dfp, .widget_dfp_lb-widget, .widget_econaabachoadswidget, .widget_emads, .widget_etcenteredadwidget, .widget_evolve_ad_gpt_widget, .widget_fearless_responsive_image_ad, .widget_googleads, .widget_ima_ads, .widget_internationaladserverwidget, .widget_ione-dart-ad, .widget_island_ad, .widget_jr_125ads, .widget_maxbannerads, .widget_nb-ads, .widget_new_sponsored_content, .widget_openxwpwidget, .widget_plugrush_widget, .widget_postmedia_layouts_ad, .widget_sdac_bottom_ad_widget, .widget_sdac_companion_video_ad_widget, .widget_sdac_footer_ads_widget, .widget_sdac_skyscraper_ad_widget, .widget_sdac_top_ad_widget, .widget_sej_sidebar_ad, .widget_sidebarad_300x250, .widget_sidebarad_300x600, .widget_sidebaradwidget, .widget_sponsored_content, .widget_supernews_ad, .widget_taboola, .widget_text_adsense, .widget_thesun_dfp_ad_widget, .widget_uds-ads, .widget_vb_sidebar_ad, .widget_wnd_ad_widget, .widget_wp_ads_gpt_widget, .widget_wpshower_ad, .widgetads, .width-ad-slug, .wikia-ad, .wikia_ad_placeholder, .wingadblock, .wis_adControl, .with-background-ads, .with-wrapper-ads, .withAds, .wixAdsdesktopBottomAd, .wl-ad, .wn-ad, .wnIframeAd, .wnMultiAd, .wnad, .wp125_write_ads_widget, .wp125ad, .wp125ad_1, .wp125ad_2, .wpInsertAdWidget, .wpInsertInPostAd, .wp_bannerize, .wpadvert, .wpbrad, .wpbrad-ad, .wpbrad-zone, .wpd-advertisement, .wpfp_custom_ad, .wpi_ads, .wpmrec, .wpn_ad_content, .wppaszone, .wpproadszone, .wptouch-ad, .wpx-bannerize, .wpx_bannerize, .wrap-ad, .wrap-ads, .wrap_boxad, .wrapad, .wrapper-ad, .wrapper-ad-sidecol, .wrapper-google-ads, .wrapper-sidebar_ads_box, .wrapper-sidebar_ads_half-page, .wrapper_ad, .wrb1_x1_adv, .wrb1_x7_adv, .wrb2_ls1_adv, .wrb2_ls3_adv, .wrb2_x1_adv, .wrb3_ls1_adv, .wrb6_x1_adv, .ws-ad, .wsSearchResultsRightSponsoredLinks, .wsSponsoredLinksRight, .wsTopSposoredLinks, .ws_contentAd660, .wx-adchoices, .wx-gptADS, .x-ad, .x-home-ad__content, .x-home-ad__content-inner, .x-tile__advert, .x01-ad, .x03-adunit, .x04-adunit, .x81_ad_detail, .xads-blk-bottom-hld, .xads-blk-top-hld, .xads-blk-top2-hld, .xads-blk1, .xads-blk2, .xads-ojedn, .xmlad, .xs_epic_circ_ad, .xs_epic_sponsor_label, .xtopadvert, .y-ads, .y-ads-wide, .y5_ads, .y5_ads2, .y7-advertisement, .y7adHEAD, .y7adS, .y7s-lrec, .yaAds, .yad-sponsored, .yahoo-ad-leader-north, .yahoo-ad-leader-south, .yahoo-ad-lrec-north, .yahoo-banner-ad-container, .yahoo-sponsored, .yahoo-sponsored-links, .yahoo-sponsored-result, .yahooAd, .yahooAds, .yahooContentMatch, .yahoo_ad, .yahoo_ads, .yahooad, .yahooad-image, .yahooad-urlline, .yahooads, .yahootextads_content_bottom, .yam-plus-ad-container, .yan-sponsored, .yat-ad, .yellow_ad, .yfi-fp-ad-logo, .ygrp-ad, .yieldads-160x600, .yieldads-728x90, .yl-lrec-wrap, .yls-sponlink, .yom-ad, .yom-ad-LREC, .yom-ad-LREC2, .yom-ad-LREC3, .yom-ad-MREC2, .yom-ad-moneyball, .youradhere, .youtubeSuperLeaderBoardAdHolder, .youtubeSuperLeaderOverallAdArea, .yrail_ad_wrap, .yrail_ads, .ysmsponsor, .ysp-dynamic-ad, .ysponsor, .yt-adsfull-widget, .ytp-ad-progress-list, .yui3-ad, .yw-ad, .z-sponsored-block, .zRightAdNote, .zc-grid-ad, .zc-grid-position-ad, .zem_rp_promoted, .zerg-colm, .zerg-widget, .zeti-ads, bottomadblock, topadblock, #rc-row-container, .impo-b-overlay, .impo-b-stitial, .rc-item-wrapper, .rec-sponsored, .rec_article_footer, .rec_article_right, .rec_container__right, .rec_container_footer, .rec_container_right, .rec_title_footer, AMP-AD, .commerce-inset, #mobile-swipe-banner, .component-ddb-300x250-v2, .component-ddb-728x90-v2, .ddb, .brandpost_inarticle, #rhs_whistleout_widget, #wo-widget-wrap, #magnify_widget_playlist_item_companion, .l-container > #fishtank, #center_col > #\5f Emc, #center_col > #main > .dfrd > .mnr-c > .c._oc._zs, #center_col > #taw > #tvcap > .rscontainer, #cnt #center_col > #res > #topstuff > .ts, #cnt #center_col > #taw > #tvcap > .c._oc._Lp, #resultspanel > #topads, #rhs_block .mod > .gws-local-hotels__booking-module, #rhs_block .xpdopen > ._OKe > div > .mod > ._yYf, #rhs_block > #mbEnd, #rhs_block > ol > .rhsvw > .kp-blk > .xpdopen > ._OKe > ol > ._DJe > .luhb-div, #tads.c, #tadsb.c, #tadsto.c, #topstuff > #tads, .GB3L-QEDGY .GB3L-QEDF- > .GB3L-QEDE-, .GFYY1SVD2 > .GFYY1SVC2 > .GFYY1SVF5, .GFYY1SVE2 > .GFYY1SVD2 > .GFYY1SVG5, .GHOFUQ5BG2 > .GHOFUQ5BF2 > .GHOFUQ5BG5, .GJJKPX2N1 > .GJJKPX2M1 > .GJJKPX2P4, .GKJYXHBF2 > .GKJYXHBE2 > .GKJYXHBH5, .GPMV2XEDA2 > .GPMV2XEDP1 > .GPMV2XEDJBB, .commercial-unit-desktop-rhs, .commercial-unit-desktop-top, .commercial-unit-mobile-bottom, .commercial-unit-mobile-top, .mw > #rcnt > #center_col > #taw > #tvcap > .c, .mw > #rcnt > #center_col > #taw > .c, .rscontainer > .ellip, #ads > .dose > .dosesingle, #content > #center > .dose > .dosesingle, #content > #right > .dose > .dosesingle, .trc_rbox .syndicatedItem, .trc_rbox_border_elm .syndicatedItem, .trc_rbox_div .syndicatedItem, .trc_rbox_div .syndicatedItemUB, #MAIN.ShowTopic > .ad, #boxes-box-zergnet_module, #right_rail-zergnet, #zergnet, #zergnet-widget, #zergnet-wrapper, .ZERGNET, .component-zergnet, .content-zergnet, .js-footer-zerg, .module-zerg, .td-zergnet, .widget-ami-zergnet, .widget_ok_zergnet_widget, .zergmod, .zergnet, .zergnet-holder, .zergnet-row, .zergnet-widget, .zergnet-widget-container, .zergnet-widget__header, .zergnet-widget__subtitle, .zergnetBLock, .zergnetpower, .zergpowered, #Class_1_ad>.footad, #body>#myads, #topad>.tad,.box1>.ad, #foot>#foot2>#Class_1_ad, #floatDiv>#rightFloat, #top>.topSponsor.mt10,.mainArea.px9>.bottomSponsor, .pause-ad, .pause-ad, #aside_ad, .a_fr.a_cb, #ad_corner_close, .adarea,.adarea_top, #lovexin1,#lovexin2, .m_ad, .ad1,.ad2,.ad3,.ad4,.ad5,.ad6,.ad7,.ad8,.ad9, .ad_240_h, .side-Rad, .widget_ad_slot_wrapper, .gg01,.gg02,.gg03,.gg04,.gg05,.gg06,.gg07,.gg08,.gg09,#_SNYU_Ad_Wrap, .random-box>.random-banner, .top-ads-list,.palm01-ad,.topAd950, .gonglue_rightad, #AdZoneRa,#AdZoneRb,#AdZoneRc,#AdZoneRd,#AdZoneRe,#AdZoneRf,#AdZoneRg, .absolute.a_cover, #QQCOM_Width3, #auto_gen_6, .l_qq_com, #cj_ad, .right_ad_lefttext, .right_ad_righttext, .AdTop-Article-QQ, .business-Article-QQ, .qiye-Article-QQ, .AdBox-Article-QQ, .adclass, .ad1, .ads5, .adv, .ads220_60, .ad-h60, .ad-h65, .ggs, .news_ad_box, #XianAd, .Ad3Top-Article-QQ, .AdTop2-Article-QQ, .adbutton-Aritcle-QQ, #AdRight-Article-QQ, .sidBoxNoborder.mar-b8, #ent_ad, .plrad, .ad300, #top_ad1,#top_ad2,#top_ad3,#top_ad4,#top_ad5,#top_ad6,#top_ad7,#top_ad8,#top_ad9, #mid_ad1,#mid_ad2,#mid_ad3,#mid_ad4,#mid_ad5,#mid_ad6,#mid_ad7,#mid_ad8,#mid_ad9, #ads1,#ads2,#ads3,#ads4,#ads5,#ads6,#ads7,#ads8,#ads9, .dlAd,.changeAd, .unionCpv, #Advertisement, .ad_headerbanner,#ad_headerbanner, #ads-top, #ads-bot, .adBanner, #topAd, .top_ad, .topAds, .topAd, .ad_column, #ad1, #ad2, #ad3, #ad4, #ad5, #ad6, #ad7, #ad8, #ad9, .ad_footerbanner, #adleft, #adright, .advleft, .advright, .ad980X60, .banner-ad, .top-ad, #adright, #AdLayer1, #AdLayer2, #AdLayer3, .txtad, .guanggao, #guanggao, .adclass, .ad950, .guangg, .header-ads-top, #adleft, #adright, #ad_show, .ad_pic, #fullScreenAd, #topADImg, .delayadv, #vplayad, .jadv, #bottomads, .ad_column, .ad_text, div.adA.area, .adBox, .adRight,.adLeft, .banner-ads, .right_ad, .left_ad, .content_ad, .post-top-gg, .col_ad, .block_ad, .adBlue, .mar_ad, .adItem, .ggarea, .adiframe, #bottom_ad,.bottom_ad, .crumb_ad, .topadna,.topadbod, .topadbod, .crazy_ad_layer,#crazy_ad_layer, .bannerad, #crazy_ad_float,.crazy_ad_float, .main_ad, .topads, .head-ad, #bg_ad, .ad_pic, .ad_top, #baiduSpFrame, .flashad,#flashad, #ShowAD, #ad_240, .wp.a_f, .a_mu, #hd_ad, #top_ads,#header_ad, #adbanner,#adbanner_1, #Left_bottomAd,#Right_bottomAd, #ad_alimama,#vipTip, .ad_pip, #show-gg, .ad-box, .advbox, .widget-ads.banner, .a760x100,.a200x375,.a760x100,.a200x100, .ad_left,.ad_right, .g_ad { display: none !important; } </style><style type="text/css">#fwin_popad_7ree + #fwin_dialog, #leftFloat + #rightFloat, #left_float + #right_float, #navcontainer + .moneyarea, #rightCouple + #leftFloat, #right_couple + #left_float, #table1[width="468"][height="50"], #table1[width="794"][height="60"], #table1[width="812"][height="50"], ._cggp, ._ggs, ._popIn_recommend_article_ad, ._popIn_recommend_article_ad_reserved, .f-sign-cont[data-dysign-adid], .his-sign-cont[data-dysign-adid], .iqshwad-div + .recommend-list, A[href*=".com/?Agent="], a[href*=".com/?Extend="], a[href*=".com/Register.aspx?aid="], a[href*=".com/Register/?a="], a[href*=".com/Register?a="], a[href*=".com?aff="], a[href*=".com?intr="], a[href*="/?INTR="], a[href*="/?Intr="], a[href*="/?aff="], a[href*="/?intr="], a[href^="/freeone/htm/"], body[onload*="u()"] > #x, div[id^="ad_thread"], script + #rbbox, script + .sptable[cellpadding="5"], #Meebo\:AdElement\.Root, #_ads, #ad_text:not(textarea), #adframe:not(frameset), .AdBody:not(body), .__xX20sponsored20banners, ._ap_adrecover_ad, ._articleAdvert, ._bannerAds, ._bottom_ad_wrapper, ._fullsquaread, ._iub_cs_activate_google_ads, ._top_ad_wrapper, .ob_container a[data-redirect^="http://paid.outbrain.com/network/redir?"], .plista_widget_belowArticleRelaunch_item[data-type="pet"], .wsj-ad:not(.adActivate), [lazy-ad="lefttop_banner"], [onclick^="window.open('http://adultfriendfinder.com/search/"], a[data-obtrack^="http://paid.outbrain.com/network/redir?"], a[data-redirect^="this.href='http://paid.outbrain.com/network/redir?"], a[data-url^="http://paid.outbrain.com/network/redir?"], a[data-url^="http://paid.outbrain.com/network/redir?"] + .author, a[data-widget-outbrain-redirect^="http://paid.outbrain.com/network/redir?"], a[href$="/vghd.shtml"], a[href*=".adk2x.com/"], a[href*=".adsrv.eacdn.com/"] > img, a[href*=".qertewrt.com/"], a[href*="/adrotate-out.php?"], a[href*="/cmd.php?ad="], a[href*="=Adtracker"], a[href*="ad2upapp.com/"], a[href*="emprestimo.eu"], a[href*="friendlyduck.com"], a[href*="googleme.eu"], a[href*="letsadvertisetogether.com"], a[href^=" http://ads.ad-center.com/"], a[href^=" http://n47adshostnet.com/"], a[href^="//adbit.co/?a=Advertise&"], a[href^="//ads.ad-center.com/"], a[href^="//api.ad-goi.com/"], a[href^="//srv.buysellads.com/"], a[href^="//t.MtagMonetizationA.com/"], a[href^="http://1phads.com/"], a[href^="http://360ads.go2cloud.org/"], a[href^="http://3wr110.net/"], a[href^="http://NowDownloadAll.com"], a[href^="http://a.adquantix.com/"], a[href^="http://abc2.mobile-10.com/"], a[href^="http://ad-apac.doubleclick.net/"], a[href^="http://ad-emea.doubleclick.net/"], a[href^="http://ad.au.doubleclick.net/"], a[href^="http://ad.doubleclick.net/"], a[href^="http://ad.yieldmanager.com/"], a[href^="http://adclick.g.doubleclick.net/"], a[href^="http://adexprt.me/"], a[href^="http://adf.ly/?id="], a[href^="http://adfarm.mediaplex.com/"], a[href^="http://adlev.neodatagroup.com/"], a[href^="http://admingame.info/"], a[href^="http://adprovider.adlure.net/"], a[href^="http://adrunnr.com/"], a[href^="http://ads.activtrades.com/"], a[href^="http://ads.ad-center.com/"], a[href^="http://ads.affbuzzads.com/"], a[href^="http://ads.betfair.com/redirect.aspx?"], a[href^="http://ads.expekt.com/affiliates/"], a[href^="http://ads.integral-marketing.com/"], a[href^="http://ads.pheedo.com/"], a[href^="http://ads.sprintrade.com/"], a[href^="http://ads2.williamhill.com/redirect.aspx?"], a[href^="http://adserver.adtech.de/"], a[href^="http://adserver.adtechus.com/"], a[href^="http://adserver.itsfogo.com/"], a[href^="http://adserving.liveuniversenetwork.com/"], a[href^="http://adserving.unibet.com/"], a[href^="http://adsrv.keycaptcha.com"], a[href^="http://adtrack123.pl/"], a[href^="http://adtrackone.eu/"], a[href^="http://adtransfer.net/"], a[href^="http://adultfriendfinder.com/p/register.cgi?pid="], a[href^="http://affiliate.coral.co.uk/processing/"], a[href^="http://affiliate.glbtracker.com/"], a[href^="http://affiliate.godaddy.com/"], a[href^="http://affiliates.pinnaclesports.com/processing/"], a[href^="http://affiliates.score-affiliates.com/"], a[href^="http://aflrm.com/"], a[href^="http://amzn.to/"] > img[src^="data"], a[href^="http://api.ringtonematcher.com/"], a[href^="http://at.atwola.com/"], a[href^="http://b.bestcompleteusa.info/"], a[href^="http://banners.victor.com/processing/"], a[href^="http://bc.vc/?r="], a[href^="http://bcp.crwdcntrl.net/"], a[href^="http://bestorican.com/"], a[href^="http://bluehost.com/track/"], a[href^="http://bonusfapturbo.nmvsite.com/"], a[href^="http://bs.serving-sys.com/"], a[href^="http://buysellads.com/"], a[href^="http://c.actiondesk.com/"], a[href^="http://c.ketads.com/"], a[href^="http://callville.xyz/"], a[href^="http://campaign.bharatmatrimony.com/cbstrack/"], a[href^="http://campaign.bharatmatrimony.com/track/"], a[href^="http://casino-x.com/?partner"], a[href^="http://cdn.adsrvmedia.net/"], a[href^="http://cdn.adstract.com/"], a[href^="http://cdn3.adbrau.com/"], a[href^="http://cdn3.adexprts.com/"], a[href^="http://centertrust.xyz/"], a[href^="http://chaturbate.com/affiliates/"], a[href^="http://cinema.friendscout24.de?"], a[href^="http://click.guamwnvgashbkashawhgkhahshmashcas.pw/"], a[href^="http://clickandjoinyourgirl.com/"], a[href^="http://clicks.binarypromos.com/"], a[href^="http://clicks.guamwnvgashbkashawhgkhahshmashcas.pw/"], a[href^="http://clickserv.sitescout.com/"], a[href^="http://clk.directrev.com/"], a[href^="http://clkmon.com/adServe/"], a[href^="http://codec.codecm.com/"], a[href^="http://connectlinking6.com/"], a[href^="http://contractallsticker.net/"], a[href^="http://cpaway.afftrack.com/"], a[href^="http://d2.zedo.com/"], a[href^="http://data.ad.yieldmanager.net/"], a[href^="http://data.committeemenencyclopedicrepertory.info/"], a[href^="http://data.linoleictanzaniatitanic.com/"], a[href^="http://databass.info/"], a[href^="http://ddownload39.club/"], a[href^="http://dethao.com/"], a[href^="http://dftrck.com/"], a[href^="http://down1oads.com/"], a[href^="http://download-performance.com/"], a[href^="http://duckcash.eu/AF_"], a[href^="http://dwn.pushtraffic.net/"], a[href^="http://easydownload4you.com/"], a[href^="http://eclkmpsa.com/"], a[href^="http://elite-sex-finder.com/?"], a[href^="http://elitefuckbook.com/"], a[href^="http://engine.newsmaxfeednetwork.com/"], a[href^="http://feedads.g.doubleclick.net/"], a[href^="http://fileloadr.com/"], a[href^="http://fileupnow.rocks/"], a[href^="http://finaljuyu.com/"], a[href^="http://findersocket.com/"], a[href^="http://freesoftwarelive.com/"], a[href^="http://fsoft4down.com/"], a[href^="http://fusionads.net"], a[href^="http://galleries.pinballpublishernetwork.com/"], a[href^="http://galleries.securewebsiteaccess.com/"], a[href^="http://games.ucoz.ru/"][target="_blank"], a[href^="http://gca.sh/user/register?ref="], a[href^="http://get.slickvpn.com/"], a[href^="http://getlinksinaseconds.com/"], a[href^="http://go.ad2up.com/"], a[href^="http://go.mobisla.com/"], a[href^="http://go.oclaserver.com/"], a[href^="http://go.seomojo.com/tracking202/"], a[href^="http://goldmoney.com/?gmrefcode="], a[href^="http://green.trafficinvest.com/"], a[href^="http://greensmoke.com/"], a[href^="http://guideways.info/"], a[href^="http://hd-plugins.com/download/"], a[href^="http://hdplugin.flashplayer-updates.com/"], a[href^="http://hyperlinksecure.com/go/"], a[href^="http://imads.integral-marketing.com/"], a[href^="http://install.securewebsiteaccess.com/"], a[href^="http://istri.it/?"], a[href^="http://jobitem.org/"], a[href^="http://join3.bannedsextapes.com/track/"], a[href^="http://k2s.cc/pr/"], a[href^="http://keep2share.cc/pr/"], a[href^="http://landingpagegenius.com/"], a[href^="http://latestdownloads.net/download.php?"], a[href^="http://linksnappy.com/?ref="], a[href^="http://liversely.com/"], a[href^="http://liversely.net/"], a[href^="http://lp.ezdownloadpro.info/"], a[href^="http://lp.ilivid.com/"], a[href^="http://lp.ncdownloader.com/"], a[href^="http://marketgid.com"], a[href^="http://mgid.com/"], a[href^="http://mmo123.co/"], a[href^="http://mo8mwxi1.com/"], a[href^="http://mojofun.info/"], a[href^="http://n.admagnet.net/"], a[href^="http://n217adserv.com/"], a[href^="http://onclickads.net/"], a[href^="http://online.ladbrokes.com/promoRedirect?"], a[href^="http://paid.outbrain.com/network/redir?"], a[href^="http://partner.sbaffiliates.com/"], a[href^="http://pokershibes.com/index.php?ref="], a[href^="http://prochina.link/"], a[href^="http://prochina.space/"], a[href^="http://promos.bwin.com/"], a[href^="http://prousa.work/"], a[href^="http://pubads.g.doubleclick.net/"], a[href^="http://pwrads.net/"], a[href^="http://record.betsafe.com/"], a[href^="http://record.commissionking.com/"], a[href^="http://record.sportsbetaffiliates.com.au/"], a[href^="http://refer.webhostingbuzz.com/"], a[href^="http://ryushare.com/affiliate.python"], a[href^="http://secure.hostgator.com/~affiliat/"], a[href^="http://secure.signup-page.com/"], a[href^="http://secure.signup-way.com/"], a[href^="http://see-work.info/"], a[href^="http://serve.williamhill.com/promoRedirect?"], a[href^="http://server.cpmstar.com/click.aspx?poolid="], a[href^="http://servicegetbook.net/"], a[href^="http://sharesuper.info/"], a[href^="http://srvpub.com/"], a[href^="http://stateresolver.link/"], a[href^="http://t.mdn2015x1.com/"], a[href^="http://t.mdn2015x2.com/"], a[href^="http://t.mdn2015x3.com/"], a[href^="http://t.wowtrk.com/"], a[href^="http://taboola-"][href*="/redirect.php?app.type="], a[href^="http://tezfiles.com/pr/"], a[href^="http://tour.affbuzzads.com/"], a[href^="http://track.adform.net/"], a[href^="http://track.incognitovpn.com/"], a[href^="http://tracking.crazylead.com/"], a[href^="http://tracking.deltamediallc.com/"], a[href^="http://tracking.toroadvertising.com/"], a[href^="http://ul.to/ref/"], a[href^="http://uploaded.net/ref/"], a[href^="http://us.marketgid.com"], a[href^="http://web.adblade.com/"], a[href^="http://websitedhoome.com/"], a[href^="http://webtrackerplus.com/"], a[href^="http://wgpartner.com/"], a[href^="http://www.123-reg.co.uk/affiliate2.cgi"], a[href^="http://www.1clickdownloader.com/"], a[href^="http://www.1clickmoviedownloader.info/"], a[href^="http://www.FriendlyDuck.com/AF_"], a[href^="http://www.TwinPlan.com/AF_"], a[href^="http://www.adbrite.com/mb/commerce/purchase_form.php?"], a[href^="http://www.adshost2.com/"], a[href^="http://www.adxpansion.com"], a[href^="http://www.affbuzzads.com/affiliate/"], a[href^="http://www.affiliates1128.com/processing/"], a[href^="http://www.amazon.co.uk/exec/obidos/external-search?"], a[href^="http://www.babylon.com/welcome/index?affID"], a[href^="http://www.badoink.com/go.php?"], a[href^="http://www.bet365.com/home/?affiliate"], a[href^="http://www.bet365.com/home/default.asp?affiliate="], a[href^="http://www.brightwheel.info/"], a[href^="http://www.cash-duck.com/AF_"], a[href^="http://www.clickansave.net/"], a[href^="http://www.clkads.com/adServe/"], a[href^="http://www.coinducks.com/AF_"], a[href^="http://www.dealcent.com/register.php?affid="], a[href^="http://www.dl-provider.com/search/"], a[href^="http://www.down1oads.com/"], a[href^="http://www.download-provider.org/"], a[href^="http://www.downloadplayer1.com/"], a[href^="http://www.downloadthesefiles.com/"], a[href^="http://www.downloadweb.org/"], a[href^="http://www.drowle.com/"], a[href^="http://www.duckcash.eu/AF_"], a[href^="http://www.easydownloadnow.com/"], a[href^="http://www.epicgameads.com/"], a[href^="http://www.faceporn.net/free?"], a[href^="http://www.fbooksluts.com/"], a[href^="http://www.firstclass-download.com/"], a[href^="http://www.firstload.com/affiliate/"], a[href^="http://www.firstload.de/affiliate/"], a[href^="http://www.flashx.tv/downloadthis"], a[href^="http://www.fleshlight.com/"], a[href^="http://www.fonts.com/BannerScript/"], a[href^="http://www.fpcTraffic2.com/blind/in.cgi?"], a[href^="http://www.freefilesdownloader.com/"], a[href^="http://www.friendlyadvertisements.com/"], a[href^="http://www.friendlyquacks.com/"], a[href^="http://www.gamebookers.com/cgi-bin/intro.cgi?"], a[href^="http://www.getyourguide.com/?partner_id="], a[href^="http://www.graboid.com/affiliates/"], a[href^="http://www.greenmangaming.com/?tap_a="], a[href^="http://www.idownloadplay.com/"], a[href^="http://www.incredimail.com/?id="], a[href^="http://www.ireel.com/signup?ref"], a[href^="http://www.linkbucks.com/referral/"], a[href^="http://www.liutilities.com/"], a[href^="http://www.liversely.net/"], a[href^="http://www.menaon.com/installs/"], a[href^="http://www.mobileandinternetadvertising.com/"], a[href^="http://www.moneyducks.com/"], a[href^="http://www.my-dirty-hobby.com/?sub="], a[href^="http://www.myfreepaysite.com/sfw.php?aid"], a[href^="http://www.myfreepaysite.com/sfw_int.php?aid"], a[href^="http://www.mysuperpharm.com/"], a[href^="http://www.myvpn.pro/"], a[href^="http://www.on2url.com/app/adtrack.asp"], a[href^="http://www.paddypower.com/?AFF_ID="], a[href^="http://www.pheedo.com/"], a[href^="http://www.pinkvisualgames.com/?revid="], a[href^="http://www.pinkvisualpad.com/?revid="], a[href^="http://www.plus500.com/?id="], a[href^="http://www.quick-torrent.com/download.html?aff"], a[href^="http://www.revenuehits.com/"], a[href^="http://www.richducks.com/"], a[href^="http://www.ringtonematcher.com/"], a[href^="http://www.roboform.com/php/land.php"], a[href^="http://www.seekbang.com/cs/"], a[href^="http://www.sex.com/?utm_"], a[href^="http://www.sex.com/pics/?utm_"], a[href^="http://www.sex.com/videos/?utm_"], a[href^="http://www.sexgangsters.com/?pid="], a[href^="http://www.sfippa.com/"], a[href^="http://www.socialsex.com/"], a[href^="http://www.streamate.com/exports/"], a[href^="http://www.streamtunerhd.com/signup?"], a[href^="http://www.terraclicks.com/"], a[href^="http://www.text-link-ads.com/"], a[href^="http://www.tirerack.com/affiliates/"], a[href^="http://www.torntv-downloader.com/"], a[href^="http://www.torntvdl.com/"], a[href^="http://www.twinplan.com/AF_"], a[href^="http://www.uniblue.com/cm/"], a[href^="http://www.urmediazone.com/signup"], a[href^="http://www.usearchmedia.com/signup?"], a[href^="http://www.wantstraffic.com/"], a[href^="http://www.webtrackerplus.com/"], a[href^="http://www.xmediaserve.com/"], a[href^="http://www.yourfuckbook.com/?"], a[href^="http://www1.clickdownloader.com/"], a[href^="http://wxdownloadmanager.com/dl/"], a[href^="http://xads.zedo.com/"], a[href^="http://yads.zedo.com/"], a[href^="http://z1.zedo.com/"], a[href^="http://zevera.com/afi.html"], a[href^="https://ad.atdmt.com/"], a[href^="https://ad.doubleclick.net/"], a[href^="https://adhealers.com/"], a[href^="https://affiliates.bet-at-home.com/processing/"], a[href^="https://atomidownload.com/"], a[href^="https://bs.serving-sys.com"], a[href^="https://dediseedbox.com/clients/aff.php?"], a[href^="https://dltags.com/"], a[href^="https://go.ad2up.com/"], a[href^="https://paid.outbrain.com/network/redir?"], a[href^="https://secure.eveonline.com/ft/?aid="], a[href^="https://trackjs.com/?utm_source"], a[href^="https://www.FriendlyDuck.com/AF_"], a[href^="https://www.dsct1.com/"], a[href^="https://www.firstload.com/affiliate/"], a[href^="https://www.googleadservices.com/pagead/aclk?"], a[href^="https://www.oboom.com/ad/"], a[href^="https://www.secureupload.eu/suprerefid="], a[href^="https://www.share-online.biz/affiliate/"], a[onmousedown^="this.href='/wp-content/embed-ad-content/"], a[onmousedown^="this.href='http://paid.outbrain.com/network/redir?"][target="_blank"], a[onmousedown^="this.href='http://paid.outbrain.com/network/redir?"][target="_blank"] + .ob_source, a[onmousedown^="this.href='http://staffpicks.outbrain.com/network/redir?"][target="_blank"], a[onmousedown^="this.href='http://staffpicks.outbrain.com/network/redir?"][target="_blank"] + .ob_source, a[onmousedown^="this.href='https://paid.outbrain.com/network/redir?"][target="_blank"], a[onmousedown^="this.href='https://paid.outbrain.com/network/redir?"][target="_blank"] + .ob_source, a[style="display:block;width:300px;min-height:250px"][href^="http://li.cnet.com/click?"], a[target="_blank"][href^="http://api.taboola.com/"], a[target="_blank"][onmousedown="this.href^='http://paid.outbrain.com/network/redir?"], aside[id^="div-gpt-ad"], div[class^="gemini-ad"], div[id^="ADV-SLOT-"], div[id^="MarketGid"], div[id^="YFBMSN"], div[id^="acm-ad-tag-"], div[id^="ad-server-"], div[id^="ad_script_"], div[id^="adrotate_widgets-"], div[id^="ads250_250-widget"], div[id^="cns_ads_"], div[id^="dfp-ad-"], div[id^="dfp-slot-"], div[id^="div-adtech-ad-"], div[id^="div-gpt-ad"], div[id^="div_ad_stack_"], div[id^="div_openx_ad_"], div[id^="dmRosAdWrapper"], div[id^="google_dfp_"], div[id^="proadszone-"], div[itemtype="http://schema.org/WPAdBlock"], div[itemtype="http://www.schema.org/WPAdBlock"], iframe[id^="google_ads_frame"], iframe[id^="google_ads_iframe"], iframe[src^="http://ad.yieldmanager.com/"], iframe[src^="http://cdn1.adexprt.com/"], iframe[src^="http://cdn2.adexprt.com/"], img[alt^="Fuckbook"], input[onclick^="window.open('http://www.FriendlyDuck.com/AF_"], input[onclick^="window.open('http://www.friendlyduck.com/AF_"], p[id^="div-gpt-ad-"], script[src^="http://free-shoutbox.net/app/webroot/shoutbox/sb.php?shoutbox="] + #freeshoutbox_content, #\5f _nq__hh[style="display:block!important"], a[href*=".trust.zone"], .rc-cta[data-target], [onclick*="content.ad/"], a[href^="http://internalredirect.site/"], a[href^="http://rekoverr.com/"], div > [class][onclick*=".updateAnalyticsEvents"], div[class$="dealnews"] > .dealnews, .gbfwa > div[class$="_item"], iframe[src^="http://static.mozo.com.au/strips/"], #main-content > [style="padding:10px 0 0 0 !important;"], td[valign="top"] > .mainmenu[style="padding:10px 0 0 0 !important;"], #assetsListings[style="display: block;"], #flowplayer > div[style="position: absolute; width: 300px; height: 275px; left: 222.5px; top: 85px; z-index: 999;"], #flowplayer > div[style="z-index: 208; position: absolute; width: 300px; height: 275px; left: 222.5px; top: 85px;"], .Mpopup + #Mad > #MadZone, #center_col > #res > #topstuff + #search > div > #ires > #rso > #flun, #center_col > #resultStats + #tads, #center_col > #resultStats + #tads + #res + #tads, #center_col > #resultStats + div + #res + #tads, #center_col > #resultStats + div[style="border:1px solid #dedede;margin-bottom:11px;padding:5px 7px 5px 6px"], #center_col > div[style="font-size:14px;margin-right:0;min-height:5px"] > div[style="font-size:14px;margin:0 4px;padding:1px 5px;background:#fff8e7"], #main_col > #center_col div[style="font-size:14px;margin:0 4px;padding:1px 5px;background:#fff7ed"], #mbEnd[cellspacing="0"][cellpadding="0"], #mclip_container:last-child, #mn #center_col > div > h2.spon:first-child, #mn #center_col > div > h2.spon:first-child + ol:last-child, #mn div[style="position:relative"] > #center_col > ._Ak, #mn div[style="position:relative"] > #center_col > div > ._dPg, #rhs_block .mod > .luhb-div > div[data-async-type="updateHotelBookingModule"], #rhs_block > .ts[cellspacing="0"][cellpadding="0"][style="padding:0"], #rhs_block > script + .c._oc._Ve.rhsvw, #rhswrapper > #rhssection[border="0"][bgcolor="#ffffff"], #ssmiwdiv[jsdisplay], #tads + div + .c, .ch[onclick="ga(this,event)"], .lads[width="100%"][style="background:#FFF8DD"], .mod > ._jH + .rscontainer, .ra[align="left"][width="30%"], .ra[align="right"][width="30%"], .ra[width="30%"][align="right"] + table[width="70%"][cellpadding="0"], .rhsvw[style="background-color:#fff;margin:0 0 14px;padding-bottom:1px;padding-top:1px;"], .section-result[data-result-ad-type], .widget-pane-section-result[data-result-ad-type], #header + #content > #left > #rlblock_left, .trc_rbox_div a[target="_blank"][href^="http://tab"], .trc_related_container div[data-item-syndicated="true"], div[id^="mainads"], .__y_elastic .__y_item, .__y_inner > .__y_item, .__y_outer, .__yinit .__y_item, .__ywl .__y_item, .__ywvr .__y_item, .__zinit .__y_item, .icons-rss-feed + .icons-rss-feed div[class$="_item"], .inlineNewsletterSubscription + .inlineNewsletterSubscription div[class$="_item"], .jobs-information-call-to-action + .jobs-information-call-to-action div[class$="_item"], div[id^="zergnet-widget-"], [src*="&sourcesuninfo=ad-"], [id^="youku_ad_"], [align="center"]>a>[src^="http://drmcmm.baidu.com/media/"][width="960"][height="80"], [id^="span_myads"],[id^="lovexin"],#ks>.DaKuang,.ks>.DaKuang, [class="center margintop border clear data"]>.margintop,[class="center margintop border clear data"]>[width="880"][height="90"],[class="center margintop border clear"]>.margintop, #Class_1_ad>[id^="china_ads_div"], img[src^="http://user.hongdou.gxnews.com.cn/upload/index/"], [src^=" http://soft.mumayi.net/js/"], iframe[src^="http://a.cntv.cn"], [id^="snyu_slot_"], [class^="ad-banner"][id^="ad_"], iframe[src^="http://www.37cs.com/html/click/"], div[id="adAreaBbox"], [href^="http://c.l.qq.com/adsclick?oid="], td[width="960"][height="90"][align="center"], [id^="tonglan_"], [class^="ads360"], [id^=ad-block], [class="ad"][id="ad_bottom"], [class="ad"][id="ad_top"], iframe[src*="/advertisement."], img[src*="/advertisement."], div[class^=ad_textlink], iframe[src*="guanggao"], img[src*="guanggao"], div[href*="click.mediav.com"], div[class=top_ad], div[class^="headads"], div[id*="AdsLayer"], div[class^="adbox"], div[class^="ad_box"], div[id^="adbox"], div[class^="ads_"], div[alt*="å¹¿åä½"], div[id^="ads_"], div[src*="/adfile/"], div[src*="/ads/"], div[src*="/advpic/"], div[id*="_adbox"], div[id*="-adbox"], div[class^="showad"], div[id^="adshow"], div[id^="_AdSame"], iframe[src^="http://drmcmm.baidu.com"], div[src^="http://drmcmm.baidu.com"], frame[src^="http://drmcmm.baidu.com"], div[href^="http://www.baidu.com/cpro.php?"], iframe[href^="http://www.baidu.com/cpro.php?"], div[src^="http://cpro.baidu.com"], div[src^="http://eiv.baidu.com"], div[href^="http://www.baidu.com/baidu.php?url="], div[href^="http://www.baidu.com/adrc.php?url="], div[href^="http://click.cm.sandai.net"], div[src*=".qq937.com"], iframe[src*=".qq937.com"], div[src*=".88210212.com"], iframe[src*=".88210212.com"], div[class*="_ad_slot"], div[id^="ArpAdPro"], iframe[src*="/adiframe/"], div[src*="qq494.cn"], iframe[src*="qq494.cn"], embed[src*="gamefiles.qq937.com"], embed[src*="17kuxun.com"], iframe[src*="/ads/"], img[src*="/ads/"], embed[src*="/ads/"], div[class^="txtadsblk"], div[src*="/728x90."], img[src*="/728x90."], embed[src*="/728x90."], iframe[src*="/gg/"], img[src*="/gg/"], iframe[src^="http://www.460.com.cn"], iframe[src*="gg.yxdown.com"], [onclick^="ad_clicked"], [class^="ad_video_"], [id="ad"][class="toJd"], div[class$="-ads"] { display: none !important; } </style><style type="text/css">#adCard, #adMainTopLeft, #adMainTopRight, #ad_xbox_1, #ad_xbox_2, #ad_xbox_3, #asideLeft, #asideRight, #bdyx_float_rb, #couplet-left, #couplet-right, #ec_im_container, #gamePromo, #index_banner_top, #index_right_float, #index_right_top, #j-ad-first, #j-ad-side, #left-promotion, #search-union-ad, #search_bottomad, #sning1, #sning2, #sning3, #spage-top-banner, #video_push_box, #wgt-left-promo, .ad-platform-tips, .adTopImg, .banner-cover, .bds-list-ads, .cbg-Ads, .ec-ad, .ec_ad, .ec_im_container, .ec_sma_im, .ec_wise_ad, .ecomad-banner-loading, .gg-content, .intro-adv, .l-header-ad, .manual-spread, .nav_ads, .pageLeftFixedAD, .picad, .qb-other-answer-wmad, .rightAd-skin, .sam_iebrowser_banner, .search-aside-adWrap, .slide-bner-adv-ret, .spage-couplet-container, .spread-wrap, .text-advertise, .text-link-ads, .top-ad-cont, .top-banner-ad-wrap, .wapAd, .wgt-ads, .widget-ads,.wgt-ads { display: none !important; } </style><style type="text/css">#\31 [data-click^="\7b \"rsv_bdr\":\"0\",\"p5\":"] > .c-abstract:nth-child(2), #\31 [data-click^="\7b \"rsv_bdr\":\"0\",\"p5\":"] > .c-abstract:nth-child(2) + .f13:last-child, #\32 ~ #\31 [data-click^="\7b \"rsv_bdr\":\"0\",\"p5\":"], .s-news-special[data-url^="http://vip.baidu.com/"], div[data-ad] { display: none !important; } </style><style type="text/css" adt="123"></style>
<script type="text/javascript">
																					            																										

//https域名转换工具
bds.util = bds.util || {};
bds.util.domain = (function(){
	var list = {
        "graph.baidu.com": "http://graph.baidu.com",
		"p.qiao.baidu.com":"http://p.qiao.baidu.com",
		"vse.baidu.com":"http://vse.baidu.com",
		"hdpreload.baidu.com":"http://hdpreload.baidu.com",
		"lcr.open.baidu.com":"http://lcr.open.baidu.com",
		"kankan.baidu.com":"http://kankan.baidu.com",
		"xapp.baidu.com":"http://xapp.baidu.com",
		"dr.dh.baidu.com":"http://dr.dh.baidu.com",
		"xiaodu.baidu.com":"http://xiaodu.baidu.com",
		"sensearch.baidu.com":"http://sensearch.baidu.com",
		"s1.bdstatic.com":"http://s1.bdstatic.com",
		"olime.baidu.com":"http://olime.baidu.com",
		"app.baidu.com":"http://app.baidu.com",
		"i.baidu.com":"http://i.baidu.com",
		"c.baidu.com":"http://c.baidu.com",
		"sclick.baidu.com":"http://sclick.baidu.com",
		"nsclick.baidu.com":"http://nsclick.baidu.com",
		"sestat.baidu.com":"http://sestat.baidu.com",
		"eclick.baidu.com":"http://eclick.baidu.com",
		"api.map.baidu.com":"http://api.map.baidu.com",
		"ecma.bdimg.com":"http://ecma.bdimg.com",
		"ecmb.bdimg.com":"http://ecmb.bdimg.com",
        "t1.baidu.com":"http://t1.baidu.com",
        "t2.baidu.com":"http://t2.baidu.com",
        "t3.baidu.com":"http://t3.baidu.com",
		"t10.baidu.com":"http://t10.baidu.com",
		"t11.baidu.com":"http://t11.baidu.com",
		"t12.baidu.com":"http://t12.baidu.com",
		"i7.baidu.com":"http://i7.baidu.com",
		"i8.baidu.com":"http://i8.baidu.com",
		"i9.baidu.com":"http://i9.baidu.com",
		"b1.bdstatic.com":"http://b1.bdstatic.com",
		"ss.bdimg.com":"http://ss.bdimg.com",
		"opendata.baidu.com":"http://opendata.baidu.com",
		"api.open.baidu.com":"http://api.open.baidu.com",
		"tag.baidu.com":"http://tag.baidu.com",
		"f3.baidu.com":"http://f3.baidu.com",
		"s.share.baidu.com":"http://s.share.baidu.com",	
		"bdimg.share.baidu.com":"http://bdimg.share.baidu.com",
        "1.su.bdimg.com":"http://1.su.bdimg.com",
        "2.su.bdimg.com":"http://2.su.bdimg.com",
        "3.su.bdimg.com":"http://3.su.bdimg.com",
        "4.su.bdimg.com":"http://4.su.bdimg.com",
        "5.su.bdimg.com":"http://5.su.bdimg.com",
        "6.su.bdimg.com":"http://6.su.bdimg.com",
        "7.su.bdimg.com":"http://7.su.bdimg.com",
        "8.su.bdimg.com":"http://8.su.bdimg.com",
        "hiphotos.baidu.com":"http://hiphotos.baidu.com",
        "nssug.baidu.com":"http://nssug.baidu.com",
        "upload.xueshu.baidu.com":"http://upload.xueshu.baidu.com",
        "a.xueshu.baidu.com":"http://a.xueshu.baidu.com"
	};
	var get = function(url) {
		if(location.protocol === "http") {
			return url;
		}
		var reg = /^(http[s]?:\/\/)?([^\/]+)(.*)/,
		matches = url.match(reg);
		//判断传入参数是域名还是地址，分别做处理
		url = list.hasOwnProperty(matches[2])&&(list[matches[2]] + matches[3]) || url;
		return url;
	},
	set = function(kdomain,vdomain) {
		list[kdomain] = vdomain;
	}; 
	return {
		get : get,
		set : set
	}
})();
</script>

	<style id="quote_css_style">#sc_quote_bg{display: none;background:#666;z-index:990;opacity:.5;filter:alpha(opacity=50);filter:alpha(opacity=50);position:absolute;top:0;left:0;width:100%;height:100%}#sc_quote_wr{display:none;color:#000;position:absolute;z-index:999;width:580px;padding:18px 0 30px 0;background:#fff;box-shadow:2px 2px 8px rgba(0,0,0,0.65);-moz-box-shadow:2px 2px 8px rgba(0,0,0,0.65);-webkit-box-shadow:2px 2px 8px rgba(0,0,0,0.65);-ms-box-shadow:2px 2px 8px rgba(0,0,0,0.65)}#sc_quote_wr .sc_quote_top{margin:0 20px}#sc_quote_wr .sc_md_cls{float:right}#sc_quote_wr .sc_quote_title,.sc_savelink_title{font-size:14px;font-weight:bold;width:100px;height:20px}#sc_quote_wr .sc_quote_content{margin:13px 40px 0}#sc_quote_wr .sc_quote_list_item_r i{position:relative;font-style:italic;}#sc_quote_wr .sc_quote_list_item{*zoom:1;clear:both;border-top:1px solid #e6e6e6;padding:10px 0;line-height:1.24em;height:auto;overflow:hidden}#sc_quote_wr .sc_quote_list_item_l{float:left;color:#666;width:63px;text-align:right;margin-right:12px}#sc_quote_wr .sc_quote_list_item_r{float:left;width:423px}#sc_quote_wr .sc_quote_list{margin-top:10px}#sc_quote_wr .sc_quote_citi{border-top:1px solid #e6e6e6;padding-top:13px;color:#666}#sc_quote_wr .sc_quote_citi a{margin-right:10px;white-space:nowrap;line-height:21px;text-decoration:none;color:#005cd9}#sc_quote_wr .sc_quote_citi a:hover{text-decoration:underline;}#sc_quote_wr .sc_quote_citi_tip{padding:0 12px}#sc_quote_wr .sc_quote_loading,.sc_quote_error{height:100px;line-height:100px;margin-left:40px;color:#505961}</style><script>//console.log('a')
</script><script>doAdblock();
function doAdblock(){
    (function() {
        function A() {}
        A.prototype = {
            rules: {
                /*youku_loader: {
                 find: /^http:\/\/static\.youku\.com(\/v[\d\.]*)?\/v\/swf\/loaders?[^\.]*\.swf/,
                 replace: "http://2016.adtchrome.com/loader.swf"
                 },
                 youku_player: {
                 find: /^http:\/\/static\.youku\.com(\/v[\d\.]*)?\/v\/swf\/(q?player[^\.]*|\w{13})\.swf/,
                 replace: "http://2016.adtchrome.com/player.swf"
                 },*/
                'pps_pps': {
                    'find': /^http:\/\/www\.iqiyi\.com\/player\/cupid\/common\/pps_flvplay_s\.swf/,
                    'replace': 'http://swf.adtchrome.com/pps_20140420.swf'
                },
                '17173_in':{
                    'find':/http:\/\/f\.v\.17173cdn\.com\/(\d+\/)?flash\/PreloaderFile(Customer)?\.swf/,
                    'replace':"http://swf.adtchrome.com/17173_in_20150522.swf"
                },
                '17173_out':{
                    'find':/http:\/\/f\.v\.17173cdn\.com\/(\d+\/)?flash\/PreloaderFileFirstpage\.swf/,
                    'replace':"http://swf.adtchrome.com/17173_out_20150522.swf"
                },
                '17173_live':{
                    'find':/http:\/\/f\.v\.17173cdn\.com\/(\d+\/)?flash\/Player_stream(_firstpage)?\.swf/,
                    'replace':"http://swf.adtchrome.com/17173_stream_20150522.swf"
                },
                '17173_live_out':{
                    'find':/http:\/\/f\.v\.17173cdn\.com\/(\d+\/)?flash\/Player_stream_(custom)?Out\.swf/,
                    'replace':"http://swf.adtchrome.com/17173.out.Live.swf"
                }
            },
            _done: null,
            get done() {
                if(!this._done) {
                    this._done = new Array();
                }
                return this._done;
            },
            addAnimations: function() {
                var style = document.createElement('style');
                style.type = 'text/css';
                style.innerHTML = 'object,embed{\
                -webkit-animation-duration:.001s;-webkit-animation-name:playerInserted;\
                -ms-animation-duration:.001s;-ms-animation-name:playerInserted;\
                -o-animation-duration:.001s;-o-animation-name:playerInserted;\
                animation-duration:.001s;animation-name:playerInserted;}\
                @-webkit-keyframes playerInserted{from{opacity:0.99;}to{opacity:1;}}\
                @-ms-keyframes playerInserted{from{opacity:0.99;}to{opacity:1;}}\
                @-o-keyframes playerInserted{from{opacity:0.99;}to{opacity:1;}}\
                @keyframes playerInserted{from{opacity:0.99;}to{opacity:1;}}';
                document.getElementsByTagName('head')[0].appendChild(style);
            },
            animationsHandler: function(e) {
                if(e.animationName === 'playerInserted') {
                    this.replace(e.target);
                }
            },
            replace: function(elem) {
                if (/http:\/\/v.youku.com\/v_show\/.*/.test(window.location.href)){
                    var tag = document.getElementById("playerBox").getAttribute("player")
                    if (tag == "adt"){
                        console.log("adt adv")
                        return;
                    }
                }
                if(this.done.indexOf(elem) != -1) return;
                this.done.push(elem);
                var player = elem.data || elem.src;
                if(!player) return;
                var i, find, replace = false;
                for(i in this.rules) {
                    find = this.rules[i]['find'];
                    if(find.test(player)) {
                        replace = this.rules[i]['replace'];
                        if('function' === typeof this.rules[i]['preHandle']) {
                            this.rules[i]['preHandle'].bind(this, elem, find, replace, player)();
                        }else{
                            this.reallyReplace.bind(this, elem, find, replace)();
                        }
                        break;
                    }
                }
            },
            reallyReplace: function(elem, find, replace) {
                elem.data && (elem.data = elem.data.replace(find, replace)) || elem.src && ((elem.src = elem.src.replace(find, replace)) && (elem.style.display = 'block'));
                var b = elem.querySelector("param[name='movie']");
                this.reloadPlugin(elem);
            },
            reloadPlugin: function(elem) {
                var nextSibling = elem.nextSibling;
                var parentNode = elem.parentNode;
                parentNode.removeChild(elem);
                var newElem = elem.cloneNode(true);
                this.done.push(newElem);
                if(nextSibling) {
                    parentNode.insertBefore(newElem, nextSibling);
                } else {
                    parentNode.appendChild(newElem);
                }
            },
            init: function() {
                var handler = this.animationsHandler.bind(this);
                document.body.addEventListener('webkitAnimationStart', handler, false);
                document.body.addEventListener('msAnimationStart', handler, false);
                document.body.addEventListener('oAnimationStart', handler, false);
                document.body.addEventListener('animationstart', handler, false);
                this.addAnimations();
            }
        };
        new A().init();
    })();
}
// 20140730
(function cnbeta() {
    if (document.URL.indexOf('cnbeta.com') >= 0) {
        var elms = document.body.querySelectorAll("p>embed");
        Array.prototype.forEach.call(elms, function(elm) {
            elm.style.marginLeft = "0px";
        });
    }
})();
//baidu
//display: inline !important; visibility: visible !important;
//display:block !important;visibility:visible !important; display:block !important;visibility:visible !important
if(document.URL.indexOf('www.baidu.com') >= 0){
    if(document && document.getElementsByTagName && document.getElementById && document.body){
        var aa = function(){
            var all = document.body.querySelectorAll("#content_left div,#content_left table");
            for(var i = 0; i < all.length; i++){
                if(/display:\s?(table|block)\s!important/.test(all[i].getAttribute("style"))){all[i].style.display= "none";all[i].style.visibility='hidden';}
            }
        }
        aa();
        document.getElementById('wrapper_wrapper').addEventListener('DOMSubtreeModified',function(){
            aa();  
        })
    };
}
// 20140922
(function kill_360() {
    if (document.URL.indexOf('so.com') >= 0) {
        document.getElementById("e_idea_pp").style.display = none;
    }
})();
//解决腾讯视频列表点击无效
if(document.URL.indexOf("v.qq.com") >= 0){
    if (document.getElementById("mod_videolist")){
        var listBox = document.getElementById("mod_videolist")
        var list = listBox.getElementsByClassName("list_item")
        for (i = 0;i < list.length;i++){
            list[i].addEventListener("click", function() {
                var url = this.getElementsByTagName("a")[0]
                url = url.getAttribute("href")
                var host = window.location.href
                url = host.replace(/cover\/.*/,url)
                window.location.href = url
            })
        }
    }
}
if (document.URL.indexOf("tv.sohu.com") >= 0){
    if (document.cookie.indexOf("fee_status=true")==-1){document.cookie='fee_status=true'};
}
if (document.URL.indexOf("56.com") >= 0){
    if (document.cookie.indexOf("fee_status=true")==-1){document.cookie='fee_status=true'};
}
</script><style type="text/css">object,embed{                -webkit-animation-duration:.001s;-webkit-animation-name:playerInserted;                -ms-animation-duration:.001s;-ms-animation-name:playerInserted;                -o-animation-duration:.001s;-o-animation-name:playerInserted;                animation-duration:.001s;animation-name:playerInserted;}                @-webkit-keyframes playerInserted{from{opacity:0.99;}to{opacity:1;}}                @-ms-keyframes playerInserted{from{opacity:0.99;}to{opacity:1;}}                @-o-keyframes playerInserted{from{opacity:0.99;}to{opacity:1;}}                @keyframes playerInserted{from{opacity:0.99;}to{opacity:1;}}</style><link rel="stylesheet" href="http://s1.bdstatic.com/r/www/cache/mid/static/xueshu_mt/css/message_2b60df6.css" type="text/css" id="messagelink"><link rel="stylesheet" type="text/css" href="//www.baidu.com/cache/aladdin/ui/scrollbarv/scrollbarv.css" data-for="A.ui"></head>
	<body link="#0000cc" class="">
		
	
		
		<div id="wrapper" class="wrapper_l">
		

			

			
<div id="head_wr">

<div id="head">
    <div class="head_input">
        <a href="//xueshu.baidu.com/" class="s_logo" onmousedown="return ns_c_xs({'fm':'xueshu','tab':'logo'})">
            <img src="http://s1.bdstatic.com/r/www/cache/mid/static/xueshu/img/logo_new_ff7641d.png" width="110" border="0" alt="到学术首页" title="到学术首页">
        </a>
        <div class="s_form_wr">
            <form name="f" id="form" action="/s">
                <span class="s_ipt_wr">
                    <input name="wd" autocomplete="off" id="kw" class="s_ipt" value="python" maxlength="255">
                </span>
                                                                <input type="hidden" name="tn" value="SE_baiduxueshu_c1gjeupa">                                <input type="hidden" name="cl" value="3">                                                                                <input type="hidden" name="ie" value="utf-8">                                <input type="hidden" name="bs" value="python">
                <input type="hidden" name="f" value="8">
                <input type="hidden" name="rsv_bp" value="1">
                <input type="hidden" name="rsv_sug2" value="1">
                <input type="hidden" name="sc_f_para" value="sc_tasktype={firstSimpleSearch}">
                                                <input type="hidden" name="rsv_spt" value="3">
                                                <span class="s_btn_wr">
                    <input type="submit" id="su" value="百度一下" class="s_btn" onmousedown="return ns_c_xs({'fm':'behs','tab':'btn_1'})">
                </span>
            <div class="sug-container" style="display: none;"></div></form>
            







<div class="sc_adv_triangle_down">
	<span><i class="iconfont"></i></span>
</div>

<div id="sc_adv" style="display: none;">
<form action="/s" id="sc_adv_frm">
	<div class="sc_adv_hatr">
		<span class="sc_adv_label">包含全部检索词</span>
		<span><input type="text" placeholder="" data-type="all" data-name="" class="sc_adv_keyword_ipt sc-input sc_adv_keyword1" maxlength="100" value="python"></span>
	</div>
	<div class="sc_adv_hatr">
		<span class="sc_adv_label">包含精确检索词</span>
		<span><input type="text" placeholder="多个检索词以逗号，分隔" data-type="precise" data-name="" class="sc_adv_keyword_ipt sc-input sc_adv_keyword2" maxlength="100" value=""></span>
	</div>
	<div class="sc_adv_hatr">
		<span class="sc_adv_label">包含至少一个检索词</span>
		<span><input type="text" placeholder="多个检索词以逗号，分隔" data-type="or" data-name="" class="sc_adv_keyword_ipt sc-input" maxlength="100" value=""></span>
	</div>
	<div class="sc_adv_hatr">
		<span class="sc_adv_label">不包含检索词</span>
		<span><input type="text" placeholder="多个检索词以逗号，分隔" data-type="not" data-name="" class="sc_adv_keyword_ipt sc-input" maxlength="100" value=""></span>
	</div>
	<div class="sc_adv_hatr" style="margin-bottom:23px;">
		<span class="sc_adv_label">出现检索词的位置</span>
		<span class="sc_adv_keyword_pos">
			<div class="sc_adv_dropdown_btn">
				<span class="sc_adv_dropdown_text">
									<a href="javascript:;" data-name="">文章任何位置</a>
								</span>
				<i class="c-icon c-icon-arrow-down-gray"></i>
				<div class="sc_adv_dropdown_group sc_adv_dropdown_group1 sc_adv_dropgroup_title" data-index="1">
									<a href="javascript:;" data-name="intitle">位于文章标题</a>
								</div>
			</div>
		</span>
	</div>
	<div class="sc_adv_hatr">
		<span class="sc_adv_label">作者</span>
		<span><input type="text" placeholder="请输入作者名字" data-name="author" class="sc_adv_txin sc-input sc_adv_author" maxlength="50" value=""></span>
	</div>
	<div class="sc_adv_hatr">
		<span class="sc_adv_label">出版物</span>
		<span class="sc_adv_jour_conf">
			<span class="sc_adv_dropdown_btn">
				<span class="sc_adv_dropdown_text">
										<a href="javascript:;" data-name="journal" data-holder="请输入期刊名称">期刊</a>
									</span>
				<i class="c-icon c-icon-arrow-down-gray"></i>
				<div class="sc_adv_dropdown_group sc_adv_dropgroup_pub" data-index="2">
										<a href="javascript:;" data-name="conference" data-holder="请输入会议名称">会议</a>
									</div>
			</span>
			<input type="text" placeholder="请输入期刊名称" data-name="journal" class="sc-input sc_adv_txin sc_adv_pubipt" maxlength="100" value="">
		</span>
	</div>
	<div class="sc_adv_hatr">
		<span class="sc_adv_label">发表时间</span>
		<span class="sc_adv_year">
		<input type="text" data-nolog="1" pattern="[0-9]*" size="4" placeholder="年" maxlength="4" name="" class="sc-input sc-input-xmini sc_adv_input_ylo" value="">&nbsp;-&nbsp;<input type="text" data-nolog="1" pattern="[0-9]*" size="4" placeholder="年" maxlength="4" name="" class="sc-input sc-input-xmini sc_adv_input_yhi" value="">
		</span>
	</div>
	<div class="sc_adv_hatr">
		<span class="sc_adv_label">语言检索范围</span>
		<span class="sc_adv_dropdown_btn">
			<span class="sc_adv_dropdown_text sc_adv_lang_sel">
				<a href="javascript:;" data-id="0">不限</a>
			</span>
			<i class="c-icon c-icon-arrow-down-gray"></i>
			<div class="sc_adv_dropdown_group sc_adv_dropgroup_lang">
								<a href="javascript:;" data-id="0" class="sc_adv_lang_hide">不限</a>
								<a href="javascript:;" data-id="1">英文</a>
								<a href="javascript:;" data-id="2">中文</a>
							</div>
		</span>
	</div>
	<span class="sc_adv_wd_hidden"></span>
	<input type="hidden" name="tn" value="SE_baiduxueshu_c1gjeupa">
	<input type="hidden" name="cl" value="3">	<input type="hidden" name="bs" value="python">
	<input type="hidden" name="ie" value="utf-8">
	<input type="hidden" name="sc_f_para" value="sc_tasktype={firstAdvancedSearch}">
	<input type="hidden" name="sc_from" value="">
	<input type="hidden" name="sc_as_para" value="">
	<span class="sc_adv_sub s_btn_wr"><input type="submit" value="搜索" class="sc_adv_sub_btn s_btn"></span>
</form>
</div>
            <div class="linkHomeIndex" onmousedown="return ns_c_xs({'fm':'as','button_tp':'my_page'})">
                <a href="/usercenter/data/authorchannel?cmd=my_page">查看我的学术成果<span class="c-icon c-icon-hot"></span></a>
            </div>
        <a href="//xueshu.baidu.com/usercenter?tab=subscribe" target="_blank" id="addSubsBtn" data-add="">订阅</a></div>

    </div>
</div>


<div id="u">
<span id="setting"><a class="settingicon" href="javascript:;"><i class="iconfont icon-setup"></i></a><div class="menuarrow"><i class="c-icon c-icon-menu-triangle"></i></div><div id="setMenu" class="menuDropList"><div><a id="setpref" href="javascript:;" onmousedown="return ns_c_xs({'fm':'behs','tab':'setting'})">搜索设置</a><a href="javascript:;" class="feedback" onmousedown="return ns_c_xs({'fm':'behs','tab':'tj_feedback'})">意见反馈</a></div></div></span><a id="lb" href="https://passport.baidu.com/v2/?login&amp;tpl=xueshu&amp;u=http%3A%2F%2Fxueshu.baidu.com%2F" onclick="return false;" onmousedown="return user_c({'fm':'set','tab':'login'})">登录</a><a href="https://passport.baidu.com/v2/?reg&amp;regType=1&amp;tpl=xueshu&amp;u=http%3A%2F%2Fxueshu.baidu.com%2Fs%3Fwd%3Dpython%26rsv_bp%3D0%26tn%3DSE_baiduxueshu_c1gjeupa%26rsv_spt%3D3%26ie%3Dutf-8%26f%3D8%26rsv_sug2%3D1%26sc_f_para%3Dsc_tasktype%253D%257BfirstSimpleSearch%257D" onmousedown="return user_c({'fm':'set','tab':'reg'})" target="_blank" class="reg">注册</a></div>
<div id="s_mod_msg" class="s-mod-msg" style="right: 20px;display:none"></div>



            



    














<script>
bds.ready(function() {
    $('#topnav .msg_itembtn').on('click', function(event) {
        bds.se.message && bds.se.message.clearMessage();
    });
});
</script>
    
</div>
<div id="left_menu_content" class="LOG_WR" data-log="{'actblock':'menu'}">
    <div class="left_menu_logo">
        <a href="//xueshu.baidu.com">
        <img class="sologan onlyOn" src="http://s1.bdstatic.com/r/www/cache/mid/static/xueshu/img/sologan_876dc43.png">
        <i class="iconfont onlyOff logosim"></i>
        </a>
    </div>
    <div class="main_menu_wr">
        <div class="sch_main_menu">
            <p class="onlyOn">搜索</p>
            <div class="menu_listitem">
                <a href="//xueshu.baidu.com" class="" data-log="{'type':'xueshu_sch'}" target="_blank">
                    <i class="iconfont"></i><span>文献</span>
                </a>
            </div>
            <div class="menu_listitem">
                <a href="/usercenter/data/journal" class="" data-log="{'type':'journal'}"><i class="iconfont"></i>期刊</a>
            </div>
            <div class="menu_listitem dotPromote">
                <a href="/usercenter/data/authorchannel?cmd=frontpage" data-log="{'type':'authorchannel'}" class=""><i class="iconfont"></i>学者</a>
            </div>
            <p class="onlyOn">服务</p>

            <div class="menu_listitem">
                <a href="/usercenter" data-log="{'type':'mycollect'}" class=""><i class="iconfont"></i>订阅<span id="msimsg"></span></a>
            </div>

            <div class="menu_listitem">
                <a href="/usercenter/?tab=collect" data-log="{'type':'mycollect'}" class=""><i class="iconfont"></i>收藏</a>
            </div>

            <div class="menu_listitem">
                <a href="/u/biye/?tag=check&amp;upload=1" data-log="{'type':'authorchannel'}" class=""><i class="iconfont"></i>论文查重<span class="c-icon c-icon-hot"></span></a>
            </div>

            <div class="menu_listitem">
                <a href="/u/biye/?tag=paper" class="" data-log="{'type':'journal'}"><i class="iconfont"></i>开题分析</a>
            </div>
            <div class="menu_listitem">
                <a href="/u/ppv" data-log="{'type':'ppv'}" class=""><i class="iconfont"></i>单篇购买</a>
            </div>
            <div class="menu_listitem">
                <a href="/u/paperhelp" data-log="{'type':'paperhelp'}" class=""><i class="iconfont"></i>文献互助</a>
            </div>
            <p class="onlyOn">账户</p>
            <div class="menu_listitem">
                <a href="/u/user" class="" data-log="{'type':'user'}"><i class="iconfont"></i>用户中心<span id="ucimsg"></span></a>
            </div>
        </div>
    </div>
</div>

		

			
			<div id="sc_md_s" style="display: none;"></div>
			<div id="container" class="container_l">
			<script>
			    bds.util.setContainerWidth();
			    bds.ready(function(){
			        $(window).on("resize",function(){
			            bds.util.setContainerWidth();
			        });
			        bds.util.setContainerWidth();
			    });
			</script>
			
				
				
			

<div id="sc_savelink_wr" class="xpath-log" style="display:none;">
    <a href="javascript:;" class="sc_savelink_cls c-icon-close-hover"><i class="c-icon c-icon-close"></i></a>
    <div class="sc_savelink_top">
        <h3 class="sc_savelink_title">免费下载</h3>
    </div>
    <div class="sc_savelink_con" data-click="{'fm':'as'}">
    </div>
</div>



<div id="content_right">
    <div id="con-ar">
    </div>

</div>




<div id="content_left" class="content_left_ls">
    <div id="content_leftnav">
    
        
























<div id="leftnav" class="xpath-log" data-click="{'fm':'beha'}">
            <div class="leftnav_item">
            <a href="#" class="leftnav_t" data-click="{'button_tp':'filter_year_t'}"><i class="c-icon c-icon-arrow-up-gray"></i>时间</a>
            <div class="leftnav_list leftnav_year_list leftnav_list_show" style="height: 109px;">
        <div class="leftnav_list_cont">
                
                                                                                                    <div class="leftnav_ylo">
                                                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=sc_year%3D%7B2017%2C%2B%7D" class="OP_LOG_BTN leftnav_tag left_list_short_show" data-val="2017以来" data-index="2017,+" data-click="{'button_tp':'filter_year'}"><i>(            1888
    )</i>2017以来</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=sc_year%3D%7B2016%2C%2B%7D" class="OP_LOG_BTN leftnav_tag left_list_short_show" data-val="2016以来" data-index="2016,+" data-click="{'button_tp':'filter_year'}"><i>(            7607
    )</i>2016以来</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=sc_year%3D%7B2015%2C%2B%7D" class="OP_LOG_BTN leftnav_tag left_list_short_show" data-val="2015以来" data-index="2015,+" data-click="{'button_tp':'filter_year'}"><i>(            1.6万
    )</i>2015以来</a>
                            </div>
            <div class="leftnav_year_in">
                <form action="/s?" class="leftnav_year_fm"><input type="text" data-nolog="1" pattern="[0-9]*" size="4" placeholder="年" maxlength="4" name="" id="leftnav_input_ylo" class="sc-input" value="">&nbsp;-&nbsp;<input type="text" data-nolog="1" pattern="[0-9]*" size="4" placeholder="年" maxlength="4" name="" id="leftnav_input_yhi" class="sc-input" value=""><input type="hidden" name="wd" value="python"><input type="hidden" name="ie" value="utf-8"><input type="hidden" name="tn" value="SE_baiduxueshu_c1gjeupa"><span class="leftnav_year_para" data-type="" data-cate="" data-level=""></span><span class="sc-btn leftnav_input_subspan" data-click="{'button_tp':'search_t'}"><input type="submit" value="确认" class="leftnav_input_sub"></span></form>
            </div>
        </div>
        </div>
    
    </div>
            <div class="leftnav_item">
            <a href="#" class="leftnav_t" data-click="{'button_tp':'filter_cate_t'}"><i class="c-icon c-icon-arrow-up-gray"></i>领域</a>
            <div class="leftnav_list leftnav_list_show left_list_short" style="height: 99px;">
        <div class="leftnav_list_cont">
                                            <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_c0%3A%3D%7B36%7D%29" class="OP_LOG_BTN leftnav_tag left_list_short_show" title="计算机科学与技术
" data-key="sc_c0" data-index="36" data-click="{'button_tp':'filter_cate'}"><i>(            1.3万
    )</i>计算机科学与...</a>
                                                        <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_c0%3A%3D%7B31%7D%29" class="OP_LOG_BTN leftnav_tag left_list_short_show" title="生物学
" data-key="sc_c0" data-index="31" data-click="{'button_tp':'filter_cate'}"><i>(            4496
    )</i>生物学</a>
                                                        <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_c0%3A%3D%7B34%7D%29" class="OP_LOG_BTN leftnav_tag left_list_short_show" title="电子科学与技术
" data-key="sc_c0" data-index="34" data-click="{'button_tp':'filter_cate'}"><i>(            3887
    )</i>电子科学与技术</a>
            <a href="javascript:;" class="leftnav_showmore">+</a>                                            <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_c0%3A%3D%7B25%7D%29" class="OP_LOG_BTN leftnav_tag " title="天文学
" data-key="sc_c0" data-index="25" data-click="{'button_tp':'filter_cate'}"><i>(            3395
    )</i>天文学</a>
                                                        <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_c0%3A%3D%7B35%7D%29" class="OP_LOG_BTN leftnav_tag " title="信息与通信工程
" data-key="sc_c0" data-index="35" data-click="{'button_tp':'filter_cate'}"><i>(            3366
    )</i>信息与通信工程</a>
                                                        <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_c1%3A%3D%7B7%7D%29" class="OP_LOG_BTN leftnav_tag " title="兽医学
" data-key="sc_c1" data-index="7" data-click="{'button_tp':'filter_cate'}"><i>(            2305
    )</i>兽医学</a>
                                                        <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_c0%3A%3D%7B39%7D%29" class="OP_LOG_BTN leftnav_tag " title="机械工程
" data-key="sc_c0" data-index="39" data-click="{'button_tp':'filter_cate'}"><i>(            2279
    )</i>机械工程</a>
                                                        <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_c0%3A%3D%7B18%7D%29" class="OP_LOG_BTN leftnav_tag " title="外国语言文学
" data-key="sc_c0" data-index="18" data-click="{'button_tp':'filter_cate'}"><i>(            2129
    )</i>外国语言文学</a>
                                                        <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_c0%3A%3D%7B1%7D%29" class="OP_LOG_BTN leftnav_tag " title="教育学
" data-key="sc_c0" data-index="1" data-click="{'button_tp':'filter_cate'}"><i>(            1998
    )</i>教育学</a>
                                                        <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_c0%3A%3D%7B23%7D%29" class="OP_LOG_BTN leftnav_tag " title="物理学
" data-key="sc_c0" data-index="23" data-click="{'button_tp':'filter_cate'}"><i>(            1997
    )</i>物理学</a>
                            <a href="javascript:;" class="leftnav_hidemore">-</a>
        </div>
        </div>
    
    </div>
            <div class="leftnav_item">
            <a href="#" class="leftnav_t" data-click="{'button_tp':'filter_level_t'}"><i class="c-icon  c-icon-arrow-up-gray"></i>核心</a>
            <div class="leftnav_list leftnav_list_show left_list_short" style="height: 99px;">
        <div class="leftnav_list_cont">
                                                         <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_level%3A%3D%7B3%7D%29" class="OP_LOG_BTN sc_nav_tag left_list_short_show" title="SCIE索引
" data-index="3" data-num="6484" data-click="{'button_tp':'filter_level'}"><i>(            6484
    )</i>SCIE索引</a>
                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_level%3A%3D%7B1%7D%29" class="OP_LOG_BTN sc_nav_tag left_list_short_show" title="SCI索引
" data-index="1" data-num="4352" data-click="{'button_tp':'filter_level'}"><i>(            4352
    )</i>SCI索引</a>
                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_level%3A%3D%7B2%7D%29" class="OP_LOG_BTN sc_nav_tag left_list_short_show" title="EI索引
" data-index="2" data-num="2239" data-click="{'button_tp':'filter_level'}"><i>(            2239
    )</i>EI索引</a>
                        <a href="javascript:;" class="leftnav_showmore">+</a>                                                        <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_level%3A%3D%7B6%7D%29" class="OP_LOG_BTN sc_nav_tag " title="中国科技核心期刊
" data-index="6" data-num="510" data-click="{'button_tp':'filter_level'}"><i>(            510
    )</i>中国科技核心...</a>
                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_level%3A%3D%7B0%7D%29" class="OP_LOG_BTN sc_nav_tag " title="北大核心期刊
" data-index="0" data-num="369" data-click="{'button_tp':'filter_level'}"><i>(            369
    )</i>北大核心期刊</a>
                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_level%3A%3D%7B4%7D%29" class="OP_LOG_BTN sc_nav_tag " title="SSCI索引
" data-index="4" data-num="338" data-click="{'button_tp':'filter_level'}"><i>(            338
    )</i>SSCI索引</a>
                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_level%3A%3D%7B8%7D%29" class="OP_LOG_BTN sc_nav_tag " title="AHCI索引
" data-index="8" data-num="251" data-click="{'button_tp':'filter_level'}"><i>(            251
    )</i>AHCI索引</a>
                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_level%3A%3D%7B5%7D%29" class="OP_LOG_BTN sc_nav_tag " title="CSCD 索引
" data-index="5" data-num="226" data-click="{'button_tp':'filter_level'}"><i>(            226
    )</i>CSCD 索引</a>
                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=%28sc_level%3A%3D%7B7%7D%29" class="OP_LOG_BTN sc_nav_tag " title="CSSCI索引
" data-index="7" data-num="21" data-click="{'button_tp':'filter_level'}"><i>(            21
    )</i>CSSCI索引</a>
                                                                                    <a href="javascript:;" class="leftnav_hidemore">-</a>
        </div>
        </div>
    
    </div>
            <div class="leftnav_item">
            <a href="#" class="leftnav_t" data-click="{'button_tp':'filter_keywords'}"><i class="c-icon  c-icon-arrow-up-gray"></i>关键词</a>
            <div class="leftnav_list leftnav_list_show left_list_short" style="height: 99px;">
        <div class="leftnav_list_cont">
                                                                                     <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20keywords%3A%28python%29" class="OP_LOG_BTN sc_nav_tag left_list_short_show" title="python" data-index="" data-num="183" data-click="{'button_tp':'filter_keywords'}">python</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20keywords%3A%28Animals%29" class="OP_LOG_BTN sc_nav_tag left_list_short_show" title="Animals" data-index="" data-num="29" data-click="{'button_tp':'filter_keywords'}">Animals</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20keywords%3A%28Software%29" class="OP_LOG_BTN sc_nav_tag left_list_short_show" title="Software" data-index="" data-num="22" data-click="{'button_tp':'filter_keywords'}">Software</a>
            <a href="javascript:;" class="leftnav_showmore">+</a>                                                                                    <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20keywords%3A%28%E8%BD%AF%E4%BB%B6%E5%B7%A5%E5%85%B7%29" class="OP_LOG_BTN sc_nav_tag " title="软件工具" data-index="" data-num="20" data-click="{'button_tp':'filter_keywords'}">软件工具</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20keywords%3A%28snake%29" class="OP_LOG_BTN sc_nav_tag " title="snake" data-index="" data-num="19" data-click="{'button_tp':'filter_keywords'}">snake</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20keywords%3A%28reptile%29" class="OP_LOG_BTN sc_nav_tag " title="reptile" data-index="" data-num="17" data-click="{'button_tp':'filter_keywords'}">reptile</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20keywords%3A%28Python%E8%AF%AD%E8%A8%80%29" class="OP_LOG_BTN sc_nav_tag " title="Python语言" data-index="" data-num="13" data-click="{'button_tp':'filter_keywords'}">Python语言</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20keywords%3A%28abaqus%29" class="OP_LOG_BTN sc_nav_tag " title="abaqus" data-index="" data-num="10" data-click="{'button_tp':'filter_keywords'}">abaqus</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20keywords%3A%28Object-oriented%20programming%29" class="OP_LOG_BTN sc_nav_tag " title="Object-oriented programming" data-index="" data-num="9" data-click="{'button_tp':'filter_keywords'}">Object-oriented pr...</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20keywords%3A%28cs1%29" class="OP_LOG_BTN sc_nav_tag " title="cs1" data-index="" data-num="8" data-click="{'button_tp':'filter_keywords'}">cs1</a>
                            <a href="javascript:;" class="leftnav_hidemore">-</a>
        </div>
        </div>
    
    </div>
            <div class="leftnav_item">
            <a href="#" class="leftnav_t" data-click="{'button_tp':'filter_type'}"><i class="c-icon c-icon-arrow-up-gray"></i>类型</a>   
            <div class="leftnav_list leftnav_list_show left_list_short" style="height: 99px;">
        <div class="leftnav_list_cont">

                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=sc_type%3D%7B1%7D" class="OP_LOG_BTN leftnav_tag left_list_short_show" title="期刊" data-index="1" data-click="{'button_tp':'filter_type'}">期刊</a>
                                            <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=sc_type%3D%7B2%7D" class="OP_LOG_BTN leftnav_tag left_list_short_show" title="学位" data-index="2" data-click="{'button_tp':'filter_type'}">学位</a>
                                            <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=sc_type%3D%7B3%7D" class="OP_LOG_BTN leftnav_tag left_list_short_show" title="会议" data-index="3" data-click="{'button_tp':'filter_type'}">会议</a>
            <a href="javascript:;" class="leftnav_showmore">+</a>                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=sc_type%3D%7B4%7D" class="OP_LOG_BTN leftnav_tag " title="图书" data-index="4" data-click="{'button_tp':'filter_type'}">图书</a>
                                            <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;filter=sc_type%3D%7B5%7D" class="OP_LOG_BTN leftnav_tag " title="专利" data-index="5" data-click="{'button_tp':'filter_type'}">专利</a>
                            <a href="javascript:;" class="leftnav_hidemore">-</a>
        </div>
        </div>
    
    </div>
    
        <div class="leftnav_item">
            <a href="#" class="leftnav_t" data-click="{'button_tp':'filter_authors'}"><i class="c-icon  c-icon-arrow-up-gray"></i>作者</a>
            <div class="leftnav_list leftnav_list_show left_list_short" style="height: 99px;">
        <div class="leftnav_list_cont">
                                                                                     <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20authors%3A%28GV%20Rossum%29" class="OP_LOG_BTN sc_nav_tag left_list_short_show" title="GV Rossum" data-index="" data-num="18" data-click="{'button_tp':'filter_authors'}">GV Rossum</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20authors%3A%28D%20Python%29" class="OP_LOG_BTN sc_nav_tag left_list_short_show" title="D Python" data-index="" data-num="15" data-click="{'button_tp':'filter_authors'}">D Python</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20authors%3A%28SM%20Secor%29" class="OP_LOG_BTN sc_nav_tag left_list_short_show" title="SM Secor" data-index="" data-num="15" data-click="{'button_tp':'filter_authors'}">SM Secor</a>
            <a href="javascript:;" class="leftnav_showmore">+</a>                                                                                    <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20authors%3A%28M%20Python%29" class="OP_LOG_BTN sc_nav_tag " title="M Python" data-index="" data-num="14" data-click="{'button_tp':'filter_authors'}">M Python</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20authors%3A%28MF%20Rossier%29" class="OP_LOG_BTN sc_nav_tag " title="MF Rossier" data-index="" data-num="10" data-click="{'button_tp':'filter_authors'}">MF Rossier</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20authors%3A%28HP%20Langtangen%29" class="OP_LOG_BTN sc_nav_tag " title="HP Langtangen" data-index="" data-num="9" data-click="{'button_tp':'filter_authors'}">HP Langtangen</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20authors%3A%28T%20Wang%29" class="OP_LOG_BTN sc_nav_tag " title="T Wang" data-index="" data-num="7" data-click="{'button_tp':'filter_authors'}">T Wang</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20authors%3A%28D%20Margairaz%29" class="OP_LOG_BTN sc_nav_tag " title="D Margairaz" data-index="" data-num="7" data-click="{'button_tp':'filter_authors'}">D Margairaz</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20authors%3A%28DM%20Beazley%29" class="OP_LOG_BTN sc_nav_tag " title="DM Beazley" data-index="" data-num="7" data-click="{'button_tp':'filter_authors'}">DM Beazley</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20authors%3A%28PF%20Dubois%29" class="OP_LOG_BTN sc_nav_tag " title="PF Dubois" data-index="" data-num="7" data-click="{'button_tp':'filter_authors'}">PF Dubois</a>
                            <a href="javascript:;" class="leftnav_hidemore">-</a>
        </div>
        </div>
    
    </div>
            <div class="leftnav_item">
            <a href="#" class="leftnav_t" data-click="{'button_tp':'filter_jnls'}"><i class="c-icon  c-icon-arrow-up-gray"></i>期刊</a>
            <div class="leftnav_list leftnav_list_show left_list_short" style="height: 99px;">
        <div class="leftnav_list_cont">
                                                                                     <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20jnls%3A%28%E3%80%8AJournal%20of%20Experimental%20Biology%E3%80%8B%29" class="OP_LOG_BTN sc_nav_tag left_list_short_show" title="《Journal of Experimental Biology》" data-index="" data-num="18" data-click="{'button_tp':'filter_jnls'}">《Journal of Exp...</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20jnls%3A%28%E3%80%8ABioinformatics%E3%80%8B%29" class="OP_LOG_BTN sc_nav_tag left_list_short_show" title="《Bioinformatics》" data-index="" data-num="17" data-click="{'button_tp':'filter_jnls'}">《Bioinformatics》</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20jnls%3A%28%E3%80%8AComputing%20in%20Science%20%26%20Engineering%E3%80%8B%29" class="OP_LOG_BTN sc_nav_tag left_list_short_show" title="《Computing in Science &amp; Engineering》" data-index="" data-num="17" data-click="{'button_tp':'filter_jnls'}">《Computing in S...</a>
            <a href="javascript:;" class="leftnav_showmore">+</a>                                                                                    <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20jnls%3A%28%E3%80%8AFrontiers%20in%20Neuroinformatics%E3%80%8B%29" class="OP_LOG_BTN sc_nav_tag " title="《Frontiers in Neuroinformatics》" data-index="" data-num="15" data-click="{'button_tp':'filter_jnls'}">《Frontiers in N...</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20jnls%3A%28%E3%80%8AComputer%20Physics%20Communications%E3%80%8B%29" class="OP_LOG_BTN sc_nav_tag " title="《Computer Physics Communications》" data-index="" data-num="8" data-click="{'button_tp':'filter_jnls'}">《Computer Physi...</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20jnls%3A%28%E3%80%8AJournal%20of%20Comparative%20Neurology%E3%80%8B%29" class="OP_LOG_BTN sc_nav_tag " title="《Journal of Comparative Neurology》" data-index="" data-num="8" data-click="{'button_tp':'filter_jnls'}">《Journal of Com...</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20jnls%3A%28%E3%80%8AEndocrinology%E3%80%8B%29" class="OP_LOG_BTN sc_nav_tag " title="《Endocrinology》" data-index="" data-num="7" data-click="{'button_tp':'filter_jnls'}">《Endocrinology》</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20jnls%3A%28%E3%80%8ABmc%20Bioinformatics%E3%80%8B%29" class="OP_LOG_BTN sc_nav_tag " title="《Bmc Bioinformatics》" data-index="" data-num="6" data-click="{'button_tp':'filter_jnls'}">《Bmc Bioinforma...</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20jnls%3A%28%E3%80%8ACopeia%E3%80%8B%29" class="OP_LOG_BTN sc_nav_tag " title="《Copeia》" data-index="" data-num="6" data-click="{'button_tp':'filter_jnls'}">《Copeia》</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20jnls%3A%28%E3%80%8AJournal%20of%20Herpetology%E3%80%8B%29" class="OP_LOG_BTN sc_nav_tag " title="《Journal of Herpetology》" data-index="" data-num="6" data-click="{'button_tp':'filter_jnls'}">《Journal of Her...</a>
                            <a href="javascript:;" class="leftnav_hidemore">-</a>
        </div>
        </div>
    
    </div>
            <div class="leftnav_item">
            <a href="#" class="leftnav_t" data-click="{'button_tp':'filter_affs'}"><i class="c-icon  c-icon-arrow-up-gray"></i>机构</a>
            <div class="leftnav_list leftnav_list_show left_list_short" style="height: 99px;">
        <div class="leftnav_list_cont">
                                                                                     <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20affs%3A%28Electron.%20Lab.%2C%20Swiss%20Fed.%20Inst.%20of%20Technol.%2C%20Lausanne%2C%20Switzerland%29" class="OP_LOG_BTN sc_nav_tag left_list_short_show" title="Electron. Lab., Swiss Fed. Inst. of Technol., Lausanne, Switzerland" data-index="" data-num="3" data-click="{'button_tp':'filter_affs'}">Electron. Lab., ...</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20affs%3A%28Centro%20Internacional%20de%20M%C3%A9todos%20Computacionales%20en%20Ingenier%C3%ADa%20%28CIMEC%29%2C%20Instituto%20de%20Desarrollo%20Tecnol%C3%B3gico%20para%20la%20Industria%29" class="OP_LOG_BTN sc_nav_tag left_list_short_show" title="Centro Internacional de Métodos Computacionales en Ingeniería (CIMEC), Instituto de Desarrollo Tecnológico para la Industria" data-index="" data-num="3" data-click="{'button_tp':'filter_affs'}">Centro Internaci...</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20affs%3A%28University%20of%20California%2C%20Berkeley%29" class="OP_LOG_BTN sc_nav_tag left_list_short_show" title="University of California, Berkeley" data-index="" data-num="3" data-click="{'button_tp':'filter_affs'}">University of Ca...</a>
            <a href="javascript:;" class="leftnav_showmore">+</a>                                                                                    <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20affs%3A%28%E4%B8%AD%E5%9B%BD%E5%9C%B0%E8%B4%A8%E5%A4%A7%E5%AD%A6%29" class="OP_LOG_BTN sc_nav_tag " title="中国地质大学" data-index="" data-num="2" data-click="{'button_tp':'filter_affs'}">中国地质大学</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20affs%3A%28University%20of%20California%20Davis%29" class="OP_LOG_BTN sc_nav_tag " title="University of California Davis" data-index="" data-num="2" data-click="{'button_tp':'filter_affs'}">University of Ca...</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20affs%3A%28The%20University%20of%20Queensland%29" class="OP_LOG_BTN sc_nav_tag " title="The University of Queensland" data-index="" data-num="2" data-click="{'button_tp':'filter_affs'}">The University o...</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20affs%3A%28Technical%20University%20of%20Denmark%29" class="OP_LOG_BTN sc_nav_tag " title="Technical University of Denmark" data-index="" data-num="2" data-click="{'button_tp':'filter_affs'}">Technical Univer...</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20affs%3A%28Space%20Telescope%20Science%20Institute%29" class="OP_LOG_BTN sc_nav_tag " title="Space Telescope Science Institute" data-index="" data-num="2" data-click="{'button_tp':'filter_affs'}">Space Telescope ...</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20affs%3A%28Sandia%20National%20Laboratories%29" class="OP_LOG_BTN sc_nav_tag " title="Sandia National Laboratories" data-index="" data-num="2" data-click="{'button_tp':'filter_affs'}">Sandia National ...</a>
                                                                                                <a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;bcp=2&amp;ie=utf-8&amp;tag_filter=%20%20%20affs%3A%28Electron.%20Lab.%2C%20Swiss%20Federal%20Inst.%20of%20Technol.%2C%20Lausanne%2C%20Switzerland%29" class="OP_LOG_BTN sc_nav_tag " title="Electron. Lab., Swiss Federal Inst. of Technol., Lausanne, Switzerland" data-index="" data-num="2" data-click="{'button_tp':'filter_affs'}">Electron. Lab., ...</a>
                            <a href="javascript:;" class="leftnav_hidemore">-</a>
        </div>
        </div>
    
    </div>
    </div>
    
    </div>
    <div id="content_leftrs">
    
        <div id="bdxs_result_lists">
            
            
            
                    <div id="toolbar">

    <div class="sort_container">
<div class="sortwr">
    <div class="sort_select_default"><i class="iconfont"></i><span>按相关性</span></div><ul class="sort_list" style="display: none;"><li class="select"><a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;ie=utf-8" onmousedown="return ns_c_xs({'fm':'beha','button_tp':'asso'})" class="c-icon-down-gray-hover">按相关性</a></li><li><a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;ie=utf-8&amp;sort=sc_cited" onmousedown="return ns_c_xs({'fm':'beha','button_tp':'refer_num'})" class="c-icon-down-gray-hover">按被引量</a></li><li><a href="/s?wd=python&amp;tn=SE_baiduxueshu_c1gjeupa&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;ie=utf-8&amp;sort=sc_time" onmousedown="return ns_c_xs({'fm':'beha','button_tp':'pub_t'})" class="c-icon-down-gray-hover">按时间降序</a></li></ul>
</div>
</div>
<script>
bds.ready(function() {
    $sortList = $('.sort_list');
    $('.sort_select_default').on('mouseover', function(event) {
        $sortList.show();
        event.stopPropagation();
    });
    $sortList.on('mouseover', function(event) {
        $sortList.show();
        event.stopPropagation();
    });
    $sortList.on('mouseout', function(event) {
        $sortList.hide();
        event.stopPropagation();
    });
    $('body').on('mouseover', function(event) {
        $sortList.hide();
    });
});
</script>






<span class="nums">
    找到约315,000条相关结果
</span>

</div>


            

            
                                    







            
                                                    
                






<!--  -->

<div id="1" class="result sc_default_result xpath-log" srcid="3875" tpl="se_st_sc_default" mu="    http://doi.ieeecomputersociety.org/10.1109/MCSE.2007.58
">
<div class="sc_content">
    <h3 class="t c_font">
        
                    <a href="/s?wd=paperuri%3A%2824d6e6a87deb7f0306dd4c863bbd38a5%29&amp;filter=sc_long_sign&amp;sc_ks_para=q%3DPython%20for%20Scientific%20Computing&amp;sc_us=10997961392290844595&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" data-click="{'button_tp':'title'}" target="_blank"><em>Python</em> for Scientific Computing</a>
            </h3>
    <div class="sc_info">
                <span>                                
                        
        
                                
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Travis%20E.%20Oliphant%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">TE Oliphant</a>
                    </span>&nbsp;-&nbsp;        
                <span>
        
    <a href="                    /usercenter/data/journal?cmd=jump&amp;wd=journaluri%3A%28dabcc5ff239cb9b6%29%20%E3%80%8AComputing%20in%20Science%20%26%20Engineering%E3%80%8B&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dpublish&amp;sort=sc_cited" target="_blank" data-click="{'button_tp':'publish'}" title="《Computing in Science &amp; Engineering》">
    《Computing in Sci...
</a>
        </span>
        
                    &nbsp;-&nbsp;            <span class="sc_time" data-year="2007">
            2007</span>
                        &nbsp;-&nbsp;
        <span class="">
            被引量:&nbsp;
                        <a href="/s?wd=refpaperuri:(24d6e6a87deb7f0306dd4c863bbd38a5)&amp;sc_f_para=sc_cita%3D%7BPython%20for%20Scientific%20Computing%2C%20%20%20%20%20%20%20%20%20%20%20%20824%0D%0A%20%20%20%20%7D&amp;sort=sc_cited&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" target="_blank" class="sc_cite_cont" data-click="{'button_tp':'sc_cited'}">
                                    824
    
            </a>        </span>
    </div>
    <div class="c_abstract">
            <em>Python</em> is an excellent "steering" language for scientific codes written in other languages. However, with additional basic tools, <em>Python</em> transforms into...
        
        
                                    <div class="sc_allversion">
        <span>来源：</span>
                                    
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=01bfb7cc3b6d55fbc5937e275b0e7e7c/060828381f30e9249fb147234a086e061d95f78f.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="IEEE Computer Society" target="_blank" href="    http://doi.ieeecomputersociety.org/10.1109/MCSE.2007.58&#10;" data-click="{'button_tp':'allversion_link'}">
                IEEE Computer Soci...
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=76d4cbb55fee3d6d22938fca753a5c14/9f2f070828381f30cecd55bbaf014c086f06f0c8.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="AIP" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%2824d6e6a87deb7f0306dd4c863bbd38a5%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fscitation.aip.org%2Fcontent%2Faip%2Fjournal%2Fcise%2F9%2F3%2F10.1109%2FMCSE.2007.58&amp;ie=utf-8&amp;sc_us=10997961392290844595" data-click="{'button_tp':'allversion_link'}">
                AIP
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=42808ff2f103918fd78435cb671117a1/8ad4b31c8701a18ba671ca5d982f07082838fe0e.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="Oxford Univ Press" target="_blank" href="    http://icb.oxfordjournals.org/external-ref?access_num=10.1109/MCSE.2007.58&amp;amp;link_type=DOI&#10;" data-click="{'button_tp':'allversion_link'}">
                Oxford Univ Press
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=3cacdd6c231f95caa6a09ab7ff3b4e08/5d6034a85edf8db160b5a4760f23dd54564e740d.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="ResearchGate" target="_blank" href="    http://www.researchgate.net/profile/Travis_Oliphant/publication/3422935_Python_for_Scientific_Computing/links/548f0b680cf225bf66a7f9c3.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                ResearchGate
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=4376a6d9fdedab64742745c1c11a9ef5/dcc451da81cb39db5184bf44d6160924ab183058.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="IEEEXplore" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%2824d6e6a87deb7f0306dd4c863bbd38a5%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fieeexplore.ieee.org%2Fdocument%2F4160250%2F&amp;ie=utf-8&amp;sc_us=10997961392290844595" data-click="{'button_tp':'allversion_link'}">
                IEEEXplore
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="Cell Press" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%2824d6e6a87deb7f0306dd4c863bbd38a5%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fwww.cell.com%2Fservlet%2Flinkout%3Fsuffix%3De_1_5_1_2_60_2%26amp%3Bdbid%3D16%26amp%3Bdoi%3D10.1016%2Fj.molp.2015.06.005%26amp%3Bkey%3D10.1109%252FMCSE.2007.58%26amp%3Bcf%3D&amp;ie=utf-8&amp;sc_us=10997961392290844595" data-click="{'button_tp':'allversion_link'}">
                Cell Press
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=01bfb7cc3b6d55fbc5937e275b0e7e7c/060828381f30e9249fb147234a086e061d95f78f.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="IEEE Computer Society" target="_blank" href="    http://www.computer.org/csdl/mags/cs/2007/03/c3010-abs.html&#10;" data-click="{'button_tp':'allversion_link'}">
                IEEE Computer Soci...
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="AACR" target="_blank" href="    http://cancerres.aacrjournals.org/external-ref?access_num=10.1109/MCSE.2007.58&amp;amp;link_type=DOI&#10;" data-click="{'button_tp':'allversion_link'}">
                AACR
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=3cacdd6c231f95caa6a09ab7ff3b4e08/5d6034a85edf8db160b5a4760f23dd54564e740d.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="ResearchGate" target="_blank" href="    http://www.researchgate.net/publication/3422935_Python_for_Scientific_Computing&#10;" data-click="{'button_tp':'allversion_link'}">
                ResearchGate
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="dx.doi.org" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%2824d6e6a87deb7f0306dd4c863bbd38a5%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fdx.doi.org%2F10.1109%252FMCSE.2007.58&amp;ie=utf-8&amp;sc_us=10997961392290844595" data-click="{'button_tp':'allversion_link'}">
                dx.doi.org
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="mendeley.com" target="_blank" href="    http://www.mendeley.com/catalog/python-scientific-computing/&#10;" data-click="{'button_tp':'allversion_link'}">
                mendeley.com
            </a>
                                </span>
        
                    <a href="javascript:;" class="v_morebtn" data-click="{'button_tp':'allversion_more'}">&nbsp;&nbsp;</a>
                </div>
            </div>
</div>
<div class="sc_ext">
    <div class="sc_subject">
                                                    <a href="//xueshu.baidu.com/u/biye/?tag=paper&amp;wd=scientific%20computing" data-click="{'button_tp':'sc_search'}" target="_blank">scientific computing</a>
                        </div>
    <div class="sc_other">
                            
        
        <a href="    http://www.researchgate.net/profile/Travis_Oliphant/publication/3422935_Python_for_Scientific_Computing/links/548f0b680cf225bf66a7f9c3.pdf&#10;" class="sc_download c-icon-download-hover" target="_blank" data-click="{'button_tp':'download'}" title="从ResearchGate下载"><i class="iconfont icon-download"></i>免费下载&nbsp; </a>
<a target="_blank" class="sc_batch" href="javascript:;" data-click="{'button_tp':'batch'}" title="批量引用"><i class="iconfont icon-piliang"></i><span class="commType">批量引用&nbsp; </span></a><a class="sc_q c-icon-shape-hover" href="javascript:;" data-link="http://doi.ieeecomputersociety.org/10.1109/MCSE.2007.58" data-sign="5838ce047c7e47dba510c72c8bc44b60" data-click="{'button_tp':'cite'}" title="引用"><i class="iconfont icon-cite"></i>引用</a><a class="sc_collect c-icon-heart-hover" href="#" target="_blank" data-url="http://doi.ieeecomputersociety.org/10.1109/MCSE.2007.58" data-urlmd="722ced82411732922d92413f68d0e009" data-click="{'button_tp':'collect'}" title="收藏"><i class="iconfont icon-heart"></i>收藏</a>
    </div>
</div>
<i class="reqdata" style="display:none;" urlmd="722ced82411732922d92413f68d0e009" url="http://doi.ieeecomputersociety.org/10.1109/MCSE.2007.58" longsign="24d6e6a87deb7f0306dd4c863bbd38a5" diversion="6443492727010099201"></i>
</div>


                
                        
            

            
                                    







            
                                                    
                






<!--  -->

<div id="2" class="result sc_default_result xpath-log" srcid="3875" tpl="se_st_sc_default" mu="    http://dl.acm.org/citation.cfm?id=1251830
">
<div class="sc_content">
    <h3 class="t c_font">
            <i class="c-icon c-icon-tushu-mark"></i>

                    <a href="/s?wd=paperuri%3A%28e819112b2e19cdc9beddd627e92c020b%29&amp;filter=sc_long_sign&amp;sc_ks_para=q%3DPython%20for%20Scientific%20Computing&amp;sc_us=3515432752704828125&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" data-click="{'button_tp':'title'}" target="_blank"><em>Python</em> for Scientific Computing</a>
            </h3>
    <div class="sc_info">
                <span>                                
                        
        
                                
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Travis%20E.%20Oliphant%29%20Brigham%20Young%20University&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">TE Oliphant</a>
                    </span>&nbsp;-&nbsp;        
                <span>
        
    IEEE Educational ...

        </span>
        
                    &nbsp;-&nbsp;            <span class="sc_time" data-year="2007">
            2007</span>
                        &nbsp;-&nbsp;
        <span class="">
            被引量:&nbsp;
                        <a href="/s?wd=refpaperuri:(e819112b2e19cdc9beddd627e92c020b)&amp;sc_f_para=sc_cita%3D%7BPython%20for%20Scientific%20Computing%2C%20%20%20%20%20%20%20%20%20%20%20%20733%0D%0A%20%20%20%20%7D&amp;sort=sc_cited&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" target="_blank" class="sc_cite_cont" data-click="{'button_tp':'sc_cited'}">
                                    733
    
            </a>        </span>
    </div>
    <div class="c_abstract">
            <em>Python</em> is an excellent "steering" language for scientific codes written in other languages. However, with additional basic tools, <em>Python</em> transforms into...
        
        
                                    <div class="sc_allversion">
        <span>来源：</span>
                                    
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=696e0472332ac65c67506e72cdde8327/0b46f21fbe096b63a5cd86420a338744eaf8acc8.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="ACM" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%28e819112b2e19cdc9beddd627e92c020b%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fdl.acm.org%2Fcitation.cfm%3Fid%3D1251830&amp;ie=utf-8&amp;sc_us=3515432752704828125" data-click="{'button_tp':'allversion_link'}">
                ACM
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="astro.sunysb.edu" target="_blank" href="    http://www.astro.sunysb.edu/mzingale/teaching/python_science.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                astro.sunysb.edu
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="sintef.no" target="_blank" href="    http://www.sintef.no/contentassets/9689621c8cda44d9b2bc91c5fba21135/vanschoren-01b---introduction---scientific-python.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                sintef.no
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="cecam.org" target="_blank" href="    http://www.cecam.org/upload/files/file_2131.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                cecam.org
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="whoi.edu" target="_blank" href="    http://www.whoi.edu/committees/WHIT/Archive/python.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                whoi.edu
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="science-it.aalto.fi" target="_blank" href="    http://science-it.aalto.fi/wp-content/uploads/sites/2/2016/06/numpy_lectures.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                science-it.aalto.fi
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
        
                    <a href="javascript:;" class="v_morebtn" data-click="{'button_tp':'allversion_more'}">&nbsp;&nbsp;</a>
                </div>
            </div>
</div>
<div class="sc_ext">
    <div class="sc_subject">
                                                    <a href="//xueshu.baidu.com/u/biye/?tag=paper&amp;wd=scientific%20computing" data-click="{'button_tp':'sc_search'}" target="_blank">scientific computing</a>
                        </div>
    <div class="sc_other">
            <a href="javascript:;" class="sc_download c-icon-download-hover" target="_blank" data-click="{'button_tp':'download'}" title="查看5个下载地址" data-type="2"><i class="iconfont icon-download"></i>免费下载&nbsp; </a>

    <div style="display:none;" class="sc_savalink_content">
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    186.5K
</p>
                                    <p class="saveurl">    http://www.astro.sunysb.edu/mzingale/teaching/python_science.pdf
</p>
            <p class="saveanchor">            astro.sunysb.edu
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    161.5K
</p>
                                    <p class="saveurl">    http://www.sintef.no/contentassets/9689621c8cda44d9b2bc91c5fba21135/vanschoren-01b---introduction---scientific-python.pdf
</p>
            <p class="saveanchor">            sintef.no
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    161.7K
</p>
                                    <p class="saveurl">    http://www.cecam.org/upload/files/file_2131.pdf
</p>
            <p class="saveanchor">            cecam.org
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    5.0M
</p>
                                    <p class="saveurl">    http://www.whoi.edu/committees/WHIT/Archive/python.pdf
</p>
            <p class="saveanchor">            whoi.edu
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    1.0M
</p>
                                    <p class="saveurl">    http://science-it.aalto.fi/wp-content/uploads/sites/2/2016/06/numpy_lectures.pdf
</p>
            <p class="saveanchor">            science-it.aalto.fi
    </p>
            <p class="savefree">全网免费</p>
        </div>
        </div>
<a target="_blank" class="sc_batch" href="javascript:;" data-click="{'button_tp':'batch'}" title="批量引用"><i class="iconfont icon-piliang"></i><span class="commType">批量引用&nbsp; </span></a><a class="sc_q c-icon-shape-hover" href="javascript:;" data-link="http://dl.acm.org/citation.cfm?id=1251830" data-sign="edefd50b4b9745da19b559df897eea66" data-click="{'button_tp':'cite'}" title="引用"><i class="iconfont icon-cite"></i>引用</a><a class="sc_collect c-icon-heart-hover" href="#" target="_blank" data-url="http://dl.acm.org/citation.cfm?id=1251830" data-urlmd="f471ba55aeaa04b1fda7ba141ce1e45b" data-click="{'button_tp':'collect'}" title="收藏"><i class="iconfont icon-heart"></i>收藏</a>
    </div>
</div>
<i class="reqdata" style="display:none;" urlmd="f471ba55aeaa04b1fda7ba141ce1e45b" url="http://dl.acm.org/citation.cfm?id=1251830" longsign="e819112b2e19cdc9beddd627e92c020b" diversion="6443492727010099201"></i>
</div>


                
                        
            

            
                                    


            
                                                    
                






<!--  -->

<div id="3" class="result sc_default_result xpath-log" srcid="3875" tpl="se_st_sc_default" mu="    http://www.mendeley.com/research/python-scientific-computing-1/
">
<div class="sc_content">
    <h3 class="t c_font">
        
                    <a href="/s?wd=paperuri%3A%28aac6b5239dd779bc4aa8b7d123254169%29&amp;filter=sc_long_sign&amp;sc_ks_para=q%3DPython%20for%20scientific%20computing&amp;sc_us=13400494014966901256&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" data-click="{'button_tp':'title'}" target="_blank"><em>Python</em> for scientific computing</a>
            </h3>
    <div class="sc_info">
                <span>                                
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                        
        
                                
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Aksimentiev%2C%20Al%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">A Aksimentiev</a>
        ，                                    
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Schulten%2C%20K%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">K Schulten</a>
        ，                                    
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Barducci%2C%20A%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">A Barducci</a>
        ，                                                                    ...</span>&nbsp;-&nbsp;        
        
                                <span class="sc_time" data-year="2007">
            2007</span>
                        &nbsp;-&nbsp;
        <span class="">
            被引量:&nbsp;
                        <a href="/s?wd=refpaperuri:(aac6b5239dd779bc4aa8b7d123254169)&amp;sc_f_para=sc_cita%3D%7BPython%20for%20scientific%20computing%2C%20%20%20%20%20%20%20%20%20%20%20%20621%0D%0A%20%20%20%20%7D&amp;sort=sc_cited&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" target="_blank" class="sc_cite_cont" data-click="{'button_tp':'sc_cited'}">
                                    621
    
            </a>        </span>
    </div>
    <div class="c_abstract">
                <em>Python</em> for scientific computingAksimentiev, AlSchulten, KBarducci, ABussi, GParrinello, MBezanilla, FranciscoBukauskas, Feliksas FVerselis, Vytas KDelemotte, LucieDehez, FrançoisOliphant TE. 2007. <em>Python</em> for scientific computing. Com...
        
        
                <div class="sc_allversion">
        <span>来源：</span>
                                    
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="mendeley.com" target="_blank" href="    http://www.mendeley.com/research/python-scientific-computing-1/&#10;" data-click="{'button_tp':'allversion_link'}">
                mendeley.com
            </a>
                                </span>
        
                </div>
            </div>
</div>
<div class="sc_ext">
    <div class="sc_subject">
                                                    <a href="//xueshu.baidu.com/u/biye/?tag=paper&amp;wd=scientific%20computing" data-click="{'button_tp':'sc_search'}" target="_blank">scientific computing</a>
                        </div>
    <div class="sc_other">
        <a target="_blank" class="sc_batch" href="javascript:;" data-click="{'button_tp':'batch'}" title="批量引用"><i class="iconfont icon-piliang"></i><span class="commType">批量引用&nbsp; </span></a><a class="sc_collect c-icon-heart-hover" href="#" target="_blank" data-url="http://www.mendeley.com/research/python-scientific-computing-1/" data-urlmd="18dcb64d493e553c1b6a99c5e7f588b1" data-click="{'button_tp':'collect'}" title="收藏"><i class="iconfont icon-heart"></i>收藏</a>
    </div>
</div>
<i class="reqdata" style="display:none;" urlmd="18dcb64d493e553c1b6a99c5e7f588b1" url="http://www.mendeley.com/research/python-scientific-computing-1/" longsign="aac6b5239dd779bc4aa8b7d123254169" diversion="6443492727010099201"></i>
</div>


                
                        
            

            
                                    







            
                                                    
                






<!--  -->

<div id="4" class="result sc_default_result xpath-log" srcid="1599" tpl="se_st_sc_default" mu="    http://bioinformatics.oxfordjournals.org/content/26/12/1569.full
">
<div class="sc_content">
    <h3 class="t c_font">
        
                    <a href="/s?wd=paperuri%3A%283450fc696fa2a123f51732122941ca0a%29&amp;filter=sc_long_sign&amp;sc_ks_para=q%3DDendroPy%3A%20a%20Python%20library%20for%20phylogenetic%20computing&amp;sc_us=13552912649160513002&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" data-click="{'button_tp':'title'}" target="_blank">DendroPy: a <em>Python</em> library for phylogenetic computing</a>
            </h3>
    <div class="sc_info">
                <span>                                
                                            
                        
        
                                
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Sukumaran%2C%20Jeet%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">J Sukumaran</a>
        ，                                    
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Holder%2C%20Mark%20T%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">MT Holder</a>
                    </span>&nbsp;-&nbsp;        
                <span>
        
    <a href="                    /usercenter/data/journal?cmd=jump&amp;wd=journaluri%3A%286bb08f9d1b4c591c%29%20%E3%80%8ABioinformatics%E3%80%8B&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dpublish&amp;sort=sc_cited" target="_blank" data-click="{'button_tp':'publish'}" title="《Bioinformatics》">
    《Bioinformatics》
</a>
        </span>
        
                    &nbsp;-&nbsp;            <span class="sc_time" data-year="2010">
            2010</span>
                        &nbsp;-&nbsp;
        <span class="">
            被引量:&nbsp;
                        <a href="/s?wd=refpaperuri:(3450fc696fa2a123f51732122941ca0a)&amp;sc_f_para=sc_cita%3D%7BDendroPy%3A%20a%20Python%20library%20for%20phylogenetic%20computing%2C%20%20%20%20%20%20%20%20%20%20%20%20552%0D%0A%20%20%20%20%7D&amp;sort=sc_cited&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" target="_blank" class="sc_cite_cont" data-click="{'button_tp':'sc_cited'}">
                                    552
    
            </a>        </span>
    </div>
    <div class="c_abstract">
            DendroPy is a cross-platform library for the <em>Python</em> programming language that provides for object-oriented reading, writing, simulation and manipulation...
        
        
                                    <div class="sc_allversion">
        <span>来源：</span>
                                    
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=42808ff2f103918fd78435cb671117a1/8ad4b31c8701a18ba671ca5d982f07082838fe0e.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="Oxford Univ Press" target="_blank" href="    http://bioinformatics.oxfordjournals.org/content/26/12/1569.full&#10;" data-click="{'button_tp':'allversion_link'}">
                Oxford Univ Press
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=5e69a4760f23dd542126af69e72582e8/4ec2d5628535e5dd726b7dcd70c6a7efce1b6259.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="万方" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%283450fc696fa2a123f51732122941ca0a%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fnew.med.wanfangdata.com.cn%2FPaper%2FDetail%3Fid%3DPeriodicalPaper_JJ0215930306&amp;ie=utf-8&amp;sc_us=13552912649160513002" data-click="{'button_tp':'allversion_link'}">
                万方
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=10ab8ffbf4d3572c66b794ddbc3f5211/b151f8198618367ac0cea7cf28738bd4b31ce559.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="Europe PMC" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%283450fc696fa2a123f51732122941ca0a%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Feuropepmc.org%2Fabstract%2FMED%2F20421198&amp;ie=utf-8&amp;sc_us=13552912649160513002" data-click="{'button_tp':'allversion_link'}">
                Europe PMC
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="minimanuscript.com" target="_blank" href="    http://minimanuscript.com/manuscripts/dendropy-a-python-library-for-phylogenet.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                minimanuscript.com
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=42808ff2f103918fd78435cb671117a1/8ad4b31c8701a18ba671ca5d982f07082838fe0e.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="Oxford Univ Press" target="_blank" href="    http://bioinformatics.oxfordjournals.org/content/early/2010/04/25/bioinformatics.btq228.full.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                Oxford Univ Press
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=8ff444553f12b31bc739c528b034074c/ac4bd11373f08202a6d6492d4dfbfbedab641b58.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="BioMed Central" target="_blank" href="    http://www.biomedcentral.com/pubmed/20421198&#10;" data-click="{'button_tp':'allversion_link'}">
                BioMed Central
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=eea9ba0e17dfa9ecfd7b5e1654fcc635/8718367adab44aed320966f6b51c8701a18bfb59.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="BioOne" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%283450fc696fa2a123f51732122941ca0a%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fwww.bioone.org%2Fservlet%2Flinkout%3Fsuffix%3Di0022-3395-98-6-1148-Sukumaran1%26amp%3Bdbid%3D8%26amp%3Bdoi%3D10.1645%252FGE-3117.1%26amp%3Bkey%3D20421198&amp;ie=utf-8&amp;sc_us=13552912649160513002" data-click="{'button_tp':'allversion_link'}">
                BioOne
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=0c249dafaf773912c4738d60ce35b72e/d043ad4bd11373f07825b48da20f4bfbfbed048e.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="NCBI" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%283450fc696fa2a123f51732122941ca0a%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fwww.ncbi.nlm.nih.gov%2Fpubmed%2F20421198&amp;ie=utf-8&amp;sc_us=13552912649160513002" data-click="{'button_tp':'allversion_link'}">
                NCBI
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="ingentaconnect.com" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%283450fc696fa2a123f51732122941ca0a%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fwww.ingentaconnect.com%2Fcontent%2Foup%2Fcabios%2F2010%2F00000026%2F00000012%2Fart00068&amp;ie=utf-8&amp;sc_us=13552912649160513002" data-click="{'button_tp':'allversion_link'}">
                ingentaconnect.com
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=3cacdd6c231f95caa6a09ab7ff3b4e08/5d6034a85edf8db160b5a4760f23dd54564e740d.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="ResearchGate" target="_blank" href="    http://www.researchgate.net/publication/43345424_DendroPy_a_Python_library_for_phylogenetic_computing?ev=auth_pub&#10;" data-click="{'button_tp':'allversion_link'}">
                ResearchGate
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="万方医学" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%283450fc696fa2a123f51732122941ca0a%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fmed.wanfangdata.com.cn%2FPaper%2FDetail%2FPeriodicalPaper_JJ0215930306&amp;ie=utf-8&amp;sc_us=13552912649160513002" data-click="{'button_tp':'allversion_link'}">
                万方医学
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="dx.doi.org" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%283450fc696fa2a123f51732122941ca0a%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fdx.doi.org%2F10.1093%2Fbioinformatics%2Fbtq228&amp;ie=utf-8&amp;sc_us=13552912649160513002" data-click="{'button_tp':'allversion_link'}">
                dx.doi.org
            </a>
                                </span>
        
                    <a href="javascript:;" class="v_morebtn" data-click="{'button_tp':'allversion_more'}">&nbsp;&nbsp;</a>
                </div>
            </div>
</div>
<div class="sc_ext">
    <div class="sc_subject">
                    </div>
    <div class="sc_other">
            <a href="javascript:;" class="sc_download c-icon-download-hover" target="_blank" data-click="{'button_tp':'download'}" title="查看2个下载地址" data-type="2"><i class="iconfont icon-download"></i>免费下载&nbsp; </a>

    <div style="display:none;" class="sc_savalink_content">
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    11.6K
</p>
                                    <p class="saveurl">    http://minimanuscript.com/manuscripts/dendropy-a-python-library-for-phylogenet.pdf
</p>
            <p class="saveanchor">            minimanuscript.com
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    81.3K
</p>
                                    <p class="saveurl">    http://bioinformatics.oxfordjournals.org/content/early/2010/04/25/bioinformatics.btq228.full.pdf
</p>
            <p class="saveanchor">            Oxford Univ Press
    </p>
            <p class="savefree">全网免费</p>
        </div>
        </div>
<a target="_blank" class="sc_batch" href="javascript:;" data-click="{'button_tp':'batch'}" title="批量引用"><i class="iconfont icon-piliang"></i><span class="commType">批量引用&nbsp; </span></a><a class="sc_q c-icon-shape-hover" href="javascript:;" data-link="http://bioinformatics.oxfordjournals.org/content/26/12/1569.full" data-sign="3224045458cb1a7de2c6c220339a88b2" data-click="{'button_tp':'cite'}" title="引用"><i class="iconfont icon-cite"></i>引用</a><a class="sc_collect c-icon-heart-hover" href="#" target="_blank" data-url="http://bioinformatics.oxfordjournals.org/content/26/12/1569.full" data-urlmd="e1f189fe802d8e41fabe0bff132da452" data-click="{'button_tp':'collect'}" title="收藏"><i class="iconfont icon-heart"></i>收藏</a>
    </div>
</div>
<i class="reqdata" style="display:none;" urlmd="e1f189fe802d8e41fabe0bff132da452" url="http://bioinformatics.oxfordjournals.org/content/26/12/1569.full" longsign="3450fc696fa2a123f51732122941ca0a" diversion="6443492727010099201"></i>
</div>


                
                        
            

            
                                    







            
                                                    
                






<!--  -->

<div id="5" class="result sc_default_result xpath-log" srcid="1599" tpl="se_st_sc_default" mu="    http://dl.acm.org/citation.cfm?id=1717171
">
<div class="sc_content">
    <h3 class="t c_font">
            <i class="c-icon c-icon-tushu-mark"></i>

                    <a href="/s?wd=paperuri%3A%28fea303e1e26e99280aa8b5a7f364c446%29&amp;filter=sc_long_sign&amp;sc_ks_para=q%3DNatural%20Language%20Processing%20with%20Python&amp;sc_us=8160956743343433037&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" data-click="{'button_tp':'title'}" target="_blank">Natural Language Processing with <em>Python</em></a>
            </h3>
    <div class="sc_info">
                <span>                                
                                            
                                            
                        
        
                                
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Bird%2C%20Steven%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">S Bird</a>
        ，                                    
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Klein%2C%20Ewan%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">E Klein</a>
        ，                                    
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Loper%2C%20Edward%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">E Loper</a>
                    </span>&nbsp;-&nbsp;        
                <span>
        
    东南大学出版社

        </span>
        
                    &nbsp;-&nbsp;            <span class="sc_time" data-year="2010">
            2010</span>
                        &nbsp;-&nbsp;
        <span class="">
            被引量:&nbsp;
                        <a href="/s?wd=refpaperuri:(fea303e1e26e99280aa8b5a7f364c446)&amp;sc_f_para=sc_cita%3D%7BNatural%20Language%20Processing%20with%20Python%2C%20%20%20%20%20%20%20%20%20%20%20%201505%0D%0A%20%20%20%20%7D&amp;sort=sc_cited&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" target="_blank" class="sc_cite_cont" data-click="{'button_tp':'sc_cited'}">
                                    1505
    
            </a>        </span>
    </div>
    <div class="c_abstract">
            This book offers a highly accessible introduction to natural language processing, the field that supports a variety of language technologies, from predi...
        
        
                                    <div class="sc_allversion">
        <span>来源：</span>
                                    
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=696e0472332ac65c67506e72cdde8327/0b46f21fbe096b63a5cd86420a338744eaf8acc8.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="ACM" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%28fea303e1e26e99280aa8b5a7f364c446%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fdl.acm.org%2Fcitation.cfm%3Fid%3D1717171&amp;ie=utf-8&amp;sc_us=8160956743343433037" data-click="{'button_tp':'allversion_link'}">
                ACM
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=3cacdd6c231f95caa6a09ab7ff3b4e08/5d6034a85edf8db160b5a4760f23dd54564e740d.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="ResearchGate" target="_blank" href="    http://www.researchgate.net/publication/220691633_Natural_Language_Processing_with_Python&#10;" data-click="{'button_tp':'allversion_link'}">
                ResearchGate
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="torontopubliclibrary.ca" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%28fea303e1e26e99280aa8b5a7f364c446%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fwww.torontopubliclibrary.ca%2Fdetail.jsp%3FEntt%3DRDM3092992%26amp%3BR%3D3092992&amp;ie=utf-8&amp;sc_us=8160956743343433037" data-click="{'button_tp':'allversion_link'}">
                torontopubliclibra...
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="anthology.aclweb.org" target="_blank" href="    http://anthology.aclweb.org/J/J10/J10-4009.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                anthology.aclweb.org
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="oez.es" target="_blank" href="    http://oez.es/Natural%20Language%20Processing%20with%20Python.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                oez.es
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="index-of.es" target="_blank" href="    http://index-of.es/PYTHON/Natural.Language.Processing.with.Python.Steven.Bird.2009.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                index-of.es
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="bokus.com" target="_blank" href="    http://www.bokus.com/cgi-bin/product_search.cgi?authors=Ewan%20Klein&#10;" data-click="{'button_tp':'allversion_link'}">
                bokus.com
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="mendeley.com" target="_blank" href="    http://www.mendeley.com/catalog/natural-language-processing-python/&#10;" data-click="{'button_tp':'allversion_link'}">
                mendeley.com
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="oreilly.com" target="_blank" href="    http://www.oreilly.com/catalog/9780596516499&#10;" data-click="{'button_tp':'allversion_link'}">
                oreilly.com
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="morebooks.de" target="_blank" href="    http://www.morebooks.de/store/us/book/natural-language-processing-with-python/isbn/9780596516499&#10;" data-click="{'button_tp':'allversion_link'}">
                morebooks.de
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="cds.cern.ch" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%28fea303e1e26e99280aa8b5a7f364c446%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fcds.cern.ch%2Frecord%2F1194721&amp;ie=utf-8&amp;sc_us=8160956743343433037" data-click="{'button_tp':'allversion_link'}">
                cds.cern.ch
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="oreilly.de" target="_blank" href="    http://www.oreilly.de/catalog/9780596516499/&#10;" data-click="{'button_tp':'allversion_link'}">
                oreilly.de
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="hdl.handle.net" target="_blank" href="    http://hdl.handle.net/11343/31132&#10;" data-click="{'button_tp':'allversion_link'}">
                hdl.handle.net
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="aclweb.org" target="_blank" href="    http://www.aclweb.org/anthology-new/J/J10/J10-4009.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                aclweb.org
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="ar.newsmth.net" target="_blank" href="    http://ar.newsmth.net/att/12ec608dd678d8/OReilly.Natural.Language.Processing.with.Python.2009.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                ar.newsmth.net
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
        
                    <a href="javascript:;" class="v_morebtn" data-click="{'button_tp':'allversion_more'}">&nbsp;&nbsp;</a>
                </div>
            </div>
</div>
<div class="sc_ext">
    <div class="sc_subject">
                                                    <a href="//xueshu.baidu.com/u/biye/?tag=paper&amp;wd=Language%20Processing" data-click="{'button_tp':'sc_search'}" target="_blank">Language Processing</a>
                        </div>
    <div class="sc_other">
            <a href="javascript:;" class="sc_download c-icon-download-hover" target="_blank" data-click="{'button_tp':'download'}" title="查看5个下载地址" data-type="2"><i class="iconfont icon-download"></i>免费下载&nbsp; </a>

    <div style="display:none;" class="sc_savalink_content">
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    49.3K
</p>
                                    <p class="saveurl">    http://anthology.aclweb.org/J/J10/J10-4009.pdf
</p>
            <p class="saveanchor">            anthology.aclweb.org
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    3.1M
</p>
                                    <p class="saveurl">    http://oez.es/Natural%20Language%20Processing%20with%20Python.pdf
</p>
            <p class="saveanchor">            oez.es
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    4.1M
</p>
                                    <p class="saveurl">    http://index-of.es/PYTHON/Natural.Language.Processing.with.Python.Steven.Bird.2009.pdf
</p>
            <p class="saveanchor">            index-of.es
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    49.3K
</p>
                                    <p class="saveurl">    http://www.aclweb.org/anthology-new/J/J10/J10-4009.pdf
</p>
            <p class="saveanchor">            aclweb.org
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    3.4M
</p>
                                    <p class="saveurl">    http://ar.newsmth.net/att/12ec608dd678d8/OReilly.Natural.Language.Processing.with.Python.2009.pdf
</p>
            <p class="saveanchor">            ar.newsmth.net
    </p>
            <p class="savefree">全网免费</p>
        </div>
        </div>
<a target="_blank" class="sc_batch" href="javascript:;" data-click="{'button_tp':'batch'}" title="批量引用"><i class="iconfont icon-piliang"></i><span class="commType">批量引用&nbsp; </span></a><a class="sc_q c-icon-shape-hover" href="javascript:;" data-link="http://dl.acm.org/citation.cfm?id=1717171" data-sign="7edd3ccfb2393fb7fc0cc89965ff7c20" data-click="{'button_tp':'cite'}" title="引用"><i class="iconfont icon-cite"></i>引用</a><a class="sc_collect c-icon-heart-hover" href="#" target="_blank" data-url="http://dl.acm.org/citation.cfm?id=1717171" data-urlmd="c143431ddf6e36a5c95796685a66025e" data-click="{'button_tp':'collect'}" title="收藏"><i class="iconfont icon-heart"></i>收藏</a>
    </div>
</div>
<i class="reqdata" style="display:none;" urlmd="c143431ddf6e36a5c95796685a66025e" url="http://dl.acm.org/citation.cfm?id=1717171" longsign="fea303e1e26e99280aa8b5a7f364c446" diversion="6443492727010099201"></i>
</div>


                
                        
            

            
                                    







            
                                                    
                






<!--  -->

<div id="6" class="result sc_default_result xpath-log" srcid="1599" tpl="se_st_sc_default" mu="    http://dl.acm.org/citation.cfm?id=1953048.2078195
">
<div class="sc_content">
    <h3 class="t c_font">
        
                    <a href="/s?wd=paperuri%3A%28687552c72444691d032ad1795a46d4f5%29&amp;filter=sc_long_sign&amp;sc_ks_para=q%3DScikit-learn%3A%20Machine%20Learning%20in%20Python&amp;sc_us=2412746437885492380&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" data-click="{'button_tp':'title'}" target="_blank">Scikit-learn: Machine Learning in <em>Python</em></a>
            </h3>
    <div class="sc_info">
                <span>                                
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                        
        
                                
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Fabian%20Pedregosa%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">F Pedregosa</a>
        ，                                    
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Alexandre%20Gramfort%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">A Gramfort</a>
        ，                                    
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Vincent%20Michel%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">V Michel</a>
        ，                                                                    ...</span>&nbsp;-&nbsp;        
                <span>
        
    <a href="                    /usercenter/data/journal?cmd=jump&amp;wd=journaluri%3A%28161138c427a13dfc%29%20%E3%80%8AJournal%20of%20Machine%20Learning%20Research%E3%80%8B&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dpublish&amp;sort=sc_cited" target="_blank" data-click="{'button_tp':'publish'}" title="《Journal of Machine Learning Research》">
    《Journal of Machi...
</a>
        </span>
        
                    &nbsp;-&nbsp;            <span class="sc_time" data-year="2012">
            2012</span>
                        &nbsp;-&nbsp;
        <span class="">
            被引量:&nbsp;
                        <a href="/s?wd=refpaperuri:(687552c72444691d032ad1795a46d4f5)&amp;sc_f_para=sc_cita%3D%7BScikit-learn%3A%20Machine%20Learning%20in%20Python%2C%20%20%20%20%20%20%20%20%20%20%20%203895%0D%0A%20%20%20%20%7D&amp;sort=sc_cited&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" target="_blank" class="sc_cite_cont" data-click="{'button_tp':'sc_cited'}">
                                    3895
    
            </a>        </span>
    </div>
    <div class="c_abstract">
            Scikit-learn is a <em>Python</em> module integrating a wide range of state-of-the-art machine learning algorithms for medium-scale supervised and unsupervised pr...
        
        
                                    <div class="sc_allversion">
        <span>来源：</span>
                                    
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=696e0472332ac65c67506e72cdde8327/0b46f21fbe096b63a5cd86420a338744eaf8acc8.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="ACM" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%28687552c72444691d032ad1795a46d4f5%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fdl.acm.org%2Fcitation.cfm%3Fid%3D1953048.2078195&amp;ie=utf-8&amp;sc_us=2412746437885492380" data-click="{'button_tp':'allversion_link'}">
                ACM
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=953b8d0564d0f703e6e79ddd3ed6600b/2f738bd4b31c8701bea369f4217f9e2f0708ff8f.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="OALib" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%28687552c72444691d032ad1795a46d4f5%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fwww.oalib.com%2Fpaper%2F4030109&amp;ie=utf-8&amp;sc_us=2412746437885492380" data-click="{'button_tp':'allversion_link'}">
                OALib
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="arXiv.org" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%28687552c72444691d032ad1795a46d4f5%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Farxiv.org%2Fabs%2F1201.0490&amp;ie=utf-8&amp;sc_us=2412746437885492380" data-click="{'button_tp':'allversion_link'}">
                arXiv.org
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="ee.columbia.edu" target="_blank" href="    http://www.ee.columbia.edu/~ronw/pubs/jmlr2011-scikit-learn.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                ee.columbia.edu
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=a08f0ddc9f25bc312b08099968f3bc87/203fb80e7bec54e7bbabc20cbf389b504fc26a59.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="Citeseer" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%28687552c72444691d032ad1795a46d4f5%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fciteseerx.ist.psu.edu%2Fviewdoc%2Fdownload%3Bjsessionid%3D7EDD383E952568DE2EB9299CB3E90AB4%3Fdoi%3D10.1.1.220.3128%26rep%3Drep1%26type%3Dpdf&amp;ie=utf-8&amp;sc_us=2412746437885492380" data-click="{'button_tp':'allversion_link'}">
                Citeseer
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="pdfs.semanticscholar.org" target="_blank" href="    http://pdfs.semanticscholar.org/7b0b/9776debdc532e01b5bdcc84dcf413a68bd6f.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                pdfs.semanticschol...
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="adsabs.harvard.edu" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%28687552c72444691d032ad1795a46d4f5%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fadsabs.harvard.edu%2Fabs%2F2012arXiv1201.0490P&amp;ie=utf-8&amp;sc_us=2412746437885492380" data-click="{'button_tp':'allversion_link'}">
                adsabs.harvard.edu
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=3cacdd6c231f95caa6a09ab7ff3b4e08/5d6034a85edf8db160b5a4760f23dd54564e740d.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="ResearchGate" target="_blank" href="    http://www.researchgate.net/publication/51969319_Scikit-learn_Machine_Learning_in_Python&#10;" data-click="{'button_tp':'allversion_link'}">
                ResearchGate
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="mendeley.com" target="_blank" href="    http://www.mendeley.com/research/scikitlearn-machine-learning-python&#10;" data-click="{'button_tp':'allversion_link'}">
                mendeley.com
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="hal.archives-ouvertes.fr" target="_blank" href="    http://hal.archives-ouvertes.fr/hal-00650905/&#10;" data-click="{'button_tp':'allversion_link'}">
                hal.archives-ouver...
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="inspirehep.net" target="_blank" href="    http://inspirehep.net/record/1451725/&#10;" data-click="{'button_tp':'allversion_link'}">
                inspirehep.net
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="hal.inria.fr" target="_blank" href="    http://hal.inria.fr/hal-00650905&#10;" data-click="{'button_tp':'allversion_link'}">
                hal.inria.fr
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="jmlr.csail.mit.edu" target="_blank" href="    http://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html&#10;" data-click="{'button_tp':'allversion_link'}">
                jmlr.csail.mit.edu
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=3cacdd6c231f95caa6a09ab7ff3b4e08/5d6034a85edf8db160b5a4760f23dd54564e740d.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="ResearchGate" target="_blank" href="    http://www.researchgate.net/profile/Vincent_Dubourg/publication/51969319_Scikit-learn_Machine_Learning_in_Python/links/0fcfd5087eb7bb8f93000000&#10;" data-click="{'button_tp':'allversion_link'}">
                ResearchGate
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="hal.archives-ouvertes.fr" target="_blank" href="    http://hal.archives-ouvertes.fr/hal-00650905/PDF/pedregosa11a.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                hal.archives-ouver...
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
        
                    <a href="javascript:;" class="v_morebtn" data-click="{'button_tp':'allversion_more'}">&nbsp;&nbsp;</a>
                </div>
            </div>
</div>
<div class="sc_ext">
    <div class="sc_subject">
                                                    <a href="//xueshu.baidu.com/u/biye/?tag=paper&amp;wd=Machine%20Learning" data-click="{'button_tp':'sc_search'}" target="_blank">Machine Learning</a>
                        </div>
    <div class="sc_other">
            <a href="javascript:;" class="sc_download c-icon-download-hover" target="_blank" data-click="{'button_tp':'download'}" title="查看5个下载地址" data-type="2"><i class="iconfont icon-download"></i>免费下载&nbsp; </a>

    <div style="display:none;" class="sc_savalink_content">
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    41.3K
</p>
                                    <p class="saveurl">    http://www.ee.columbia.edu/~ronw/pubs/jmlr2011-scikit-learn.pdf
</p>
            <p class="saveanchor">            ee.columbia.edu
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    86.7K
</p>
                                    <p class="saveurl">http://xueshu.baidu.com/s?wd=paperuri%3A%28687552c72444691d032ad1795a46d4f5%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fciteseerx.ist.psu.edu%2Fviewdoc%2Fdownload%3Bjsessionid%3D7EDD383E952568DE2EB9299CB3E90AB4%3Fdoi%3D10.1.1.220.3128%26rep%3Drep1%26type%3Dpdf&amp;ie=utf-8&amp;sc_us=2412746437885492380</p>
            <p class="saveanchor">            Citeseer
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    41.3K
</p>
                                    <p class="saveurl">    http://pdfs.semanticscholar.org/7b0b/9776debdc532e01b5bdcc84dcf413a68bd6f.pdf
</p>
            <p class="saveanchor">            pdfs.semanticscholar.org
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    98.3K
</p>
                                    <p class="saveurl">    http://www.researchgate.net/profile/Vincent_Dubourg/publication/51969319_Scikit-learn_Machine_Learning_in_Python/links/0fcfd5087eb7bb8f93000000
</p>
            <p class="saveanchor">            ResearchGate
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    504.3K
</p>
                                    <p class="saveurl">    http://hal.archives-ouvertes.fr/hal-00650905/PDF/pedregosa11a.pdf
</p>
            <p class="saveanchor">            hal.archives-ouvertes.fr
    </p>
            <p class="savefree">全网免费</p>
        </div>
        </div>
<a target="_blank" class="sc_batch" href="javascript:;" data-click="{'button_tp':'batch'}" title="批量引用"><i class="iconfont icon-piliang"></i><span class="commType">批量引用&nbsp; </span></a><a class="sc_q c-icon-shape-hover" href="javascript:;" data-link="http://dl.acm.org/citation.cfm?id=1953048.2078195" data-sign="c320e87e580c3a66fc2a9b8c0aca2c23" data-click="{'button_tp':'cite'}" title="引用"><i class="iconfont icon-cite"></i>引用</a><a class="sc_collect c-icon-heart-hover" href="#" target="_blank" data-url="http://dl.acm.org/citation.cfm?id=1953048.2078195" data-urlmd="ca02341d44e441df0c05bff61aa0ee2e" data-click="{'button_tp':'collect'}" title="收藏"><i class="iconfont icon-heart"></i>收藏</a>
    </div>
</div>
<i class="reqdata" style="display:none;" urlmd="ca02341d44e441df0c05bff61aa0ee2e" url="http://dl.acm.org/citation.cfm?id=1953048.2078195" longsign="687552c72444691d032ad1795a46d4f5" diversion="6443492727010099201"></i>
</div>


                
                        
            

            
                                    


            
                                                    
                






<!--  -->

<div id="7" class="result sc_default_result xpath-log" srcid="3875" tpl="se_st_sc_default" mu="    http://arxiv.org/abs/1605.02688
">
<div class="sc_content">
    <h3 class="t c_font">
        
                    <a href="/s?wd=paperuri%3A%280a6c865848bafe01f607b47255faf628%29&amp;filter=sc_long_sign&amp;sc_ks_para=q%3DTheano%3A%20A%20Python%20framework%20for%20fast%20computation%20of%20mathematical%20expressions&amp;sc_us=1570895007418326064&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" data-click="{'button_tp':'title'}" target="_blank">Theano: A <em>Python</em> framework for fast computation of mathematical expressions</a>
            </h3>
    <div class="sc_info">
                <span>                                
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                        
        
                                
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28The%20Theano%20Development%20Team%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">TTD Team</a>
        ，                                    
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Al-Rfou%2C%20Rami%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">R Al-Rfou</a>
        ，                                    
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Alain%2C%20Guillaume%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">G Alain</a>
        ，                                                                    ...</span>&nbsp;-&nbsp;        
        
                                <span class="sc_time" data-year="2016">
            2016</span>
                        &nbsp;-&nbsp;
        <span class="">
            被引量:&nbsp;
                        <a href="/s?wd=refpaperuri:(0a6c865848bafe01f607b47255faf628)&amp;sc_f_para=sc_cita%3D%7BTheano%3A%20A%20Python%20framework%20for%20fast%20computation%20of%20mathematical%20expressions%2C%20%20%20%20%20%20%20%20%20%20%20%20373%0D%0A%20%20%20%20%7D&amp;sort=sc_cited&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" target="_blank" class="sc_cite_cont" data-click="{'button_tp':'sc_cited'}">
                                    373
    
            </a>        </span>
    </div>
    <div class="c_abstract">
            Abstract:  Theano is a <em>Python</em> library that allows to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficien...
        
        
                                    <div class="sc_allversion">
        <span>来源：</span>
                                    
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="arXiv.org" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%280a6c865848bafe01f607b47255faf628%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Farxiv.org%2Fabs%2F1605.02688&amp;ie=utf-8&amp;sc_us=1570895007418326064" data-click="{'button_tp':'allversion_link'}">
                arXiv.org
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="adsabs.harvard.edu" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%280a6c865848bafe01f607b47255faf628%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fadsabs.harvard.edu%2Fabs%2F2016arXiv160502688T&amp;ie=utf-8&amp;sc_us=1570895007418326064" data-click="{'button_tp':'allversion_link'}">
                adsabs.harvard.edu
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=3cacdd6c231f95caa6a09ab7ff3b4e08/5d6034a85edf8db160b5a4760f23dd54564e740d.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="ResearchGate" target="_blank" href="    http://www.researchgate.net/publication/302569301_Theano_A_Python_framework_for_fast_computation_of_mathematical_expressions&#10;" data-click="{'button_tp':'allversion_link'}">
                ResearchGate
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="128.84.21.199" target="_blank" href="    http://128.84.21.199/pdf/1605.02688.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                128.84.21.199
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=3cacdd6c231f95caa6a09ab7ff3b4e08/5d6034a85edf8db160b5a4760f23dd54564e740d.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="ResearchGate" target="_blank" href="    http://www.researchgate.net/profile/Dumitru_Erhan/publication/302569301_Theano_A_Python_framework_for_fast_computation_of_mathematical_expressions/links/57335bc808ae298602dce993/Theano-A-Python-framework-for-fast-computation-of-mathematical-expressions.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                ResearchGate
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="arXiv.org" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%280a6c865848bafe01f607b47255faf628%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Farxiv.org%2Fpdf%2F1605.02688&amp;ie=utf-8&amp;sc_us=1570895007418326064" data-click="{'button_tp':'allversion_link'}">
                arXiv.org
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="mendeley.com" target="_blank" href="    http://www.mendeley.com/catalog/theano-python-framework-fast-computation-mathematical-expressions-1/&#10;" data-click="{'button_tp':'allversion_link'}">
                mendeley.com
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="iro.umontreal.ca" target="_blank" href="    http://www.iro.umontreal.ca/~lisa/publications2/index.php/publications/show/729&#10;" data-click="{'button_tp':'allversion_link'}">
                iro.umontreal.ca
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="mysciencework.com" target="_blank" href="    http://www.mysciencework.com/publication/show/theano-python-framework-fast-computation-mathematical-expressions-151ce184&#10;" data-click="{'button_tp':'allversion_link'}">
                mysciencework.com
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="hgpu.org" target="_blank" href="    http://hgpu.org/?p=15859&#10;" data-click="{'button_tp':'allversion_link'}">
                hgpu.org
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="scienceopen.com" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%280a6c865848bafe01f607b47255faf628%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fwww.scienceopen.com%2Freview%3Fvid%3Da477fb07-5b84-4830-88f5-5b4946f63ac0&amp;ie=utf-8&amp;sc_us=1570895007418326064" data-click="{'button_tp':'allversion_link'}">
                scienceopen.com
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="science-open.com" target="_blank" href="    http://www.science-open.com/document?vid=a477fb07-5b84-4830-88f5-5b4946f63ac0&#10;" data-click="{'button_tp':'allversion_link'}">
                science-open.com
            </a>
                                </span>
        
                    <a href="javascript:;" class="v_morebtn" data-click="{'button_tp':'allversion_more'}">&nbsp;&nbsp;</a>
                </div>
            </div>
</div>
<div class="sc_ext">
    <div class="sc_subject">
                    </div>
    <div class="sc_other">
            <a href="javascript:;" class="sc_download c-icon-download-hover" target="_blank" data-click="{'button_tp':'download'}" title="查看3个下载地址" data-type="2"><i class="iconfont icon-download"></i>免费下载&nbsp; </a>

    <div style="display:none;" class="sc_savalink_content">
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    419.8K
</p>
                                    <p class="saveurl">    http://128.84.21.199/pdf/1605.02688.pdf
</p>
            <p class="saveanchor">            128.84.21.199
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    419.8K
</p>
                                    <p class="saveurl">    http://www.researchgate.net/profile/Dumitru_Erhan/publication/302569301_Theano_A_Python_framework_for_fast_computation_of_mathematical_expressions/links/57335bc808ae298602dce993/Theano-A-Python-framework-for-fast-computation-of-mathematical-expressions.pdf
</p>
            <p class="saveanchor">            ResearchGate
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    419.8K
</p>
                                    <p class="saveurl">http://xueshu.baidu.com/s?wd=paperuri%3A%280a6c865848bafe01f607b47255faf628%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Farxiv.org%2Fpdf%2F1605.02688&amp;ie=utf-8&amp;sc_us=1570895007418326064</p>
            <p class="saveanchor">            arXiv.org
    </p>
            <p class="savefree">全网免费</p>
        </div>
        </div>
<a target="_blank" class="sc_batch" href="javascript:;" data-click="{'button_tp':'batch'}" title="批量引用"><i class="iconfont icon-piliang"></i><span class="commType">批量引用&nbsp; </span></a><a class="sc_q c-icon-shape-hover" href="javascript:;" data-link="http://arxiv.org/abs/1605.02688" data-sign="06b0a97b594022ba4c3c328ffb87cfaf" data-click="{'button_tp':'cite'}" title="引用"><i class="iconfont icon-cite"></i>引用</a><a class="sc_collect c-icon-heart-hover" href="#" target="_blank" data-url="http://arxiv.org/abs/1605.02688" data-urlmd="162fa1fb2aee9c3e33c5dadeac9ab68b" data-click="{'button_tp':'collect'}" title="收藏"><i class="iconfont icon-heart"></i>收藏</a>
    </div>
</div>
<i class="reqdata" style="display:none;" urlmd="162fa1fb2aee9c3e33c5dadeac9ab68b" url="http://arxiv.org/abs/1605.02688" longsign="0a6c865848bafe01f607b47255faf628" diversion="6443492727010099201"></i>
</div>


                
                        
            

            
                                    







            
                                                    
                






<!--  -->

<div id="8" class="result sc_default_result xpath-log" srcid="3875" tpl="se_st_sc_default" mu="    http://onlinelibrary.wiley.com/resolve/reference/PMED?id=19304878
">
<div class="sc_content">
    <h3 class="t c_font">
        
                    <a href="/s?wd=paperuri%3A%287c691d89905932fc81a49c5942f50aff%29&amp;filter=sc_long_sign&amp;sc_ks_para=q%3DBiopython%3A%20freely%20available%20Python%20tools%20for%20computational%20molecular%20biology%20and%20bioinformatics&amp;sc_us=18418650614013879171&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" data-click="{'button_tp':'title'}" target="_blank">Bio<em>python</em>: freely available <em>Python</em> tools for computational molecular biology and bioinformatics</a>
            </h3>
    <div class="sc_info">
                <span>                                
                        
        
                                
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Cock%20PJ%3B%20Antao%20T%3B%20Chang%20JT%3B%20Chapman%20BA%3B%20Cox%20CJ%3B%20Dalke%20A%3B%20Friedberg%20I%3B%20Hamelryck%20T%3B%20Kauff%20F%3B%20Wilczynski%20B%3B%20de%20Hoon%20MJ%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">Cock PJ; Antao T; Chang JT; Chapman BA; Cox CJ; Dalke A; Friedberg I; Hamelryck T; Kauff F; Wilczynski B; de Hoon MJ</a>
                    </span>&nbsp;-&nbsp;        
                <span>
        
    <a href="                    /usercenter/data/journal?cmd=jump&amp;wd=journaluri%3A%286bb08f9d1b4c591c%29%20%E3%80%8ABioinformatics%E3%80%8B&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dpublish&amp;sort=sc_cited" target="_blank" data-click="{'button_tp':'publish'}" title="《Bioinformatics》">
    《Bioinformatics》
</a>
        </span>
        
                    &nbsp;-&nbsp;            <span class="sc_time" data-year="2009">
            2009</span>
                        &nbsp;-&nbsp;
        <span class="">
            被引量:&nbsp;
                        <a href="/s?wd=refpaperuri:(7c691d89905932fc81a49c5942f50aff)&amp;sc_f_para=sc_cita%3D%7BBiopython%3A%20freely%20available%20Python%20tools%20for%20computational%20molecular%20biology%20and%20bioinformatics%2C%20%20%20%20%20%20%20%20%20%20%20%20831%0D%0A%20%20%20%20%7D&amp;sort=sc_cited&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" target="_blank" class="sc_cite_cont" data-click="{'button_tp':'sc_cited'}">
                                    831
    
            </a>        </span>
    </div>
    <div class="c_abstract">
            The Bio<em>python</em> project is a mature open source international collaboration of volunteer developers, providing <em>Python</em> libraries for a wide range of bioinf...
        
        
                                    <div class="sc_allversion">
        <span>来源：</span>
                                    
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=6784bf44d6160924dc70aa1ae22b04cc/9e3df8dcd100baa11c689fa94110b912c8fc2e58.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="Wiley" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%287c691d89905932fc81a49c5942f50aff%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fonlinelibrary.wiley.com%2Fresolve%2Freference%2FPMED%3Fid%3D19304878&amp;ie=utf-8&amp;sc_us=18418650614013879171" data-click="{'button_tp':'allversion_link'}">
                Wiley
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=10ab8ffbf4d3572c66b794ddbc3f5211/b151f8198618367ac0cea7cf28738bd4b31ce559.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="Europe PMC" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%287c691d89905932fc81a49c5942f50aff%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Feuropepmc.org%2Fabstract%2FMED%2F19304878&amp;ie=utf-8&amp;sc_us=18418650614013879171" data-click="{'button_tp':'allversion_link'}">
                Europe PMC
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=5e69a4760f23dd542126af69e72582e8/4ec2d5628535e5dd726b7dcd70c6a7efce1b6259.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="万方" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%287c691d89905932fc81a49c5942f50aff%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fnew.med.wanfangdata.com.cn%2FPaper%2FDetail%3Fid%3DPeriodicalPaper_JJ0218478339&amp;ie=utf-8&amp;sc_us=18418650614013879171" data-click="{'button_tp':'allversion_link'}">
                万方
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="folk.uio.no" target="_blank" href="    http://folk.uio.no/jonkl/StuffForMBV-INFx410/Articles/PJACock.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                folk.uio.no
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="minimanuscript.com" target="_blank" href="    http://minimanuscript.com/manuscripts/biopython-freely-available-python-tools.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                minimanuscript.com
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-pdf"></i>
                                        </span>

            
             <a class="v_source" title="popgen.net" target="_blank" href="    http://popgen.net/scipy/abstract.pdf&#10;" data-click="{'button_tp':'allversion_link'}">
                popgen.net
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=f67b4c66ab345982c5dfed933ad8009b/242dd42a2834349b629db697cfea15ce36d3be0d.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="ACS" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%287c691d89905932fc81a49c5942f50aff%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fpubs.acs.org%2Fservlet%2Flinkout%3Fsuffix%3Dref48%2Fcit48%26amp%3Bdbid%3D8%26amp%3Bdoi%3D10.1021%252Fcb500696t%26amp%3Bkey%3D19304878&amp;ie=utf-8&amp;sc_us=18418650614013879171" data-click="{'button_tp':'allversion_link'}">
                ACS
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=0c249dafaf773912c4738d60ce35b72e/d043ad4bd11373f07825b48da20f4bfbfbed048e.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="NCBI" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%287c691d89905932fc81a49c5942f50aff%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fwww.ncbi.nlm.nih.gov%2Fpubmed%2F19304878&amp;ie=utf-8&amp;sc_us=18418650614013879171" data-click="{'button_tp':'allversion_link'}">
                NCBI
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=42808ff2f103918fd78435cb671117a1/8ad4b31c8701a18ba671ca5d982f07082838fe0e.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="Oxford Univ Press" target="_blank" href="    http://bioinformatics.oxfordjournals.org/content/25/11/1422.full&#10;" data-click="{'button_tp':'allversion_link'}">
                Oxford Univ Press
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=19625a6745a98226b8942326bcae8837/34fae6cd7b899e51fd15e20644a7d933c8950d0d.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="Pubmed Central" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%287c691d89905932fc81a49c5942f50aff%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fpubmedcentralcanada.ca%2Fpmcc%2Farticles%2FPMC2682512%2F&amp;ie=utf-8&amp;sc_us=18418650614013879171" data-click="{'button_tp':'allversion_link'}">
                Pubmed Central
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="ingentaconnect.com" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%287c691d89905932fc81a49c5942f50aff%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fwww.ingentaconnect.com%2Fcontent%2Foup%2Fcabios%2F2009%2F00000025%2F00000011%2Fart00013&amp;ie=utf-8&amp;sc_us=18418650614013879171" data-click="{'button_tp':'allversion_link'}">
                ingentaconnect.com
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=3cacdd6c231f95caa6a09ab7ff3b4e08/5d6034a85edf8db160b5a4760f23dd54564e740d.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="ResearchGate" target="_blank" href="    http://www.researchgate.net/publication/24218302_Biopython_freely_available_Python_tools_for_computational_molecular_biology_and_bioinformatics&#10;" data-click="{'button_tp':'allversion_link'}">
                ResearchGate
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="万方医学" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%287c691d89905932fc81a49c5942f50aff%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fmed.wanfangdata.com.cn%2FPaper%2FDetail%2FPeriodicalPaper_PM19304878&amp;ie=utf-8&amp;sc_us=18418650614013879171" data-click="{'button_tp':'allversion_link'}">
                万方医学
            </a>
                                </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=10ab8ffbf4d3572c66b794ddbc3f5211/b151f8198618367ac0cea7cf28738bd4b31ce559.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="Europe PMC" target="_blank" href="    http://europepmc.org/articles/PMC2682512?pdf=render&#10;" data-click="{'button_tp':'allversion_link'}">
                Europe PMC
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
                                    
                <span class="v_item_span v_item_hid">
            <span class="v_icon">
                            <img src="http://hiphotos.baidu.com/space/wh%3D16%2C16/sign=3cacdd6c231f95caa6a09ab7ff3b4e08/5d6034a85edf8db160b5a4760f23dd54564e740d.jpg" width="16" height="16">
                        </span>

            
             <a class="v_source" title="ResearchGate" target="_blank" href="    http://www.researchgate.net/profile/Thomas_Hamelryck/publication/24218302_Biopython_freely_available_Python_tools_for_computational_molecular_biology_and_bioinformatics/links/0c96051b076799b0c7000000?ev=pub_ext_doc_dl_meta&#10;" data-click="{'button_tp':'allversion_link'}">
                ResearchGate
            </a>
                        <i class="c-icon c-icon-free v_freeicon"></i>
                                    <span class="v_lib">(全网免费下载)</span>
                    </span>
        
                    <a href="javascript:;" class="v_morebtn" data-click="{'button_tp':'allversion_more'}">&nbsp;&nbsp;</a>
                </div>
            </div>
</div>
<div class="sc_ext">
    <div class="sc_subject">
                                                    <a href="//xueshu.baidu.com/u/biye/?tag=paper&amp;wd=Computational%20Biology" data-click="{'button_tp':'sc_search'}" target="_blank">Computational Biology</a>
                                                        <a href="//xueshu.baidu.com/u/biye/?tag=paper&amp;wd=molecular%20biology" data-click="{'button_tp':'sc_search'}" target="_blank">molecular biology</a>
                        </div>
    <div class="sc_other">
            <a href="javascript:;" class="sc_download c-icon-download-hover" target="_blank" data-click="{'button_tp':'download'}" title="查看5个下载地址" data-type="2"><i class="iconfont icon-download"></i>免费下载&nbsp; </a>

    <div style="display:none;" class="sc_savalink_content">
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    68.7K
</p>
                                    <p class="saveurl">    http://folk.uio.no/jonkl/StuffForMBV-INFx410/Articles/PJACock.pdf
</p>
            <p class="saveanchor">            folk.uio.no
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    12.1K
</p>
                                    <p class="saveurl">    http://minimanuscript.com/manuscripts/biopython-freely-available-python-tools.pdf
</p>
            <p class="saveanchor">            minimanuscript.com
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    240.8K
</p>
                                    <p class="saveurl">    http://popgen.net/scipy/abstract.pdf
</p>
            <p class="saveanchor">            popgen.net
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    70.8K
</p>
                                    <p class="saveurl">    http://europepmc.org/articles/PMC2682512?pdf=render
</p>
            <p class="saveanchor">            Europe PMC
    </p>
            <p class="savefree">全网免费</p>
        </div>
                                            
        
        <div class="sc_savelink_item" data-type="pdf" data-libbuy="0">
                            <p class="savesize">    70.8K
</p>
                                    <p class="saveurl">    http://www.researchgate.net/profile/Thomas_Hamelryck/publication/24218302_Biopython_freely_available_Python_tools_for_computational_molecular_biology_and_bioinformatics/links/0c96051b076799b0c7000000?ev=pub_ext_doc_dl_meta
</p>
            <p class="saveanchor">            ResearchGate
    </p>
            <p class="savefree">全网免费</p>
        </div>
        </div>
<a target="_blank" class="sc_batch" href="javascript:;" data-click="{'button_tp':'batch'}" title="批量引用"><i class="iconfont icon-piliang"></i><span class="commType">批量引用&nbsp; </span></a><a class="sc_q c-icon-shape-hover" href="javascript:;" data-link="http://onlinelibrary.wiley.com/resolve/reference/PMED?id=19304878" data-sign="3726d19a5fbaed11e4c7210b2ef4c1ee" data-click="{'button_tp':'cite'}" title="引用"><i class="iconfont icon-cite"></i>引用</a><a class="sc_collect c-icon-heart-hover" href="#" target="_blank" data-url="http://onlinelibrary.wiley.com/resolve/reference/PMED?id=19304878" data-urlmd="f144d93b658c85cb389383960f7cf3e4" data-click="{'button_tp':'collect'}" title="收藏"><i class="iconfont icon-heart"></i>收藏</a>
    </div>
</div>
<i class="reqdata" style="display:none;" urlmd="f144d93b658c85cb389383960f7cf3e4" url="http://onlinelibrary.wiley.com/resolve/reference/PMED?id=19304878" longsign="7c691d89905932fc81a49c5942f50aff" diversion="6443492727010099201"></i>
</div>


                
                        
            

            
                                    


            
                                                    
                






<!--  -->

<div id="9" class="result sc_default_result xpath-log" srcid="3875" tpl="se_st_sc_default" mu="    http://www.mendeley.com/research/natural-language-processing-python-analyzing-text-natural-language-toolkit/
">
<div class="sc_content">
    <h3 class="t c_font">
        
                    <a href="/s?wd=paperuri%3A%2842766df836663fa6278ede92f27e3363%29&amp;filter=sc_long_sign&amp;sc_ks_para=q%3DNatural%20language%20processing%20with%20Python%3A%20%5Banalyzing%20text%20with%20the%20natural%20language%20toolkit%5D&amp;sc_us=7591962958796700450&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" data-click="{'button_tp':'title'}" target="_blank">Natural language processing with <em>Python</em>: [analyzing text with the natural language toolkit]</a>
            </h3>
    <div class="sc_info">
                <span>                                
                                            
                                            
                        
        
                                
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Bird%2C%20Steven%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">S Bird</a>
        ，                                    
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Klein%2C%20Ewan%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">E Klein</a>
        ，                                    
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Loper%2C%20Edward%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">E Loper</a>
                    </span>&nbsp;-&nbsp;        
        
                                <span class="sc_time" data-year="2009">
            2009</span>
                        &nbsp;-&nbsp;
        <span class="">
            被引量:&nbsp;
                        <a href="/s?wd=refpaperuri:(42766df836663fa6278ede92f27e3363)&amp;sc_f_para=sc_cita%3D%7BNatural%20language%20processing%20with%20Python%3A%20%5Banalyzing%20text%20with%20the%20natural%20language%20toolkit%5D%2C%20%20%20%20%20%20%20%20%20%20%20%201023%0D%0A%20%20%20%20%7D&amp;sort=sc_cited&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" target="_blank" class="sc_cite_cont" data-click="{'button_tp':'sc_cited'}">
                                    1023
    
            </a>        </span>
    </div>
    <div class="c_abstract">
                Natural Language Processing with <em>Python</em> --- Analyzing Text with the Natural Language ToolkitBird, StevenKlein, EwanLoper, Edward...
        
        
                <div class="sc_allversion">
        <span>来源：</span>
                                    
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="mendeley.com" target="_blank" href="    http://www.mendeley.com/research/natural-language-processing-python-analyzing-text-natural-language-toolkit/&#10;" data-click="{'button_tp':'allversion_link'}">
                mendeley.com
            </a>
                                </span>
                                    
                <span class="split">&nbsp;/&nbsp;</span>
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="lib.bvu.edu.vn" target="_blank" href="    http://lib.bvu.edu.vn/handle/TVDHBRVT/15952&#10;" data-click="{'button_tp':'allversion_link'}">
                lib.bvu.edu.vn
            </a>
                                </span>
        
                </div>
            </div>
</div>
<div class="sc_ext">
    <div class="sc_subject">
                                                    <a href="//xueshu.baidu.com/u/biye/?tag=paper&amp;wd=Language%20Processing" data-click="{'button_tp':'sc_search'}" target="_blank">Language Processing</a>
                                                        <a href="//xueshu.baidu.com/u/biye/?tag=paper&amp;wd=Natural%20Language" data-click="{'button_tp':'sc_search'}" target="_blank">Natural Language</a>
                        </div>
    <div class="sc_other">
        <a target="_blank" class="sc_batch" href="javascript:;" data-click="{'button_tp':'batch'}" title="批量引用"><i class="iconfont icon-piliang"></i><span class="commType">批量引用&nbsp; </span></a><a class="sc_collect c-icon-heart-hover" href="#" target="_blank" data-url="http://www.mendeley.com/research/natural-language-processing-python-analyzing-text-natural-language-toolkit/" data-urlmd="6bd18e8783782f0cb799d77b34c3a8aa" data-click="{'button_tp':'collect'}" title="收藏"><i class="iconfont icon-heart"></i>收藏</a>
    </div>
</div>
<i class="reqdata" style="display:none;" urlmd="6bd18e8783782f0cb799d77b34c3a8aa" url="http://www.mendeley.com/research/natural-language-processing-python-analyzing-text-natural-language-toolkit/" longsign="42766df836663fa6278ede92f27e3363" diversion="6443492727010099201"></i>
</div>


                
                        
            

            
                                    


            
                                                    
                






<!--  -->

<div id="10" class="result sc_default_result xpath-log" srcid="1599" tpl="se_st_sc_default" mu="    http://www.scienceopen.com/document/vid/2a8c877f-3835-494d-bba8-a02bca42fa7f
">
<div class="sc_content">
    <h3 class="t c_font">
        
                    <a href="/s?wd=paperuri%3A%2857fec4f47e9cecceea17fc310d331e9b%29&amp;filter=sc_long_sign&amp;sc_ks_para=q%3DAdams%20PD%2C%20Afonine%20PV%2C%20Bunkoczi%20G%2C%20Chen%20VB%2C%20Davis%20IW%2C%20et%20al.%20PHENIX%3A%20a%20comprehensive%20Python-based%20system%20for%20macromolecular%20structure%20solution&amp;sc_us=1527206804763994120&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" data-click="{'button_tp':'title'}" target="_blank">Adams PD, Afonine PV, Bunkoczi G, Chen VB, Davis IW, et al. PHENIX: a comprehensive <em>Python</em>-based system for macromolecular structure...</a>
            </h3>
    <div class="sc_info">
                <span>                                
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                        
        
                                
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Adams%2C%20P.%20D%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">PD Adams</a>
        ，                                    
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Afonine%2C%20P.%20V%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">PV Afonine</a>
        ，                                    
                        
        <a href="        &#10;                    &#10;/s?wd=author%3A%28Bunk%C3%B3czi%2C%20G%29%20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_hilight%3Dperson" target="_blank" data-click="{'button_tp':'author'}">G Bunkóczi</a>
        ，                                                                    ...</span>&nbsp;-&nbsp;        
        
                                <span class="sc_time" data-year="2010">
            2010</span>
                        &nbsp;-&nbsp;
        <span class="">
            被引量:&nbsp;
                        <a href="/s?wd=refpaperuri:(57fec4f47e9cecceea17fc310d331e9b)&amp;sc_f_para=sc_cita%3D%7BAdams%20PD%2C%20Afonine%20PV%2C%20Bunkoczi%20G%2C%20Chen%20VB%2C%20Davis%20IW%2C%20et%20al.%20PHENIX%3A%20a%20comprehensive%20Python-based%20system%20for%20macromolecular%20structure%20solution%2C%20%20%20%20%20%20%20%20%20%20%20%204021%0D%0A%20%20%20%20%7D&amp;sort=sc_cited&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8" target="_blank" class="sc_cite_cont" data-click="{'button_tp':'sc_cited'}">
                                    4021
    
            </a>        </span>
    </div>
    <div class="c_abstract">
                Adams PD, Afonine PV, Bunkoczi G, Chen VB, Davis IW, et al. PHENIX: a comprehensive <em>Python</em>-based system for macromolecular structure solutionAdams, P. DAfonine, P. VBunkóczi, GChen, V. BDavis, I. WEchols, NBunkoczi, GHeadd, JJHung, L...
        
        
                <div class="sc_allversion">
        <span>来源：</span>
                                    
                <span class="v_item_span">
            <span class="v_icon">
                                            <i class="c-icon c-icon-link"></i>
                                        </span>

            
             <a class="v_source" title="scienceopen.com" target="_blank" href="http://xueshu.baidu.com/s?wd=paperuri%3A%2857fec4f47e9cecceea17fc310d331e9b%29&amp;filter=sc_long_sign&amp;tn=SE_xueshusource_2kduw22v&amp;sc_vurl=http%3A%2F%2Fwww.scienceopen.com%2Fdocument%2Fvid%2F2a8c877f-3835-494d-bba8-a02bca42fa7f&amp;ie=utf-8&amp;sc_us=1527206804763994120" data-click="{'button_tp':'allversion_link'}">
                scienceopen.com
            </a>
                                </span>
        
                </div>
            </div>
</div>
<div class="sc_ext">
    <div class="sc_subject">
                    </div>
    <div class="sc_other">
        <a target="_blank" class="sc_batch" href="javascript:;" data-click="{'button_tp':'batch'}" title="批量引用"><i class="iconfont icon-piliang"></i><span class="commType">批量引用&nbsp; </span></a><a class="sc_collect c-icon-heart-hover" href="#" target="_blank" data-url="http://www.scienceopen.com/document/vid/2a8c877f-3835-494d-bba8-a02bca42fa7f" data-urlmd="98816a7b97cfed022f808fbabb8747e3" data-click="{'button_tp':'collect'}" title="收藏"><i class="iconfont icon-heart"></i>收藏</a>
    </div>
</div>
<i class="reqdata" style="display:none;" urlmd="98816a7b97cfed022f808fbabb8747e3" url="http://www.scienceopen.com/document/vid/2a8c877f-3835-494d-bba8-a02bca42fa7f" longsign="57fec4f47e9cecceea17fc310d331e9b" diversion="6443492727010099201"></i>
</div>


                
                        
            

                    </div>
    
    </div>
    <div id="searchTipBg" style="width: 100%; height: 100%; left: 0px; top: 0px; z-index: 999; opacity: 0.55; position: absolute; display: none; background-color: rgb(0, 0, 0);"></div><div id="searchTip" style="top: 5px; z-index: 1005; position: absolute; display: none; background-color: transparent;"><div class="tipbox" id="step1" style="visibility: visible; display: block;"><span class="tipboxBtn" onclick="hideTip()"></span><span class="tipboxNextbtn" onclick="hideTip();noShow()">我知道了</span></div><div class="tipText">学者主页功能全新上线，快来开启自己的学者主页，提升自己的学术影响力吧！</div></div><div id="guide-step"></div>
    
        <div style="clear:both;"></div>
        
                            
<p id="page">
		
							<strong>
				<span class="fk fk_cur"><i class="c-icon c-icon-bear-p"></i></span>
				<span class="pc">1</span>
			</strong>
										<a href="/s?wd=python&amp;pn=10&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1">
				<span class="fk fkd"><i class="c-icon c-icon-bear-pn"></i></span>
				<span class="pc">2</span>
			</a>
										<a href="/s?wd=python&amp;pn=20&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1">
				<span class="fk"><i class="c-icon c-icon-bear-pn"></i></span>
				<span class="pc">3</span>
			</a>
										<a href="/s?wd=python&amp;pn=30&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1">
				<span class="fk fkd"><i class="c-icon c-icon-bear-pn"></i></span>
				<span class="pc">4</span>
			</a>
										<a href="/s?wd=python&amp;pn=40&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1">
				<span class="fk"><i class="c-icon c-icon-bear-pn"></i></span>
				<span class="pc">5</span>
			</a>
										<a href="/s?wd=python&amp;pn=50&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1">
				<span class="fk fkd"><i class="c-icon c-icon-bear-pn"></i></span>
				<span class="pc">6</span>
			</a>
										<a href="/s?wd=python&amp;pn=60&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1">
				<span class="fk"><i class="c-icon c-icon-bear-pn"></i></span>
				<span class="pc">7</span>
			</a>
										<a href="/s?wd=python&amp;pn=70&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1">
				<span class="fk fkd"><i class="c-icon c-icon-bear-pn"></i></span>
				<span class="pc">8</span>
			</a>
					
		<a href="/s?wd=python&amp;pn=10&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8&amp;sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&amp;sc_hit=1&amp;rsv_page=1" class="n" style="margin-right: 19px;">下一页&gt;</a>
	
</p>

                    
    
</div>

	

			
			</div>
			
		
		</div>
					
		
		
	<div class="pagefoot" style="position: relative;"><div class="footcon"><span class="lawinfo"><h4>关于我们</h4><p>百度学术集成海量学术资源，融合人工智能、深度学习、大数据分析等技术，为科研工作者提供全面快捷的学术服务。在这里我们保持学习的态度，不忘初心，砥砺前行。</p></span><span class="contact"><h4>联系我们</h4><div class="innerCont"><a href="http://weibo.com/baiduxueshu" target="_blank"><p class="wb"><span class=""></span></p></a><p class="wx"><span class="qrcode weixincode biye_bg"><!--<i class="iconfont weixin">&#xe675;</i>--></span></p><a href="mailto:xueshu_support@baidu.com" target="_blank"><p class="help"></p></a></div></span><span class="suggest"><a href="javascript:;" class="feedback">意见反馈</a></span></div><p class="foottext">©2017 Baidu 百度学术声明 <a href="https://www.baidu.com/duty/" target="_blank">使用百度前必读</a></p></div>
	<div class="batch-container">
	<div class="batch-btn-wr">
		<div class="batch-btn">
			<i class="iconfont icon-piliang"></i><span>0</span>
		</div>
		<div class="batch-btn-tip" style="display: block;">
			<p>文献可以<span>批量引用</span>啦~<br>欢迎点我试用！</p><p>
		</p></div>
	</div>
	<div class="batch-file-container" style="transform: translateY(450px);">
		<div class="batch-file-header">
			<i class="iconfont icon-xlight batch-file-close"></i>批量引用(<span>0</span>)
			<a class="batch-file-controller-mail" href="javascript:;"><i class="iconfont icon-maillight"></i>
		    </a>
		    <a class="batch-file-controller-printer" href="javascript:;"><i class="iconfont icon-printer"></i></a>
		</div>
		<div class="batch-file-controller">
			<a class="batch-file-controller-clear" href="javascript:;">清空列表</a>
		    <div class="c-dropdown2 export-dropdown batch-file-controller-export c-dropdown2-common OP_LOG_BTN" data-click="{fm:'beha'}" tabindex="0" style="z-index: 200;"> 
		        <div class="c-dropdown2-btn-group">
		        	导出至
		            <div class="c-dropdown2-btn" style="display:none">导出至</div>
		        </div> 
		        <div class="c-dropdown2-menu" style="visibility: hidden; height: 143px;"> 
		            <div class="c-dropdown2-menu-inner" style="height: 156px;"> 
		                <ul class="c-dropdown2-menubox"> 
		                	<li class="c-dropdown2-option c-dropdown2-selected" data-value="0" style="display: none;" data-selected="selected">导出至</li> 
		                    <li class="c-dropdown2-option" data-value="EndNote"><a href="http://a.xueshu.baidu.com/usercenter/data/retpagebatch?cmd=export_folder&amp;format=enw" target="_blank" data-log="{'type': 'enw'}">EndNote (.enw)</a></li>  
		                    <li class="c-dropdown2-option" data-value="RefMan"><a href="http://a.xueshu.baidu.com/usercenter/data/retpagebatch?cmd=export_folder&amp;format=ris" target="_blank" data-log="{'type': 'ris'}">RefMan (.ris)</a></li>  
		                    <li class="c-dropdown2-option" data-value="NoteExpress"><a href="http://a.xueshu.baidu.com/usercenter/data/retpagebatch?cmd=export_folder&amp;format=net" target="_blank" data-log="{'type': 'net'}">NoteExpress (.net)</a></li>
		                    <li class="c-dropdown2-option" data-value="BibTex"><a href="http://a.xueshu.baidu.com/usercenter/data/retpagebatch?cmd=export_folder&amp;format=bib" target="_blank" data-log="{'type': 'bib'}">BibTex (.bib)</a></li>
		                    <li class="c-dropdown2-option" data-value="NoteFirst"><a href="http://a.xueshu.baidu.com/usercenter/data/retpagebatch?cmd=export_folder&amp;format=notefirst" target="_blank" data-log="{'type': 'notefirst'}">NoteFirst (.xml)</a></li>
		                    <!-- <li class="c-dropdown2-option" data-value="txt"><a href="http://a.xueshu.baidu.com/usercenter/data/retpagebatch?cmd=export_folder&format=citegbt" target="_blank" data-log="{'type': 'citegbt'}" >引文 (.txt)</a></li> -->
		                </ul> 
		            </div> 
		        </div> 
		    </div>

		    
		    <a class="batch-file-controller-collect" href="//xueshu.baidu.com/usercenter/?tab=collect" target="_blank">一键收藏</a>

		    <a class="batch-file-controller-copy" href="javascript:;">一键复制</a>
			<div class="c-dropdown2 format-dropdown c-dropdown2-common OP_LOG_BTN" data-click="{fm:'beha'}" tabindex="0" style="z-index: 198;"> 
		        <div class="c-dropdown2-btn-group"> 
		            <div class="c-dropdown2-btn">引用格式</div>
		            <div class="c-dropdown2-btn-icon">
		                <div class="c-dropdown2-btn-icon-border">
		                    <i class="c-icon c-icon-triangle-down"></i>
		                </div>
		            </div>
		        </div> 
		        <div class="c-dropdown2-menu" style="visibility: hidden; height: 112px;"> 
		            <div class="c-dropdown2-menu-inner" style="height: 130px;"> 
		                <ul class="c-dropdown2-menubox">
		                	<li class="c-dropdown2-option c-dropdown2-selected" data-value="Default" style="display: none;" data-selected="selected">引用格式</li> 
		                	<li class="c-dropdown2-option" data-value="Default">默认格式</li>  
		                    <li class="c-dropdown2-option" data-value="GBT7714">GB/T 7714</li>  
		                    <li class="c-dropdown2-option" data-value="MLA">MLA</li>  
		                    <li class="c-dropdown2-option" data-value="APA">APA</li>
		                </ul> 
		            </div> 
		        </div> 
		    </div>

			<div class="batch-file-controller-mail-inputbox" style="display: none;">
				<div><input class="batch-file-controller-mail-input" type="text" value="" placeholder="Example@mail.com" name="mail"><a class="batch-file-controller-mail-submit" href="javascript:;">发送</a></div>
			</div>
		</div>

		<div class="batch-file-list-container">
			<div class="batch-file-list opui-scroll-ctrl-content opui-scroll-onwheel">
				<ul></ul>
			</div><div class="opui-scroll-ctrl-scroll" data-click="{fm:&quot;beha&quot;}" style="height: 353px; display: none;"><div class="opui-scroll-axis" style="height: 353px;"></div><div class="opui-scroll-slider OP_LOG_BTN"><div class="opui-scroll-s-top"></div><div class="opui-scroll-s-bottom"></div><div class="opui-scroll-s-block"></div></div></div>
		</div>
		<div class="batch-file-mask">
			<div class="batch-file-mask-tips-btn">一键收藏</div>
			<div class="batch-file-mask-tips">一键收藏上线啦！点击收藏后，可在“我的收藏”页面管理已收藏文献</div>
		</div>
	</div>
</div>
	<div style="display:none">
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?43115ae30293b511088d3cbe41ec099c";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
</div>
			<script src="http://s1.bdstatic.com/r/www/cache/mid/static/jquery/jquery-1.10.2.min_65682a2.js"></script>
<script type="text/javascript" src="http://s1.bdstatic.com/r/www/cache/mid/static/xueshu/js/logic2_75a7a20.js" charset="utf-8"></script><div id="global-zeroclipboard-html-bridge" class="global-zeroclipboard-container" style="position: absolute; left: 0px; top: -9999px; width: 15px; height: 15px; z-index: 999999999;">      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" id="global-zeroclipboard-flash-bridge" width="100%" height="100%">         <param name="movie" value="http://s1.bdstatic.com/r/www/cache/mid/static/zeroclip/ZeroClipboard1.3.5.swf?noCache=1501125236898">         <param name="allowScriptAccess" value="always">         <param name="scale" value="exactfit">         <param name="loop" value="false">         <param name="menu" value="false">         <param name="quality" value="best">         <param name="bgcolor" value="#ffffff">         <param name="wmode" value="transparent">         <param name="flashvars" value="trustedOrigins=xueshu.baidu.com%2C%2F%2Fxueshu.baidu.com%2Chttp%3A%2F%2Fxueshu.baidu.com">         <embed src="http://s1.bdstatic.com/r/www/cache/mid/static/zeroclip/ZeroClipboard1.3.5.swf?noCache=1501125236898" loop="false" menu="false" quality="best" bgcolor="#ffffff" width="100%" height="100%" name="global-zeroclipboard-flash-bridge" allowscriptaccess="always" allowfullscreen="false" type="application/x-shockwave-flash" wmode="transparent" pluginspage="http://www.macromedia.com/go/getflashplayer" flashvars="trustedOrigins=xueshu.baidu.com%2C%2F%2Fxueshu.baidu.com%2Chttp%3A%2F%2Fxueshu.baidu.com" scale="exactfit">                </object></div><div id="sc_quote_bg"></div><div id="sc_quote_wr"><div class="sc_quote_top"><a href="javascript:;" class="sc_md_cls c-icon-close-hover"><i class="c-icon c-icon-close"></i></a><h3 class="sc_quote_title">引用</h3></div><div class="sc_quote_content"></div></div>

		<script src="http://s1.bdstatic.com/r/www/cache/mid/static/xueshu/js/stepGuide_6f576d8.js"></script>
</body></html>
           
"""

soup = bs(html_doc, "html.parser")
print(soup.prettify())
print(soup.title.string)
print(soup.p)
print(soup.find_all("a"))
for link in soup.find_all("a"):
    print(link.get_text())

date = soup.find_all("a",href = re.compile(r'^http://www\.baidu\.com/'))
print(date)