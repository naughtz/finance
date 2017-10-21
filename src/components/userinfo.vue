<template>
<div style="text-align: left;">
	<p>用户名:&nbsp;&nbsp;&nbsp;{{user}}</p>
	<p>您的自选股:</p>
	<div style="width:500px">
		<el-input v-model="chadd" placeholder="需要添加的自选股代码">
			<template slot="prepend">添加自选股</template>
			<el-button slot="append" type="text" :disabled="false" @click="addch">添加</el-button>
		</el-input>
		<el-input v-model="chdel" placeholder="需要删除的自选股代码">
			<template slot="prepend">删除自选股</template>
			<el-button slot="append" type="text" :disabled="false" @click="delch">删除</el-button>
		</el-input>
		{{msg}}
	</div>
	<div>
		<el-table
			:data="data"
			stripe
			style="width: 100%">
			<el-table-column
				prop="code"
				label="代码"
				align="center">
			</el-table-column>
			<el-table-column
				prop="name"
				label="名称"
				align="center">
			</el-table-column>
			<el-table-column
				prop="changepercent"
				label="涨跌幅"
				align="center">
			</el-table-column>
			<el-table-column
				prop="trade"
				label="现价"
				align="center">
			</el-table-column>
			<el-table-column
				prop="open"
				label="开盘价"
				align="center">
			</el-table-column>
			<el-table-column
				prop="high"
				label="最高价"
				align="center">
			</el-table-column>
			<el-table-column
				prop="low"
				label="最低价"
				align="center">
			</el-table-column>
			<el-table-column
				prop="settlement"
				label="昨日收盘价"
				align="center">
			</el-table-column>
			<el-table-column
				prop="volume"
				label="成交量"
				align="center">
			</el-table-column>
			<el-table-column
				prop="turnoverratio"
				label="换手率"
				align="center">
			</el-table-column>
			<el-table-column
				prop="amount"
				label="成交量"
				align="center">
			</el-table-column>
			<el-table-column
				prop="per"
				label="市盈率"
				align="center">
			</el-table-column>
			<el-table-column
				prop="pb"
				label="市净率"
				align="center">
			</el-table-column>
			<el-table-column
				prop="mktcap"
				label="总市值"
				align="center">
			</el-table-column>
			<el-table-column
				prop="nmc"
				label="流通市值"
				align="center">
			</el-table-column>
		</el-table>
	</div>

</div>
</template>

<script>
export default {
name: 'finance',
data () {
	return {
		user: '',
		choose: '',
		data: '',
		chadd: '',
		chdel: '',
		msg: '',
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
mounted: function () {
	this.user = this.$route.query.user;
	this.$http({
		method:'POST',
		url:'/ajax/userdata',
		params: {
				user:this.user,
			}
		}).then(function(response){
			if (response.body.state=="true") {
				this.choose = response.body.choose
				this.data = response.body.data
			}
			else {
				
			}
		})
},
methods: {
	addch: function () {
		this.$http({
			method:'POST',
			url:'/ajax/changech',
			params: {
				user:this.user,
				chadd:this.chadd,
				chdel:this.chdel,
				type:'add',
				choose: this.choose,
			}
		}).then(function(response){
			if(response.body.state=="true"){
				this.msg = "修改成功！请刷新页面查看。"
			}
			else{
				this.msg = "修改失败！"
			}
		})
	},
	delch: function () {
		this.$http({
			method:'POST',
			url:'/ajax/changech',
			params: {
				user:this.user,
				chadd:this.chadd,
				chdel:this.chdel,
				type:'del',
				choose: this.choose,
			}
		}).then(function(response){
			if(response.body.state=="true"){
				this.msg = "修改成功！请刷新页面查看。"
			}
			else{
				this.msg = "修改失败！"
			}
		})
	}
}



}

</script>