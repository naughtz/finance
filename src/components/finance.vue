<template>
<div>
	<div style="text-align: left;"><span>欢迎您，{{user}}</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<el-button type="text" @click="logout()">注销</el-button></div>
	<div class="header">
		<el-menu :default-active="activeIndex" mode="horizontal" @select="handleSelect">
			<el-menu-item index="1">个人中心</el-menu-item>
			<el-menu-item index="2">A股概览</el-menu-item>
			<el-menu-item index="3">查看K线图</el-menu-item>
		</el-menu>
	</div>
	<div class="main">
		<router-view></router-view>
	</div>
</div>
</template>

<script>
export default {
name: 'finance',
data () {
	return {
		user: '',
		activeIndex: 1,

    }
},
created: function () {
	this.$http({
		method:'POST',
		url:'/ajax/ifLogin',
		}).then(function(response){
			if (response.body.state=="true") {
				this.user = response.body.user;
			}
			else {
				this.$router.push({path: '/login'});
			}
		})
},
methods: {
	handleSelect: function (key) {
		if ( key == 1 ) {
			this.$router.push({path: '/finance/userinfo',query: {"user": this.user}});
		}
		else if ( key == 2 ) {
			this.$router.push({path: '/finance/todayinfo'});
		}
		else if ( key == 3 ) {
			this.$router.push({path: '/finance/kline'});
		}
	},
	logout: function () {
		this.$http({
		method:'POST',
		url:'/ajax/logout',
		params: {
				user:this.user,
			}
		}).then(function(response){
			if (response.body.result=="true") {
				this.$router.push({path: '/login'});
			}
			else {
				
			}
		})
	}
}


}

</script>

<style scoped>
.header{
	height:80px;
}
.main{
	height:1000px;
	width:100%;
}
</style>