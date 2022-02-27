<template>
<div class="faq-page">
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
         a: 'Our platform does not store any user information.'},

        {q: 'This is Question 2',
        a: 'This is answer 2'},

        {q: 'This is Question 3',
        a: 'This is answer 3'},

        {q: 'This is Question 4',
        a: 'This is answer 4'},

        {q: 'This is Question 5',
        a: 'This is answer 5'}
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