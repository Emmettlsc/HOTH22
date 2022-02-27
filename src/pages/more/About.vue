<template>
  <div class="about-page">
    <div class="about-header">
      About us
      <div class="header-text">
        We're reimagining the future of education
      </div>
    </div>
    <div class="about-flexer">
    <img class="about-pic" src="@/assets/aboutus.jpg">
    <div class="center-width">
      <div class="pane">
        <div class="pane-text">
          Our Mission
        </div>
        <div class="info-text">
          We believe that anyone with a passion should have the tools they need to succeed.
          <br><br>
          Our goal is to equalize the playing field, to have first-generation and underrepresented college students have the same information and advantages as those that are priviliged to have
          top notch connections and guidance throughout their life.
          <br><br>
          With course connect, our vision is a future in which anyone can navigate the complexities of college class selection, at UCLA and beyond.
        </div>
      </div>
    </div>
    </div>
  </div>
</template>

<style scoped>
  .about-page{
    padding: 100px 24px;
  }
  .center-page{
    width: auto;
  }
  .about-header{
    max-width: 1120px;
    margin: 0 auto;
    text-align: left;
    font-size: 40px;
  }
  .header-text{
    font-size: 56px;
    margin-top: 80px;
    max-width: 730px;
    text-align: left;
    font-weight: 600;
  }
  .about-pic{
    width: 50%;
    height: 50vw;
    margin-top: 120px;
    margin-right: 40px;
  }
  .center-width{
    max-width: 1120px;
    margin: 0 auto;
  }
  .pane{
    padding: 200px 0 60px 0;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
  }
  .pane-text{
    font-size: 24px;
    font-weight: 600;
    text-align: left;
    margin-bottom: 10px;
  }
  .info-text{
    font-size: 16px;
    color: var(--light-gray);
    width: 50%;
    text-align: left;
    line-height: 32px;
    transition: .3s all;
  }
  @media screen and (max-width: 1280px) {
    .about-header{
      max-width: 960px;
    }
    .header-text{
      font-size: 40px;
      max-width: 680px;
    }
    .center-width{
      max-width: 960px;
    }
    .pane{
      flex-direction: column;
    }
    .info-text{
      width: auto;
      line-height: 26px;
      font-size: 14px;
    }
  }
  @media screen and (max-width: 767px) {
    .about-page{
      padding: 60px 24px;
    }
    .about-header, .header-text{
      font-size: 32px;
    }
    .about-pic{
      margin-top: 80px;
    }
    .pane{
      padding: 60px 0;
    }
  }
  .about-flexer{
    display: flex;
  }
  .info-text:hover{
    color: black;
  }
</style>