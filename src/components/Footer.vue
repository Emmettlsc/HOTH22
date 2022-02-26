<template>
  <div class="footer">
      <router-link to="/" class="logo-white mobile-hide">
        course connect
      </router-link>
    <div class="column">
      <div class="col-header">
        Product
      </div>
      <router-link to="/" class="item">
        Home
      </router-link>
      <router-link to="/partner" class="item">
        Partner
      </router-link>
      <router-link to="/signup" class="item">
        Sign up
      </router-link>
    </div>
    <div class="column">
      <div class="col-header">
        Company
      </div>
      <router-link to="/about" class="item">
        About
      </router-link>
      <router-link to="/Contact" class="item">
        Contact
      </router-link>
    </div>
    <div class="column">
      <div class="col-header">
        More
      </div>
      <router-link to="/login" class="item">
        Login
      </router-link>
      <router-link to="/Contact" class="item">
        Questions
      </router-link>
    </div>
  </div>
  <router-link to="/" class="logo-white mobile-logo">
        course connect
  </router-link>
</template>

<style scoped>
  .footer{
    background: var(--light-black);
    display: flex;
    justify-content: space-evenly;
    padding: 160px 34px;
    width: calc(100% - 68px);
    z-index:10;
    overflow: auto;
  }
  .logo-white{
    color: white;
    font-size: 40px;
    text-decoration: none;
    margin-top: -28px;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  }
  .logo-white:hover{
    color: var(--primary-color);
  }
  .column{
    display: flex;
    flex-direction: column;
    text-align: center;
  }
  .col-header{
    color: white;
  }
  .item{
    color: var(--light-gray);
    text-decoration: none;
    margin-top: 40px;
  }
  .item:hover{
    color: var(--primary-color);
  }
  .mobile-logo{
    display: none;
  }
  @media screen and (max-width: 600px){
    .mobile-logo{
      display: block;
      margin-top: -50px;
    }
  }
</style>