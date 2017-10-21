<template>
<div>
<center>
<div class="con">
	<div class="con_title">
		<h2>欢迎注册系统</h2>
	</div>
	<div class="register_form">
		<el-form label-width="70px" input-width="50px">
			<el-form-item label="用户名">
			<el-input type="text" placeholder="用户名" id="user" v-model="user"/>
			</el-form-item>
			<el-form-item label="密码">
			<el-input type="text" placeholder="密码" id="passwd" v-model="passwd" type="password"/>
			</el-form-item>
			<el-form-item label="确认密码">
			<el-input type="text" placeholder="确认密码" id="passwd2" v-model="passwd2" type="password"/>
			</el-form-item>
			<el-form-item>
			<el-button type="primary" @click="register">提交</el-button>
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
  name: 'register',
  data () {
    return {
    	user: '',
    	passwd: '',
    	passwd2: '',
    	message: '',
    }
  },
methods: {
	register: function () {
		if(this.passwd!=this.passwd2){
			this.message="密码不一致！"
		}
		else{
			this.$http({
				method:'POST',
				url:'/ajax/register',
				params: {
					user:this.user,
					passwd:this.passwd
				}
			}).then(function(response){
				if (response.body.state=="0") {
					this.$router.push({path: '/login'});
				}
				else if(response.body.state=="1"){
					this.message = "该用户名已存在";
				}
			})
		}
	},
  }
}
</script>
<style scoped>
	.con{
		margin: 50 auto;
		width: 500px;
	}
	.register_form{
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