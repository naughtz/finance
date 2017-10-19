<template>
<div style="text-align: left;">

</div>
</template>

<script>
export default {
name: 'finance',
data () {
	return {
		user: '',
    }
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
				console.log(response.body.result)
			}
			else {
				
			}
		})
},
}

</script>