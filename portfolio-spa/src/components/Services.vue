<template>
  <section class="ftco-section" id="services-section">
    <div class="container">
      <div class="row justify-content-center py-5 mt-5">
        <div class="col-md-12 heading-section text-center" data-aos="fade-up" data-aos-duration="1000">
          <h1 class="big big-2">Services</h1>
          <h2 class="mb-4">Services</h2>
          <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia</p>
        </div>
      </div>
      <div class="row">
        <div v-for="(service, index) in services" :key="index" 
             class="col-md-4 text-center d-flex" 
             data-aos="fade-up" 
             :data-aos-delay="index * 100">
          <a href="#" class="services-1">
            <span class="icon">
              <i :class="service.icon"></i>
            </span>
            <div class="desc">
              <h3 class="mb-5">{{ service.title }}</h3>
            </div>
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const services = ref([
  { title: 'Web Design', icon: 'flaticon-analysis' },
  { title: 'Photography', icon: 'flaticon-flasks' },
  { title: 'Web Developer', icon: 'flaticon-ideas' },
  { title: 'App Developing', icon: 'flaticon-analysis' },
  { title: 'Branding', icon: 'flaticon-flasks' },
  { title: 'Product Strategy', icon: 'flaticon-ideas' }
]);
</script>
