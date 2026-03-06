<template>
  <section class="ftco-section" id="blog-section">
    <div class="container">
      <div class="row justify-content-center mb-5 pb-5">
        <div class="col-md-7 heading-section text-center" data-aos="fade-up" data-aos-duration="1000">
          <h1 class="big big-2">Blog</h1>
          <h2 class="mb-4">Our Blog</h2>
          <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia</p>
        </div>
      </div>
      <div class="row d-flex">
        <div v-for="(post, index) in posts" :key="index" 
             class="col-md-4 d-flex" 
             data-aos="fade-up" 
             :data-aos-delay="index * 100">
          <div class="blog-entry justify-content-end">
            <a href="single.html" class="block-20" :style="{ backgroundImage: `url(${post.image})` }">
            </a>
            <div class="text mt-3 float-right d-block">
              <div class="d-flex align-items-center mb-3 meta">
                <p class="mb-0">
                  <span class="mr-2">{{ post.date }}</span>
                  <a href="#" class="mr-2">{{ post.author }}</a>
                  <a href="#" class="meta-chat"><span class="icon-chat"></span> {{ post.comments }}</a>
                </p>
              </div>
              <h3 class="heading"><a href="single.html">{{ post.title }}</a></h3>
              <p>{{ post.excerpt }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import image1 from '@/assets/images/image_1.jpg';
import image2 from '@/assets/images/image_2.jpg';
import image3 from '@/assets/images/image_3.jpg';

const posts = ref([
  {
    title: 'Why Lead Generation is Key for Business Growth',
    date: 'June 21, 2019',
    author: 'Admin',
    comments: 3,
    image: image1,
    excerpt: 'A small river named Duden flows by their place and supplies it with the necessary regelialia.'
  },
  {
    title: 'Why Lead Generation is Key for Business Growth',
    date: 'June 21, 2019',
    author: 'Admin',
    comments: 3,
    image: image2,
    excerpt: 'A small river named Duden flows by their place and supplies it with the necessary regelialia.'
  },
  {
    title: 'Why Lead Generation is Key for Business Growth',
    date: 'June 21, 2019',
    author: 'Admin',
    comments: 3,
    image: image3,
    excerpt: 'A small river named Duden flows by their place and supplies it with the necessary regelialia.'
  }
]);
</script>
