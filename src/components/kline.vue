<template>
<div>
	<div style="width:500px">
		<el-input v-model="code" placeholder="需要查看K线图的股票代码">
			<template slot="prepend">查看K线图</template>
			<el-button slot="append" type="text" :disabled="false" @click="getkline">查看</el-button>
		</el-input>
		{{msg}}
	</div>
	<div id="charts" style="width:1500px;height:600px">

	</div>
</div>
</template>

<script>
export default {
name: 'kline',
data () {
	return {
		code: '',
		msg: '',
		data: '',
		index: [],
    }
},
created: function () {
	this.$http({
		method:'POST',
		url:'/ajax/ifLogin',
		}).then(function(response){
			if (response.body.state=="true") {
				
			}
			else {
				this.$router.push({path: '/login'});
			}
		})
},
methods: {
	getkline: function () {
		this.$http({
		method:'POST',
		url:'/ajax/kline',
		params: {
				code:this.code,
			}
		}).then(function(response){
			if (response.body.state=="true") {
				this.index = response.body.index
				this.data = response.body.data
				let echart=this.$echarts.init(document.getElementById('charts'))
        		echart.setOption(options) 
			}
			else {
				this.msg="无法查看！"
			}
		})
		var options = {
    		title : {
        	text: this.code+'日线图'
    		},
    	tooltip : {
        	trigger: 'axis',
        	formatter: function (params) {
            	var res = params[0].seriesName + ' ' + params[0].name;
            	res += '<br/>  开盘 : ' + params[0].value[0] + '  最高 : ' + params[0].value[3];
            	res += '<br/>  收盘 : ' + params[0].value[1] + '  最低 : ' + params[0].value[2];
            	return res;
        	}
    		},
    		legend: {
        		data:['上证指数']
    		},
    		toolbox: {
        		show : true,
        		feature : {
         		mark : {show: true},
         	   	dataZoom : {show: true},
            	dataView : {show: true, readOnly: false},
            	magicType: {show: true, type: ['line', 'bar']},
            	restore : {show: true},
            	saveAsImage : {show: true}
        	}
    		},
    		dataZoom : {
        		show : true,
        		realtime: true,
        		start : 50,
        		end : 100
    		},
    		xAxis : [
        		{
            		type : 'category',
            		boundaryGap : true,
            		axisTick: {onGap:false},
            		splitLine: {show:false},
            		data : this.index
        		}
    			],
    		yAxis : [
       	 		{
            		type : 'value',
            		scale:true,
            		boundaryGap: [0.01, 0.01]
        		}
    			],
    		series : [
        		{
            		name:'上证指数',
            		type:'k',
            		data:this.data    
        		}
    			]
		};
		
	}
}

}
</script>

<style scoped>

</style>