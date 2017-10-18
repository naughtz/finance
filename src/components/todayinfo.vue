<template>
<div>
	<div id="todayInfo">
		<el-table
			:data="data.slice((currentPage-1)*pagesize,currentPage*pagesize)"
			stripe
			style="width: 100%">
			<el-table-column
				prop="id"
				label="序号"
				align="center">
			</el-table-column>
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
	<div class="pageturning">
		<el-pagination
			@size-change="handleSizeChange"
			@current-change="handleCurrentChange"
			:current-page="currentPage"
			:page-sizes="[10, 20, 50, 100]"
			:page-size="pagesize"
			layout="total, sizes, prev, pager, next, jumper"
			:total="data.length">
		</el-pagination>
	</div>
</div>
</template>

<script>
export default {
name: 'todayinfo',
data () {
	return {
		data: [],
		currentPage:1,
		pagesize:20,

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
	this.$http({
		method:'POST',
		url:'/ajax/todayInfo',
		}).then(function(response){
			this.data = response.body.result;

			
		})
},
methods: {
	handleSizeChange: function (size) {
		this.pagesize = size;
	},
	handleCurrentChange: function(currentPage){
		this.currentPage = currentPage;
	}
}

}
</script>

<style scoped>

</style>