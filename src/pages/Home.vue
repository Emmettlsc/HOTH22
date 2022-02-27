<template>
<div class="homepage">
  <div class="homepage-header">
    <span>
      Your personal counselor in the digital age
    </span>
    <img src="@/assets/CChome.jpg"/>
  </div>

  <div class="triple-icon">
    <div class="iconbox" v-infocus="'show-element'">
      <i class="fas fa-clipboard-list"></i>
      <br>
      <span>Ready</span>
      <p>Add all of the past classes you've taken from a list. We use this to determine which courses would work best for you</p>
    </div>
    <div class="iconbox" v-infocus="'show-element2'">
      <i class="fas fa-sliders-h"></i>
      <br>
      <span>Set</span>
      <p>Choose your class preferences to personalize your experience and receive more accurate suggestions</p>
    </div>
    <div class="iconbox" v-infocus="'show-element3'">
      <i class="fas fa-graduation-cap"></i>
      <br>
      <span>Go</span>
      <p>Our algorithm combines all of the class data, reviews, preferences, pre-reqs, timings, and options so you don't have to</p>
    </div>
  </div>
  <div class="privacy-pane">
    <span v-infocus="'show-element'">
      Privacy, built in
      <p>We believe privacy should be a basic right on the internet, which is why our site never collects user data</p>
      <p class="learn-more" @click="$router.push('/faq')">Learn More</p>
    </span>
    <i class="fas fa-user-secret" ></i>
  </div>
  <div class="privacy-pane" style="background: #eef7ff">
    <i class="fas fa-school" style="opacity: 1"></i>
    <span v-infocus="'show-element'">
      Our mission
      <p>Is to give every student an equal opportunity to succeed in school</p>
      <p class="learn-more" @click="$router.push('/about')">Learn More</p>
    </span>
  </div>

</div>
</template>

<script>
export default {
  directives: {
    infocus: {
      isLiteral: true,
      mounted: (el, binding) => {
        let f = () => {
          el.classList.add('hidden-low');
          let rect = el.getBoundingClientRect()
          let inView = (
            rect.width > 0 &&
            rect.height > 0 &&
            rect.top >= 0 &&
            (rect.top + 100) <= (window.innerHeight || document.documentElement.clientHeight)
          )
          if (inView) {
            el.classList.add(binding.value)
            window.removeEventListener('scroll', f)
          }
        }
        window.addEventListener('scroll', f)
        f()
      }
    }
  }
}
</script>

<style scoped>
.homepage{
  padding: 130px 0;
}
.homepage-header{
  display: flex;
}
.homepage-header span{
  font-size: 3.5em;
  line-height: 1.2;
  font-weight: 800;
  color: #0f1f36;;
  width: 50vw;
  text-align: left;
  margin-left: 30px;
  font-family: 'Inter - Self Hosted',Arial,sans-serif;
}
.homepage-header img{
  width: 40vw;
  height: 40vw;
  margin: 0 auto;
  margin-bottom: 60px;
}
.triple-icon{
  display: flex;
  justify-content: space-evenly;
  gap: 30px;
  padding: 90px 20px;
  margin: 20px 0;
  background: #e8e8e8;
}
.iconbox{
  font-size: 16px;
  color: #606060;
  width: 33vw;
  max-width: 300px;
}
.iconbox span{
  color: #4e4e4e;
  font-size: 26px;
  font-weight: 800;
}
.iconbox i{
  font-size: 60px;
  color: var(--primary-color);
}
.get-started-button{
  background: var(--primary-color);
  color: white;
  padding: 5px 10px;
  font-size: 18px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
}
.get-started-button:hover{
  background: var(--primary-light);
}
.privacy-pane{
  padding: 60px 20px;
  display: flex;
  justify-content: space-evenly;
  gap: 30px;
  font-size: 30px;
}
.privacy-pane span{
  width: 40vw;
  font-weight: 800;
  text-align: left;
}
.privacy-pane p{
  font-size: 18px;
  font-weight: 200;
}
.privacy-pane i{
  font-size: 200px;
  transition: .5s all;
}
.privacy-pane:hover > i{
  opacity: .1;
}
.learn-more{
  color: blue;
  text-decoration: underline;
  cursor: pointer;
}


.hidden-low {
  opacity: 0;
  transform: translate(0, 100px);
}
.show-element {
  opacity: 1;
  transform: translate(0, 0);
  -webkit-transition: all 0.5s ease-out;
  -moz-transition: all 0.5s ease-out;
  transition: all 0.5s ease-out;
}
.show-element2 {
  opacity: 1;
  transform: translate(0, 0);
  -webkit-transition: all 0.5s .2s ease-out;
  -moz-transition: all 0.5s .2s ease-out;
  transition: all 0.5s .2s ease-out;
}
.show-element3 {
  opacity: 1;
  transform: translate(0, 0);
  -webkit-transition: all 0.5s .4s ease-out;
  -moz-transition: all 0.5s .4s ease-out;
  transition: all 0.5s .4s ease-out;
}
</style>