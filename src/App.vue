<template>
  <Navbar />
  <router-view />
  <Footer />
</template>

<script>
import Navbar from './components/Navbar.vue';
import Footer from './components/Footer.vue';

export default {
  name: 'App',
  components: {
    Navbar,
    Footer
  },
  created() {
    this.$router.beforeEach((to, from, next) => {
      //console.log(to);
      //console.log(from);
      //useful info here
      document.body.scrollTop = document.documentElement.scrollTop = 0;
      next();
    });
  }
}
</script>

<style>
:root {
  --primary-color: #4285F4;
  --primary-light: #5C9FFF; 
  --white-gray: #F0F2F4;
  --lightest-gray: #D0D0D0;
  --light-gray: #777777;
  --dark-gray: #3a3d4a;
  --dark-gray-two: #2e2e2e;
  --light-black: #171717;
  --navbar-height: 60px;
  --mobile-width: 600px;
  --medium-width: 1200px;
}
#app {
  font-family: 'Open Sans', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;;
}
html, body{
  margin: 0;
}

@media screen and (max-width: 600px){
  .mobile-hide{
    display: none;
  }
}
.header{
  font-size: 40px;
  font-weight: 700;
  margin-bottom: 16px;
}
</style>
