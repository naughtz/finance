<template>
<div>
	<span></span>
	<div class="header">
		<el-menu :default-active="activeIndex" mode="horizontal" @select="handleSelect">
			<el-menu-item index="1">个人中心</el-menu-item>
			<el-menu-item index="2">A股概览</el-menu-item>
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
		activeIndex: 1,

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
	handleSelect: function (key) {
		if ( key == 1 ) {
			this.$router.push({path: '/finance/userinfo'});
		}
		else if ( key == 2 ) {
			this.$router.push({path: '/finance/todayinfo'});
		}
	},
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