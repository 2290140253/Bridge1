<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import { onMounted } from 'vue';
import { useUserStore } from '@/store/user';
import axios from '@/api/axios';
import router from '@/router';
import Swal from 'sweetalert2';

export default {
  name: 'App',
  setup() {
    const userStore = useUserStore(); 

    onMounted(() => {
      const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
      const currentPath = router.currentRoute.value.path;

      if (!isLoggedIn && currentPath !== '/login') {
        router.push('/login');
      } else if (isLoggedIn) {
        userStore.setUserInfo(JSON.parse(localStorage.getItem('userInfo'))); 
      }
    });

    
    // 拦截所有axios请求，检查响应状态码
    axios.interceptors.response.use(
      response => response,
      error => {
        if (error.response && error.response.status === 403) {
          // 如果接收到403状态码，自动注销用户并跳转到登录页面
          Swal.fire({
            title: '登录状态过期',
            text: '当前登录状态已过期，请重新登录',
            icon: 'warning',
            confirmButtonText: '确定'
          }).then(() => {
            localStorage.removeItem('isLoggedIn');
            localStorage.removeItem('userInfo');
            router.push('/login');
          });
        }
        return Promise.reject(error);
      }
    );
  },  
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>