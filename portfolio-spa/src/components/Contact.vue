<template>
  <section class="ftco-section contact-section ftco-no-pb" id="contact-section">
    <div class="container">
      <div class="row justify-content-center mb-5 pb-3">
        <div class="col-md-7 heading-section text-center" data-aos="fade-up" data-aos-duration="1000">
          <h1 class="big big-2">Contact</h1>
          <h2 class="mb-4">Contact Me</h2>
          <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia</p>
        </div>
      </div>

      <div class="row d-flex contact-info mb-5">
        <div v-for="(info, index) in contactInfo" :key="index" 
             class="col-md-6 col-lg-3 d-flex" 
             data-aos="fade-up" 
             :data-aos-delay="index * 100">
          <div class="align-self-stretch box p-4 text-center">
            <div class="icon d-flex align-items-center justify-content-center">
              <span :class="info.icon"></span>
            </div>
            <h3 class="mb-4">{{ info.label }}</h3>
            <p v-if="info.link"><a :href="info.link">{{ info.value }}</a></p>
            <p v-else>{{ info.value }}</p>
          </div>
        </div>
      </div>

      <div class="row no-gutters block-9">
        <div class="col-md-6 order-md-last d-flex" data-aos="fade-up" data-aos-delay="200">
          <form @submit.prevent="handleSubmit" class="bg-light p-4 p-md-5 contact-form">
            <div class="form-group">
              <input type="text" class="form-control" placeholder="Your Name" v-model="form.name">
            </div>
            <div class="form-group">
              <input type="text" class="form-control" placeholder="Your Email" v-model="form.email">
            </div>
            <div class="form-group">
              <input type="text" class="form-control" placeholder="Subject" v-model="form.subject">
            </div>
            <div class="form-group">
              <textarea name="" id="" cols="30" rows="7" class="form-control" placeholder="Message" v-model="form.message"></textarea>
            </div>
            <div class="form-group">
              <input type="submit" value="Send Message" class="btn btn-primary py-3 px-5">
            </div>
          </form>
        </div>

        <div class="col-md-6 d-flex" data-aos="fade-up" data-aos-delay="100">
          <div class="img" :style="{ backgroundImage: `url(${aboutImg})` }"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive } from 'vue';
import aboutImg from '@/assets/images/about.jpg';

const contactInfo = ref([
  { label: 'Address', value: '198 West 21th Street, Suite 721 New York NY 10016', icon: 'icon-map-signs' },
  { label: 'Contact Number', value: '+ 1235 2355 98', link: 'tel://1234567920', icon: 'icon-phone2' },
  { label: 'Email Address', value: 'info@yoursite.com', link: 'mailto:info@yoursite.com', icon: 'icon-paper-plane' },
  { label: 'Website', value: 'yoursite.com', link: '#', icon: 'icon-globe' }
]);

const form = reactive({
  name: '',
  email: '',
  subject: '',
  message: ''
});

const handleSubmit = () => {
  console.log('Form submitted:', form);
  alert('Thank you for your message!');
};
</script>
