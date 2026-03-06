<template>
  <section class="ftco-section ftco-no-pb" id="resume-section">
    <div class="container">
      <div class="row justify-content-center pb-5">
        <div class="col-md-10 heading-section text-center" 
             data-aos="fade-up" 
             data-aos-duration="1000">
          <h1 class="big big-2">Resume</h1>
          <h2 class="mb-4">Resume</h2>
          <p>A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth.</p>
        </div>
      </div>
      <div class="row">
        <div class="col-md-6">
          <div v-for="(item, index) in resumeLeft" :key="index" 
               class="resume-wrap" 
               data-aos="fade-up" 
               :data-aos-delay="index * 100">
            <span class="date">{{ item.date }}</span>
            <h2>{{ item.title }}</h2>
            <span class="position">{{ item.position }}</span>
            <p class="mt-4">{{ item.description }}</p>
          </div>
        </div>

        <div class="col-md-6">
          <div v-for="(item, index) in resumeRight" :key="index" 
               class="resume-wrap" 
               data-aos="fade-up" 
               :data-aos-delay="index * 100">
            <span class="date">{{ item.date }}</span>
            <h2>{{ item.title }}</h2>
            <span class="position">{{ item.position }}</span>
            <p class="mt-4">{{ item.description }}</p>
          </div>
        </div>
      </div>
      <div class="row justify-content-center mt-5">
        <div class="col-md-6 text-center" data-aos="fade-up">
          <p><a href="#" class="btn btn-primary py-4 px-5">Download CV</a></p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const resumeLeft = ref([
  { date: '2014-2015', title: 'Master Degree of Design', position: 'Cambridge University', description: 'A small river named Duden flows by their place and supplies it with the necessary regelialia.' },
  { date: '2014-2015', title: "Bachelor's Degree of C.A", position: 'Cambridge University', description: 'A small river named Duden flows by their place and supplies it with the necessary regelialia.' },
  { date: '2014-2015', title: 'Diploma in Computer', position: 'Cambridge University', description: 'A small river named Duden flows by their place and supplies it with the necessary regelialia.' }
]);

const resumeRight = ref([
  { date: '2014-2015', title: 'Art & Creative Director', position: 'Cambridge University', description: 'A small river named Duden flows by their place and supplies it with the necessary regelialia.' },
  { date: '2014-2015', title: 'Wordpress Developer', position: 'Cambridge University', description: 'A small river named Duden flows by their place and supplies it with the necessary regelialia.' },
  { date: '2017-2018', title: 'UI/UX Designer', position: 'Cambridge University', description: 'A small river named Duden flows by their place and supplies it with the necessary regelialia.' }
]);
</script>
