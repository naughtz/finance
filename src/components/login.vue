<template>
<div>
<center>
<div class="con">
	<div class="con_title">
		<h2>欢迎登录系统</h2>
	</div>
	<div class="login_form">
		<el-form label-width="70px" input-width="50px">
			<el-form-item label="用户名">
			<el-input type="text" placeholder="用户名" id="user" v-model="user"/>
			</el-form-item>
			<el-form-item label="密码">
			<el-input type="text" placeholder="密码" id="passwd" v-model="passwd" type="password"/>
			</el-form-item>
			<el-form-item>
			<el-button type="primary" @click="login">登录</el-button>
			<p class="message">{{message}}</p>
			</el-form-item>
		</el-form>
	</div>
</div>
</center>
</div>
</template>

<script>
export default {
  name: 'login',
  data () {
    return {
    	user: '',
    	passwd: '',
    	message: '',
    }
  },
created: function () {
	this.$http({
		method:'POST',
		url:'/ajax/ifLogin',
		}).then(function(response){
			if (response.body.state=="true") {
				this.$router.push({path: '/'});
			}
		})
	},
methods: {
	login: function () {
		this.$http({
			method:'POST',
			url:'/ajax/login',
			params: {
				user:this.user,
				passwd:this.passwd
			}
		}).then(function(response){
			if (response.body.state=="true") {
				this.$router.push({path: '/'});
			}
			else {
				this.message = "用户名或密码错误";
			}
		})
	}
  }
}
</script>
<style scoped>
	.con{
		margin: 50 auto;
		width: 500px;
	}
	.login_form{
		margin: 0 auto;
		padding: 20px 20px;
		border: 1px solid #272727;
		height: 200px;
	}
	.message{
		font-size: 16px;
    	color: #FF0000;
    	text-align: right;
	}
</style>