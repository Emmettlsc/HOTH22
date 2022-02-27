<template>
<div class="faq-page">
  <div class="header">
    Frequently Asked Questions
  </div>
  <div v-for="(faq, ind) in faqs" :key="faq.question">
    <div class="faq-open-button" @click="toggleFaq(ind)">
      <i class="fas fa-angle-down" :style="openFaqs.indexOf(ind) == -1 ? 'transform: rotate(270deg)' : ''"/> 
      {{faq.q}}
    </div>
    <div class="faq-a" :style="openFaqs.indexOf(ind) == -1 ? 'max-height: 0px' : 'max-height: 50px; margin-top: 20px; margin-bottom: 20px'">
      {{faq.a}}
    </div>
  </div>
</div>
</template>

<script>
export default {
  data(){
    return{
      openFaqs: [],
      faqs:[
        {q: 'What steps does course connect do to ensure user privacy concerns?',
         a: 'Our platform does not store any user information. We do not share or sell any data, nor do we allow any of our developers to tamper with these rules.'},

        {q: 'Who is course connect made for?',
        a: 'Course connect currently is for all UCLA Computer Science students, but we hope we can soon extend the platform to include all UCLA students},

        {q: '',
        a: 'This is answer 3'},

        {q: 'This is Question 4',
        a: 'This is answer 4'},

        {q: 'Is course connect free?',
        a: 'Yes'}
      ]
    }
  },
  methods:{
    toggleFaq(ind){
      if(this.openFaqs.indexOf(ind) !== -1)
        this.openFaqs = this.openFaqs.filter(i => i != ind);
      else
        this.openFaqs.push(ind);
    }
  }
}
</script>

<style scoped>
.faq-page{
  padding: 100px 35px;
}
.header{
  font-size: 24px;
  font-weight: 800;
  margin-bottom: 40px;
  text-align: left;
}
.faq-open-button{
  text-align: left;
  font-size: 20px;
  font-weight: 600;
  background: #dddddd;
  padding: 15px 10px;
  cursor: pointer;
  background: white;
  color: var(--primary-light);
  border: 1px solid gray;
  margin-top: -1px;
}
.fa-angle-down{
  transition: .5s all;
}
.faq-a{
  text-align: left;
  overflow-y: clip;
  transition: .5s ease all;
  margin-left: 25px;
}
</style>