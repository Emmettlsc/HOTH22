<template>
  <div class="navbar" id="navbar-border" >
    <router-link to="/" class="logo-black">
      course connect
    </router-link>
    <div class="navigation medium-hide" id="desktop-navigation-links">
      <router-link to="/about" class="navbar-link">
        About
      </router-link>
      <router-link to="/partner" class="navbar-link">
        Partner
      </router-link>
      <router-link to="/courses" class="navbar-link-signup">
        Course Planner
      </router-link>
    </div>
    <div class="navigation-drop medium-show">
      <i class="fas fa-bars" @click="menuOpen = !menuOpen"></i>
      <div class="menu-drop" :style="menuOpen ? 'height: 340px' : 'height: 0px; box-shadow: none; padding-top: 0;'">
        <router-link to="/about" class="navbar-link limit-width" @click="menuOpen = false">
          About
        </router-link>
        <router-link to="/contact" class="navbar-link limit-width" @click="menuOpen = false">
          Contact
        </router-link>
        <router-link to="/partner" class="navbar-link limit-width" @click="menuOpen = false">
          Partner
        </router-link>
        <router-link to="/login" class="navbar-link limit-width" @click="menuOpen = false">
          Login
        </router-link>
        <router-link to="/courses" class="navbar-link limit-width" @click="menuOpen = false">
          Course Planner
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return{
      menuOpen: false,
    }
  }
}
</script>

<style scoped>
  .navbar{
    height: var(--navbar-height);
    background: white;
    display: flex;
    /*box-shadow: 0 0 18px rgb(0 0 0 / 10%);*/
    align-items: center;
    justify-content: space-between;
    padding: 0 34px;
    position: fixed;
    width: calc(100% - 68px);
    z-index:10;
    border-bottom: 1px solid #e5e5e5;
    transition: all 1s;
    overflow: visible;
  }
  .logo {
    height: 25px;
  }
  .logo-black{
    color: black;
    font-size: 28px;
    text-decoration: none;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  }
  .logo-black:hover{
    color: var(--primary-color);
  }
  .navbar-link{
    padding: 25px 35px;
    color: var(--light-gray);
    text-decoration: none;
  }
  .navbar-link:hover{
    color: #006aff;
  }
  .navbar-link-signup{
    padding: 10px 25px;
    margin-left: 20px;
    text-decoration: none;
    transition: .3s all;
    border-radius: 30px;
    color: white;
    background-color: var(--primary-color);
  }
  .navbar-link-signup:hover{
    background-color: var(--primary-light);
  }
  .navigation-drop{
    display: none;
  }
  .fa-bars{
    cursor: pointer;
    font-size: 24px;
  }
  .menu-drop{
    display: flex;
    flex-direction: column;
    position: absolute;
    z-index: 999;
    overflow: hidden;
    width: 100%;
    left: 0;
    text-align: left;
    transition: .5s all;
    background: white;
    box-shadow: 0px 10px 10px var(--lightest-gray);
    padding-top: 25px;
}
  .limit-width{
    width: fit-content;
  }
  @media screen and (max-width: 900px) {
    .medium-hide{
      display: none;
    }
    .medium-show{
      display: block;
    }
  }
</style>