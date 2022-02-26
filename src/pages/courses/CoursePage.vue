<template>
<div class="coursepage">
  <div class="header">
    Course Planner
  </div>

  <!--COURSES TAKEN-->
  <div class="courses-list-button" @click="coursesOpen = !coursesOpen">
    <i class="fas fa-angle-down" :style="!coursesOpen ? 'transform: rotate(270deg)' : ''"/> 
    Courses Taken 
  </div>
  <div class="courses-lists" :style="!coursesOpen ? 'max-height: 0px' : 'max-height: 400px'">
    <div class="taken-courses-wrapper">

      <span class="course-list-header">Taken Courses</span>
      <div class="course-list-overflow">
        <TransitionGroup name="taken-fade">
        <div v-for="(course,ind) in studentCourses" class="taken-course" :key="course">
          <span class="taken-course-name">
            <span class="taken-course-ind">{{(ind+1) + ')'}}</span>
            {{course}}
          </span>
          <span class="remove-taken-course" @click="removeTakenCourse(course)">X</span>
        </div>
        </TransitionGroup>
      </div>
    </div>
    <div class = "all-courses-wrapper">
      <span class="course-list-header">All courses</span>
      <div class="course-list-overflow">
        <TransitionGroup name="all-fade">
        <div v-for="course in allCourses" class="taken-course" :key="course">
          <span class="taken-course-name">{{course}}</span>
          <span class="add-taken-course" @click="addTakenCourse(course)">+</span>
        </div>
        </TransitionGroup>
      </div>
    </div>
  </div>


  <!--CLASS PREFERENCES-->
  <div class="courses-list-button" @click="preferencesOpen = !preferencesOpen">
    <i class="fas fa-angle-down" :style="preferencesOpen ? 'transform: rotate(270deg)' : ''"/> 
    Class Preferences
  </div>
  <div class="courses-lists" :style="preferencesOpen ? 'max-height: 0px' : 'max-height: 400px'">
    <div class="course-list-header">
      Time Restrictions
    </div>
    <div class="course-list-header">
      Optimization 
    </div>
  </div>


  <div class="generate-region">
    <button class="generate-button"> Generate Class Recomendations </button>
  </div>
</div>
</template>

<script>
export default {

  data(){
    return{
      coursesOpen: true,
      preferencesOpen: false,

      studentCourses: [],
      allCourses: [],
    }
  },

  mounted(){
    /*fetch('/api/courses')
    .then(res => res.json())
    .then(data =>{
      this.allCourses = data;
    })*/
    for(let i = 1; i < 20; i++){
      this.allCourses.push('CS ' + (30 + i));
    }
  },

  methods:{

    addTakenCourse(c){
      this.studentCourses.push(c);
      this.allCourses = this.allCourses.filter(item => item !== c);
    },

    removeTakenCourse(c){
      this.studentCourses = this.studentCourses.filter(item => item !== c);
      this.allCourses.push(c);
    }
  }
}
</script>

<style scoped>
.coursepage{
  padding: 100px 35px;
}
.courses-list-button{
  text-align: left;
  font-size: 20px;
  font-weight: 800;
  background: #bbbbbb;
  padding: 5px;
  cursor: pointer;
}
.courses-lists{
  display: flex;
  flex-direction:row;
  justify-content: space-evenly;
  transition: 1s ease all;
  overflow-y: clip;
  margin: 30px 0;
}
.taken-course{
  display: flex;
  justify-content: space-between;
  user-select: none;
  align-items: center;
  border: 1px solid gray;
  width: 150px;
}
.remove-taken-course, 
.add-taken-course{
  border-left: 1px solid gray;
  color: black;
  background: white;
  padding: 10px;
  border-radius: 1px;
  cursor: pointer;
}
.remove-taken-course:hover,
.add-taken-course:hover{
  background: #e0e0e0;
}
.taken-course-name{
  padding: 5px;
}
.course-list-header{
  font-size: 24px;
}
.course-list-overflow{
  overflow-y: scroll;
  overflow-x: clip;
  max-height: 290px;
  margin-top: 10px;
  padding: 0 15px;
}
.taken-course-ind{
  font-size: 12px;
  margin-right: 5px;
  color: #333333;
}

.all-fade-move,
.all-fade-enter-active,
.all-fade-leave-active,
.taken-fade-move,
.taken-fade-enter-active,
.taken-fade-leave-active {
  transition: all .5s ease;
}
.all-fade-enter-from,
.all-fade-leave-to {
  opacity: 0;
  transform: translateX(-100px);
}
.taken-fade-enter-from,
.taken-fade-leave-to {
  opacity: 0;
  transform: translateX(100px);
}
.all-fade-leave-active,
.taken-fade-leave-active {
  position: absolute;
}

.generate-region{
  margin-top: 80px;
}
.generate-button{
  border: none;
  padding: 10px;
  color: white;
  background: var(--primary-color);
}

.fa-angle-down{
  transition: .5s all;
}
</style>