<template>
  <section class="ftco-section" id="skills-section">
    <div class="container">
      <div class="row justify-content-center pb-5">
        <div class="col-md-12 heading-section text-center" data-aos="fade-up" data-aos-duration="1000">
          <h1 class="big big-2">Skills</h1>
          <h2 class="mb-4">My Skills</h2>
          <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia</p>
        </div>
      </div>
      <div class="row">
        <div v-for="(skill, index) in skills" :key="index" 
             class="col-md-6" 
             data-aos="fade-up" 
             :data-aos-delay="index * 50">
          <div class="progress-wrap">
            <h3>{{ skill.name }}</h3>
            <div class="progress">
              <div class="progress-bar" 
                   :class="'color-' + (index + 1)" 
                   role="progressbar" 
                   :aria-valuenow="skill.value"
                   aria-valuemin="0" 
                   aria-valuemax="100" 
                   :style="{ width: skill.value + '%' }">
                <span>{{ skill.value }}%</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const skills = ref([
  { name: 'Photoshop', value: 90 },
  { name: 'jQuery', value: 85 },
  { name: 'HTML5', value: 95 },
  { name: 'CSS3', value: 90 },
  { name: 'WordPress', value: 70 },
  { name: 'SEO', value: 80 }
]);
</script>
