import Vue from 'vue'
import Router from 'vue-router'
import login from '@/components/login'
import finance from '@/components/finance'
import userinfo from '@/components/userinfo'
import todayinfo from '@/components/todayinfo'
import kline from '@/components/kline'
import register from '@/components/register'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect:'/finance',
    },
    {
      path: '/register',
      name: 'register',
      component: register,
    },
    {
      path: '/finance',
      name: 'finance',
      component: finance,
      children: [
      {
        path: 'userinfo',
        name: 'userinfo',
        component: userinfo,
      },
      {
        path: 'todayinfo',
        name: 'todayinfo',
        component: todayinfo,
      },
      {
        path: 'kline',
        name: 'kline',
        component: kline,
      }
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: login,
    }
  ]
})
