var Timer = (function(){
	var interval;
	function reset(){
		sessionStorage.setItem('timer_station', 600);
		this.start();
	}
	function pause(){
		window.clearInterval(interval);
	}
	function start() {
		if(interval!='undefined'){
			this.pause();
			interval='undefined'
		}
		timer = sessionStorage.getItem('timer_station');
		if(timer!=null&&timer>0){
			interval = window.setInterval(function () {
			    timer--;
			    sessionStorage.setItem('timer_station', timer);
			    if (timer === 0) {
			    	sessionStorage.removeItem("timer_station");
		    		initSurvey();
			    }
			}, 1000);
		}
	}
	return {
		'start':start,
		'pause':pause,
		'reset':reset
	}
})();
