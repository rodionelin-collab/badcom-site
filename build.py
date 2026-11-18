# -*- coding: utf-8 -*-
"""Генератор статического сайта badcom.ru. Запуск: python3 build.py -> папка site/"""
import os, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import legal

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
os.makedirs(OUT, exist_ok=True)
import shutil as _sh
for _f in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")):
    _sh.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", _f), os.path.join(OUT, _f))

PHONE = "+7 (3952) 798-567"
PHONE_TEL = "+73952798567"
SUPPORT = "+7 939 793-97-14"
SUPPORT_TEL = "+79397939714"
EMAIL = "info@badcom.ru"
LK = "http://lk.badcom.ru/"
TG = "https://t.me/badcom_news"
BRAND_LOGO = '<svg class="brand-logo" role="img" aria-label="Плохая Компания" xmlns="http://www.w3.org/2000/svg" viewBox="23.95 116.70 235.60 50.10" fill="currentColor" fill-rule="evenodd"><path d="M 26.550781 166.089844 L 66.878906 166.089844 C 68.140625 166.089844 69.171875 165.0625 69.171875 163.800781 L 69.171875 146.960938 C 69.171875 139.980469 69.179688 136.496094 68.078125 133.144531 C 67.574219 131.605469 66.902344 130.140625 66.089844 128.769531 C 66.046875 128.703125 66.054688 128.613281 66.101562 128.550781 L 67.917969 126.1875 C 69.839844 123.679688 69.347656 119.972656 66.847656 118.054688 C 64.707031 116.410156 61.878906 116.449219 59.753906 118.078125 L 57.03125 120.164062 C 56.972656 120.210938 56.890625 120.21875 56.824219 120.183594 C 53.570312 118.574219 50.339844 117.914062 46.714844 117.914062 C 43.089844 117.914062 39.859375 118.574219 36.605469 120.183594 C 36.539062 120.21875 36.457031 120.210938 36.398438 120.164062 L 33.675781 118.078125 C 31.554688 116.449219 28.722656 116.410156 26.582031 118.054688 C 24.085938 119.972656 23.589844 123.679688 25.511719 126.1875 L 27.328125 128.550781 C 27.378906 128.613281 27.382812 128.703125 27.339844 128.769531 C 26.527344 130.140625 25.855469 131.605469 25.351562 133.144531 C 24.25 136.496094 24.261719 139.980469 24.261719 146.960938 L 24.261719 163.800781 C 24.261719 165.0625 25.289062 166.089844 26.550781 166.089844 Z M 46.714844 160.136719 C 46.074219 160.136719 45.4375 160 44.84375 159.71875 L 41.121094 157.960938 C 40.066406 157.460938 39.523438 156.277344 39.835938 155.152344 L 45 136.574219 C 45.242188 135.707031 45.980469 135.269531 46.714844 135.269531 C 47.453125 135.269531 48.1875 135.707031 48.429688 136.574219 L 53.59375 155.152344 C 53.90625 156.277344 53.363281 157.460938 52.308594 157.960938 L 48.585938 159.71875 C 47.992188 160 47.355469 160.136719 46.714844 160.136719 Z M 60 140.746094 C 60.3125 139.957031 60.488281 139.09375 60.488281 138.191406 C 60.488281 135.6875 59.160156 133.492188 57.167969 132.273438 C 56.625 131.941406 55.988281 132.207031 55.730469 132.769531 C 55.550781 133.214844 55.714844 133.730469 56.125 133.984375 C 57.539062 134.847656 58.484375 136.410156 58.484375 138.191406 C 58.484375 138.824219 58.363281 139.433594 58.144531 139.988281 C 57.964844 140.445312 58.136719 140.960938 58.554688 141.214844 C 59.078125 141.527344 59.773438 141.320312 60 140.746094 Z M 57.410156 128.578125 C 57.21875 129.066406 57.4375 129.609375 57.898438 129.851562 C 60.90625 131.417969 62.957031 134.5625 62.957031 138.191406 C 62.957031 139.640625 62.628906 141.015625 62.039062 142.246094 C 61.832031 142.683594 61.964844 143.324219 62.417969 143.550781 C 62.925781 143.859375 63.585938 143.652344 63.84375 143.117188 C 64.558594 141.625 64.960938 139.953125 64.960938 138.191406 C 64.960938 133.777344 62.453125 129.949219 58.78125 128.050781 C 58.261719 127.785156 57.628906 128.042969 57.410156 128.578125 Z M 51.609375 139.304688 C 52.066406 140.097656 52.992188 140.585938 54.011719 140.386719 C 54.871094 140.21875 55.566406 139.53125 55.746094 138.675781 C 55.960938 137.65625 55.480469 136.71875 54.691406 136.253906 C 54.503906 136.148438 54.265625 136.183594 54.113281 136.332031 L 51.695312 138.726562 C 51.542969 138.878906 51.503906 139.117188 51.609375 139.304688 Z M 48.859375 146.171875 L 44.570312 146.171875 C 43.625 146.171875 43.0625 147.230469 43.59375 148.011719 L 45.082031 150.199219 C 45.472656 150.777344 46.09375 151.066406 46.714844 151.066406 C 47.335938 151.066406 47.957031 150.777344 48.351562 150.199219 L 49.835938 148.011719 C 50.367188 147.230469 49.804688 146.171875 48.859375 146.171875 Z M 60.566406 122.53125 C 61.644531 123.363281 62.644531 124.292969 63.550781 125.308594 C 63.722656 125.503906 64.03125 125.496094 64.1875 125.289062 L 65.136719 124.054688 C 65.910156 123.046875 65.644531 121.546875 64.714844 120.832031 C 63.785156 120.117188 62.703125 120.230469 61.886719 120.855469 L 60.566406 121.871094 C 60.347656 122.039062 60.351562 122.363281 60.566406 122.53125 Z M 33.429688 140.746094 C 33.117188 139.957031 32.945312 139.09375 32.945312 138.191406 C 32.945312 135.6875 34.273438 133.492188 36.261719 132.273438 C 36.804688 131.941406 37.445312 132.207031 37.699219 132.769531 C 37.878906 133.214844 37.714844 133.730469 37.304688 133.984375 C 35.890625 134.847656 34.945312 136.410156 34.945312 138.191406 C 34.945312 138.824219 35.066406 139.433594 35.285156 139.988281 C 35.464844 140.445312 35.292969 140.960938 34.875 141.214844 C 34.351562 141.527344 33.660156 141.320312 33.429688 140.746094 Z M 36.019531 128.578125 C 36.214844 129.066406 35.996094 129.609375 35.53125 129.851562 C 32.523438 131.417969 30.472656 134.5625 30.472656 138.191406 C 30.472656 139.640625 30.800781 141.015625 31.390625 142.246094 C 31.601562 142.683594 31.46875 143.324219 31.015625 143.550781 C 30.503906 143.859375 29.84375 143.652344 29.585938 143.117188 C 28.871094 141.625 28.46875 139.953125 28.46875 138.191406 C 28.46875 133.777344 30.980469 129.949219 34.648438 128.050781 C 35.167969 127.785156 35.804688 128.042969 36.019531 128.578125 Z M 41.820312 139.304688 C 41.363281 140.097656 40.4375 140.585938 39.417969 140.386719 C 38.558594 140.21875 37.863281 139.53125 37.683594 138.675781 C 37.46875 137.65625 37.949219 136.71875 38.738281 136.253906 C 38.925781 136.148438 39.164062 136.183594 39.316406 136.332031 L 41.734375 138.726562 C 41.886719 138.878906 41.925781 139.117188 41.820312 139.304688 Z M 32.863281 122.53125 C 31.785156 123.363281 30.789062 124.292969 29.878906 125.308594 C 29.707031 125.503906 29.398438 125.496094 29.242188 125.289062 L 28.292969 124.054688 C 27.519531 123.046875 27.785156 121.546875 28.714844 120.832031 C 29.644531 120.117188 30.726562 120.230469 31.542969 120.855469 L 32.867188 121.871094 C 33.082031 122.039062 33.078125 122.363281 32.863281 122.53125 "/><path d="M 98.199219 120.421875 C 98.742188 120.421875 99.015625 120.695312 99.015625 121.238281 L 99.015625 138.621094 C 99.015625 139.164062 98.742188 139.4375 98.199219 139.4375 L 93.851562 139.4375 C 93.308594 139.4375 93.039062 139.164062 93.039062 138.621094 L 93.039062 125.582031 L 86.246094 125.582031 L 86.246094 138.621094 C 86.246094 139.164062 85.976562 139.4375 85.433594 139.4375 L 81.085938 139.4375 C 80.542969 139.4375 80.273438 139.164062 80.273438 138.621094 L 80.273438 121.238281 C 80.273438 120.695312 80.542969 120.421875 81.085938 120.421875 Z M 91.816406 145.382812 C 91.960938 145.113281 92.109375 144.910156 92.265625 144.773438 C 92.417969 144.636719 92.628906 144.570312 92.902344 144.570312 L 97.792969 144.570312 C 98.0625 144.570312 98.257812 144.636719 98.375 144.773438 C 98.492188 144.910156 98.480469 145.113281 98.335938 145.382812 L 93.71875 153.53125 L 98.742188 162.765625 C 98.886719 163.039062 98.902344 163.242188 98.78125 163.378906 C 98.664062 163.515625 98.46875 163.582031 98.199219 163.582031 L 93.308594 163.582031 C 93.039062 163.582031 92.824219 163.515625 92.671875 163.378906 C 92.515625 163.242188 92.367188 163.039062 92.222656 162.765625 L 88.691406 156.25 L 86.246094 156.25 L 86.246094 162.765625 C 86.246094 163.308594 85.976562 163.582031 85.433594 163.582031 L 81.085938 163.582031 C 80.542969 163.582031 80.273438 163.308594 80.273438 162.765625 L 80.273438 145.382812 C 80.273438 144.839844 80.542969 144.570312 81.085938 144.570312 L 85.433594 144.570312 C 85.976562 144.570312 86.246094 144.839844 86.246094 145.382812 L 86.246094 151.085938 L 88.691406 151.085938 Z M 119.304688 159.234375 C 119.304688 160.738281 118.910156 161.882812 118.121094 162.671875 C 117.335938 163.460938 116.1875 163.855469 114.6875 163.855469 L 104.90625 163.855469 C 103.40625 163.855469 102.257812 163.460938 101.472656 162.671875 C 100.683594 161.882812 100.289062 160.738281 100.289062 159.234375 L 100.289062 148.914062 C 100.289062 147.410156 100.683594 146.265625 101.472656 145.480469 C 102.257812 144.691406 103.40625 144.296875 104.90625 144.296875 L 114.6875 144.296875 C 116.1875 144.296875 117.335938 144.691406 118.121094 145.480469 C 118.910156 146.265625 119.304688 147.410156 119.304688 148.914062 Z M 113.328125 150.273438 C 113.328125 149.730469 113.054688 149.457031 112.511719 149.457031 L 107.082031 149.457031 C 106.539062 149.457031 106.265625 149.730469 106.265625 150.273438 L 106.265625 157.878906 C 106.265625 158.421875 106.539062 158.691406 107.082031 158.691406 L 112.511719 158.691406 C 113.054688 158.691406 113.328125 158.421875 113.328125 157.878906 Z M 133.753906 163.582031 C 133.480469 163.582031 133.269531 163.515625 133.117188 163.378906 C 132.960938 163.242188 132.769531 163.054688 132.667969 162.765625 L 129.136719 152.933594 L 128.863281 152.933594 L 128.863281 162.765625 C 128.863281 163.308594 128.59375 163.582031 128.050781 163.582031 L 123.703125 163.582031 C 123.160156 163.582031 122.890625 163.308594 122.890625 162.765625 L 122.890625 145.382812 C 122.890625 144.839844 123.160156 144.570312 123.703125 144.570312 L 129.949219 144.570312 C 130.222656 144.570312 130.433594 144.636719 130.589844 144.773438 C 130.742188 144.910156 130.890625 145.113281 131.039062 145.382812 L 134.976562 154.890625 L 135.246094 154.890625 L 139.1875 145.382812 C 139.332031 145.113281 139.480469 144.910156 139.632812 144.773438 C 139.789062 144.636719 140 144.570312 140.273438 144.570312 L 146.519531 144.570312 C 147.0625 144.570312 147.335938 144.839844 147.335938 145.382812 L 147.335938 162.765625 C 147.335938 163.308594 147.0625 163.582031 146.519531 163.582031 L 142.171875 163.582031 C 141.628906 163.582031 141.359375 163.308594 141.359375 162.765625 L 141.359375 152.933594 L 141.085938 152.933594 L 137.554688 162.765625 C 137.453125 163.054688 137.261719 163.242188 137.109375 163.378906 C 136.953125 163.515625 136.742188 163.582031 136.46875 163.582031 Z M 169.117188 144.570312 C 169.660156 144.570312 169.933594 144.839844 169.933594 145.382812 L 169.933594 162.765625 C 169.933594 163.308594 169.660156 163.582031 169.117188 163.582031 L 164.773438 163.582031 C 164.230469 163.582031 163.957031 163.308594 163.957031 162.765625 L 163.957031 149.730469 L 157.167969 149.730469 L 157.167969 162.765625 C 157.167969 163.308594 156.894531 163.582031 156.351562 163.582031 L 152.007812 163.582031 C 151.464844 163.582031 151.191406 163.308594 151.191406 162.765625 L 151.191406 145.382812 C 151.191406 144.839844 151.464844 144.570312 152.007812 144.570312 Z M 185.957031 160.324219 L 179.4375 160.324219 L 178.488281 162.765625 C 178.289062 163.308594 177.925781 163.582031 177.402344 163.582031 L 172.785156 163.582031 C 172.222656 163.582031 172.042969 163.308594 172.242188 162.765625 L 178.761719 145.382812 C 178.976562 144.839844 179.339844 144.570312 179.847656 144.570312 L 185.550781 144.570312 C 185.894531 144.570312 186.144531 144.636719 186.296875 144.773438 C 186.453125 144.910156 186.566406 145.113281 186.636719 145.382812 L 193.15625 162.765625 C 193.335938 163.308594 193.15625 163.582031 192.613281 163.582031 L 187.996094 163.582031 C 187.6875 163.582031 187.457031 163.515625 187.304688 163.378906 C 187.148438 163.242188 187.015625 163.039062 186.910156 162.765625 Z M 182.5625 151.628906 L 181.203125 155.160156 L 184.191406 155.160156 L 182.835938 151.628906 Z M 208.230469 151.628906 L 208.230469 145.382812 C 208.230469 144.839844 208.503906 144.570312 209.046875 144.570312 L 213.390625 144.570312 C 213.933594 144.570312 214.207031 144.839844 214.207031 145.382812 L 214.207031 162.765625 C 214.207031 163.308594 213.933594 163.582031 213.390625 163.582031 L 209.046875 163.582031 C 208.503906 163.582031 208.230469 163.308594 208.230469 162.765625 L 208.230469 156.792969 L 201.441406 156.792969 L 201.441406 162.765625 C 201.441406 163.308594 201.167969 163.582031 200.625 163.582031 L 196.28125 163.582031 C 195.738281 163.582031 195.464844 163.308594 195.464844 162.765625 L 195.464844 145.382812 C 195.464844 144.839844 195.738281 144.570312 196.28125 144.570312 L 200.625 144.570312 C 201.167969 144.570312 201.441406 144.839844 201.441406 145.382812 L 201.441406 151.628906 Z M 231.101562 153.804688 L 230.828125 153.804688 L 225.398438 162.765625 C 225.253906 163.039062 225.101562 163.242188 224.949219 163.378906 C 224.792969 163.515625 224.582031 163.582031 224.308594 163.582031 L 218.878906 163.582031 C 218.335938 163.582031 218.0625 163.308594 218.0625 162.765625 L 218.0625 145.382812 C 218.0625 144.839844 218.335938 144.570312 218.878906 144.570312 L 223.222656 144.570312 C 223.765625 144.570312 224.039062 144.839844 224.039062 145.382812 L 224.039062 154.347656 L 224.308594 154.347656 L 229.742188 145.382812 C 229.886719 145.113281 230.039062 144.910156 230.191406 144.773438 C 230.34375 144.636719 230.558594 144.570312 230.828125 144.570312 L 236.261719 144.570312 C 236.804688 144.570312 237.078125 144.839844 237.078125 145.382812 L 237.078125 162.765625 C 237.078125 163.308594 236.804688 163.582031 236.261719 163.582031 L 231.914062 163.582031 C 231.371094 163.582031 231.101562 163.308594 231.101562 162.765625 Z M 252.695312 152.988281 L 252.695312 149.730469 L 247.261719 149.730469 C 246.71875 149.730469 246.445312 150 246.445312 150.542969 L 246.445312 152.175781 C 246.445312 152.71875 246.71875 152.988281 247.261719 152.988281 Z M 249.164062 158.148438 L 246.71875 162.765625 C 246.574219 163.039062 246.425781 163.242188 246.269531 163.378906 C 246.117188 163.515625 245.902344 163.582031 245.632812 163.582031 L 241.015625 163.582031 C 240.742188 163.582031 240.5625 163.496094 240.472656 163.324219 C 240.382812 163.152344 240.382812 162.964844 240.472656 162.765625 L 243.1875 157.878906 C 242.679688 157.75 242.226562 157.507812 241.828125 157.144531 C 241.484375 156.835938 241.171875 156.398438 240.894531 155.828125 C 240.613281 155.257812 240.472656 154.492188 240.472656 153.53125 L 240.472656 149.1875 C 240.472656 147.683594 240.867188 146.539062 241.652344 145.75 C 242.441406 144.960938 243.585938 144.570312 245.089844 144.570312 L 257.855469 144.570312 C 258.398438 144.570312 258.671875 144.839844 258.671875 145.382812 L 258.671875 162.765625 C 258.671875 163.308594 258.398438 163.582031 257.855469 163.582031 L 253.507812 163.582031 C 252.964844 163.582031 252.695312 163.308594 252.695312 162.765625 L 252.695312 158.148438 Z M 106.671875 121.238281 C 106.726562 120.964844 106.835938 120.761719 107 120.625 C 107.164062 120.492188 107.414062 120.421875 107.757812 120.421875 L 120.527344 120.421875 C 121.070312 120.421875 121.339844 120.695312 121.339844 121.238281 L 121.339844 138.621094 C 121.339844 139.164062 121.070312 139.4375 120.527344 139.4375 L 116.179688 139.4375 C 115.636719 139.4375 115.363281 139.164062 115.363281 138.621094 L 115.363281 125.582031 L 111.699219 125.582031 L 109.660156 135.363281 C 109.371094 136.71875 108.796875 137.785156 107.9375 138.554688 C 107.078125 139.324219 105.804688 139.707031 104.121094 139.707031 L 102.054688 139.707031 C 101.511719 139.707031 101.242188 139.4375 101.242188 138.890625 L 101.242188 135.363281 C 101.242188 134.816406 101.511719 134.546875 102.054688 134.546875 L 103.007812 134.546875 C 103.351562 134.546875 103.597656 134.476562 103.753906 134.34375 C 103.90625 134.207031 104.019531 134.003906 104.09375 133.730469 Z M 143.9375 135.089844 C 143.9375 136.59375 143.546875 137.738281 142.757812 138.527344 C 141.96875 139.3125 140.824219 139.707031 139.320312 139.707031 L 129.542969 139.707031 C 128.039062 139.707031 126.894531 139.3125 126.105469 138.527344 C 125.320312 137.738281 124.925781 136.59375 124.925781 135.089844 L 124.925781 124.769531 C 124.925781 123.265625 125.320312 122.121094 126.105469 121.332031 C 126.894531 120.542969 128.039062 120.152344 129.542969 120.152344 L 139.320312 120.152344 C 140.824219 120.152344 141.96875 120.542969 142.757812 121.332031 C 143.546875 122.121094 143.9375 123.265625 143.9375 124.769531 Z M 137.964844 126.125 C 137.964844 125.582031 137.691406 125.3125 137.148438 125.3125 L 131.714844 125.3125 C 131.171875 125.3125 130.902344 125.582031 130.902344 126.125 L 130.902344 133.730469 C 130.902344 134.273438 131.171875 134.546875 131.714844 134.546875 L 137.148438 134.546875 C 137.691406 134.546875 137.964844 134.273438 137.964844 133.730469 Z M 152.277344 138.621094 C 152.132812 138.890625 151.984375 139.097656 151.828125 139.230469 C 151.675781 139.367188 151.464844 139.4375 151.191406 139.4375 L 146.03125 139.4375 C 145.777344 139.4375 145.585938 139.367188 145.460938 139.230469 C 145.332031 139.097656 145.34375 138.890625 145.488281 138.621094 L 151.328125 129.386719 L 146.03125 121.238281 C 145.886719 120.964844 145.871094 120.761719 145.988281 120.625 C 146.109375 120.492188 146.300781 120.421875 146.574219 120.421875 L 151.734375 120.421875 C 152.007812 120.421875 152.21875 120.492188 152.371094 120.625 C 152.527344 120.761719 152.675781 120.964844 152.820312 121.238281 L 155.265625 125.582031 L 155.539062 125.582031 L 157.980469 121.238281 C 158.125 120.964844 158.277344 120.761719 158.429688 120.625 C 158.582031 120.492188 158.796875 120.421875 159.066406 120.421875 L 164.230469 120.421875 C 164.5 120.421875 164.695312 120.492188 164.8125 120.625 C 164.929688 120.761719 164.917969 120.964844 164.773438 121.238281 L 159.476562 129.386719 L 165.316406 138.621094 C 165.460938 138.890625 165.46875 139.097656 165.34375 139.230469 C 165.214844 139.367188 165.027344 139.4375 164.773438 139.4375 L 159.613281 139.4375 C 159.339844 139.4375 159.128906 139.367188 158.972656 139.230469 C 158.820312 139.097656 158.667969 138.890625 158.523438 138.621094 L 155.539062 133.730469 L 155.265625 133.730469 Z M 179.847656 136.175781 L 173.328125 136.175781 L 172.378906 138.621094 C 172.179688 139.164062 171.816406 139.4375 171.292969 139.4375 L 166.671875 139.4375 C 166.113281 139.4375 165.929688 139.164062 166.128906 138.621094 L 172.648438 121.238281 C 172.867188 120.695312 173.226562 120.421875 173.734375 120.421875 L 179.4375 120.421875 C 179.785156 120.421875 180.03125 120.492188 180.1875 120.625 C 180.339844 120.761719 180.453125 120.964844 180.527344 121.238281 L 187.042969 138.621094 C 187.226562 139.164062 187.042969 139.4375 186.5 139.4375 L 181.882812 139.4375 C 181.574219 139.4375 181.34375 139.367188 181.191406 139.230469 C 181.039062 139.097656 180.90625 138.890625 180.796875 138.621094 Z M 176.453125 127.484375 L 175.09375 131.015625 L 178.082031 131.015625 L 176.722656 127.484375 Z M 201.113281 128.84375 L 201.113281 125.582031 L 195.683594 125.582031 C 195.140625 125.582031 194.867188 125.855469 194.867188 126.398438 L 194.867188 128.027344 C 194.867188 128.570312 195.140625 128.84375 195.683594 128.84375 Z M 197.582031 134.003906 L 195.140625 138.621094 C 194.992188 138.890625 194.84375 139.097656 194.691406 139.230469 C 194.535156 139.367188 194.324219 139.4375 194.050781 139.4375 L 189.433594 139.4375 C 189.164062 139.4375 188.980469 139.351562 188.890625 139.175781 C 188.800781 139.003906 188.800781 138.820312 188.890625 138.621094 L 191.609375 133.730469 C 191.101562 133.605469 190.648438 133.359375 190.25 133 C 189.90625 132.691406 189.59375 132.25 189.3125 131.679688 C 189.03125 131.109375 188.890625 130.34375 188.890625 129.386719 L 188.890625 125.039062 C 188.890625 123.535156 189.285156 122.390625 190.074219 121.605469 C 190.859375 120.816406 192.007812 120.421875 193.507812 120.421875 L 206.273438 120.421875 C 206.816406 120.421875 207.089844 120.695312 207.089844 121.238281 L 207.089844 138.621094 C 207.089844 139.164062 206.816406 139.4375 206.273438 139.4375 L 201.929688 139.4375 C 201.386719 139.4375 201.113281 139.164062 201.113281 138.621094 L 201.113281 134.003906 Z M 197.582031 134.003906 "/></svg>'
MAX_NEWS = "https://max.ru/join/XAXjnlNrrLzhJx-er5I15L_bUsMX1Jy7rJkCYFIokds"

DISTRICTS = ["Аларский", "Боханский", "Жигаловский", "Заларинский", "Зиминский",
             "Казачинско-Ленский", "Качугский", "Усольский", "Усть-Удинский", "Черемховский"]


# ---------- населённые пункты по районам (файл data/settlements.txt) ----------
def load_settlements():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "settlements.txt")
    res, cur = {}, None
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            cur = line[1:-1].strip()
            assert cur in DISTRICTS, f"Неизвестный район в settlements.txt: {cur}"
            res[cur] = []
            continue
        parts = [p.strip() for p in line.split("|")]
        name = parts[0]
        kind = parts[1] if len(parts) > 1 else ""
        note = parts[2] if len(parts) > 2 else ""
        res[cur].append({"n": name, "t": kind, "x": note})
    for d in res:
        res[d].sort(key=lambda s: s["n"])
    return res
SETTLEMENTS = load_settlements()

PAGES = [  # slug, короткое имя в навигации
    ("index", "Базовые"),
    ("tariff_zone2", "Зона «х2»"),
    ("tariff_sputnik", "Спутник"),
    ("tariff_biz", "Юрлицам"),
    ("tariff_sputnik_biz", "Спутник юрлицам"),
]

def href(slug):
    return "/" if slug == "index" else f"/{slug}"

# ---------- данные тарифов ----------
def unlim(rows):
    return [dict(name=n, price=p, speed=s) for n, p, s in rows]

BASE = unlim([("512/512", 700, "512 Кбит/с"), ("1 Мегабит", 900, "1 Мбит/с"),
              ("2 Мегабита", 1100, "2 Мбит/с"), ("5 Мегабит", 1350, "5 Мбит/с"),
              ("10 Мегабит", 1800, "10 Мбит/с"), ("Максимум", 2800, "до 20 Мбит/с")])
X2 = unlim([("512/512", 1100, "512 Кбит/с"), ("1 Мегабит", 1500, "1 Мбит/с"),
            ("2 Мегабита", 1850, "2 Мбит/с"), ("5 Мегабит", 2350, "5 Мбит/с"),
            ("10 Мегабит", 3300, "10 Мбит/с"), ("Максимум", 5000, "до 20 Мбит/с")])
BIZ = unlim([("512/512", 2000, "512 Кбит/с"), ("1 Мегабит", 2500, "1 Мбит/с"),
             ("2 Мегабита", 3000, "2 Мбит/с"), ("5 Мегабит", 4000, "5 Мбит/с"),
             ("10 Мегабит", 7000, "10 Мбит/с"), ("Максимум", 9500, "до 20 Мбит/с")])

def vol(rows):  # помегабайтные: имя, цена, объём, цена МБ сверх, скорость
    return [dict(name=n, price=p, volume=v, over=o, speed=s) for n, p, v, o, s in rows]

def surf(rows):  # серфинг: имя, цена, сутки, месяц, скорость, после лимита
    return [dict(name=n, price=p, day=d, month=m, speed=s, after=a) for n, p, d, m, s, a in rows]

SAT_VOL = vol([("Помегабайтный", 400, "1,5 ГБ", "20 коп.", "до 1/1 Мбит/с"),
               ("Скорость-3", 1100, "3 ГБ", "16 коп.", "до 2/2 Мбит/с"),
               ("Скорость-5", 1300, "5 ГБ", "15 коп.", "до 5/5 Мбит/с"),
               ("Скорость-10", 1900, "10 ГБ", "14 коп.", "до 5/5 Мбит/с"),
               ("Скорость-15", 2500, "15 ГБ", "13 коп.", "до 5/5 Мбит/с"),
               ("Скорость-20", 4300, "20 ГБ", "12 коп.", "до 5/5 Мбит/с")])
SAT_SURF = surf([("Серфинг-350", 1600, "350 МБ", "~10,5 ГБ", "до 1/1 Мбит/с", "без доступа до следующих суток"),
                 ("Серфинг-500", 1900, "500 МБ", "~15 ГБ", "до 2/2 Мбит/с", "до 64/64 Кбит/с"),
                 ("Серфинг-800", 2500, "800 МБ", "~24 ГБ", "до 3/3 Мбит/с", "до 64/64 Кбит/с")])
TURBO = [("Турбо 500", 200, "500 МБ трафика на скорости вашего тарифа"),
         ("Турбо 1500", 400, "1500 МБ трафика на скорости вашего тарифа"),
         ("Турбо Unlim", 900, "Безлимит на одни сутки на скорости до 1/1 Мбит/с")]

SATB_VOL = vol([("Помегабайтный", 700, "1,5 ГБ", "20 коп.", "до 1/1 Мбит/с"),
                ("Скорость-3", 1600, "3 ГБ", "16 коп.", "до 2/2 Мбит/с"),
                ("Скорость-5", 1900, "5 ГБ", "15 коп.", "до 5/5 Мбит/с"),
                ("Скорость-10", 2700, "10 ГБ", "14 коп.", "до 5/5 Мбит/с"),
                ("Скорость-15", 3500, "15 ГБ", "13 коп.", "до 5/5 Мбит/с"),
                ("Скорость-20", 5900, "20 ГБ", "12 коп.", "до 5/5 Мбит/с")])
SATB_SURF = surf([("Серфинг-350", 2500, "350 МБ", "~10,5 ГБ", "до 1/1 Мбит/с", "без доступа до следующих суток"),
                  ("Серфинг-500", 3300, "500 МБ", "~15 ГБ", "до 2/2 Мбит/с", "до 64/64 Кбит/с"),
                  ("Серфинг-800", 4800, "800 МБ", "~24 ГБ", "до 3/3 Мбит/с", "до 64/64 Кбит/с"),
                  ("Серфинг-1000", 5900, "1000 МБ", "~30 ГБ", "до 3/3 Мбит/с", "до 64/64 Кбит/с"),
                  ("Серфинг-2000", 9500, "2000 МБ", "~60 ГБ", "до 3/3 Мбит/с", "до 64/64 Кбит/с"),
                  ("Серфинг-5000", 18000, "5000 МБ", "~150 ГБ", "до 3/3 Мбит/с", "до 64/64 Кбит/с")])

def rub(n):
    return f"{n:,}".replace(",", " ") + " ₽"

# ---------- фрагменты ----------
CSS = r"""
:root{
  --taiga:#1E3A2F; --taiga-2:#2B4F40; --ink:#15211B; --muted:#56665E;
  --paper:#EEF2EF; --white:#FFFFFF; --line:#C9D4CE; --signal:#F2B705; --signal-ink:#3A2C00;
  --todo:#FFE9A8;
  --r-s:6px; --r-m:14px;
  --wrap:1160px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{animation:none!important;transition:none!important}}
body{margin:0;background:var(--paper);color:var(--ink);font:400 17px/1.6 "Golos Text",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}
:focus-visible{outline:3px solid var(--signal);outline-offset:3px;border-radius:4px}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 24px}
h1,h2,h3{font-family:"Unbounded",sans-serif;font-weight:600;line-height:1.12;margin:0;letter-spacing:-.01em}
h2{font-size:clamp(26px,3.4vw,40px)}
h3{font-size:19px}
p{margin:0 0 1em;max-width:68ch}
.muted{color:var(--muted)}
.skip{position:absolute;left:-999px}.skip:focus{left:16px;top:16px;background:var(--white);padding:8px 12px;z-index:10}

/* header */
.top{background:var(--taiga);color:#E6EEE9}
.top .wrap{display:flex;align-items:center;gap:20px;min-height:72px;flex-wrap:wrap;padding-top:10px;padding-bottom:10px}
.mark{display:block;text-decoration:none;line-height:0;margin-right:auto;color:#fff;flex:none}
.brand-logo{display:block;height:40px;width:auto}
.top .wrap{max-width:none;padding-left:28px;padding-right:28px}
.nav{display:flex;gap:14px;flex-wrap:wrap}
@media (min-width:901px){.top .wrap{flex-wrap:nowrap}.nav{flex-wrap:nowrap;white-space:nowrap}}
.nav a{text-decoration:none;font-size:15px;color:#D5E1DA}
.nav a:hover{color:#fff;text-decoration:underline;text-underline-offset:4px}
.top .tel{font-weight:600;text-decoration:none;color:#fff;white-space:nowrap}
.top .tel .ic{display:none;width:44px;height:44px;padding:11px;border-radius:50%;box-shadow:inset 0 0 0 2px #5C8A75;box-sizing:border-box}
@media (min-width:901px) and (max-width:1120px){.nav a[href*="t.me"]{display:none}.top .tel span{display:none}.top .tel .ic{display:block;width:40px;height:40px;padding:10px}}
@media (min-width:901px){.top{position:sticky;top:0;z-index:30;box-shadow:0 1px 0 rgba(255,255,255,.06)}}
html{scroll-padding-top:84px}
@media (max-width:900px){html{scroll-padding-top:12px}}
.btn{display:inline-flex;align-items:center;gap:8px;font:600 16px/1 "Golos Text",system-ui,sans-serif;text-decoration:none;border:0;cursor:pointer;
  padding:14px 20px;border-radius:var(--r-s);white-space:nowrap;background:var(--signal);color:var(--signal-ink)}
.btn:hover{background:#FFC820}
.btn.ghost{background:transparent;color:inherit;box-shadow:inset 0 0 0 2px currentColor}
.btn.ghost:hover{background:rgba(255,255,255,.08)}
.top .btn{padding:11px 16px;font-size:15px}

/* hero */
.hero{background:var(--taiga);color:#EAF1ED;position:relative;overflow:hidden;padding:64px 0 56px}
.hero .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:stretch;position:relative;z-index:1}
.hero-side{display:flex;flex-direction:column}
.hero-side .hero-card{flex:1;display:flex;flex-direction:column;justify-content:space-between}
.hero-main h1{margin:0}
.hero-statement{font-family:"Unbounded",sans-serif;font-weight:700;font-size:clamp(24px,2.4vw,32px);line-height:1.22;letter-spacing:-.02em;color:#fff;margin:0 0 18px;max-width:22ch}
.hero h1{font-size:clamp(44px,8.2vw,108px);font-weight:700;line-height:.92;letter-spacing:-.035em;color:#fff}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.hero .lede{font-size:clamp(17px,1.6vw,20px);line-height:1.5;margin:0 0 30px;color:#D3DFD8;max-width:44ch}
.hero-card{align-self:stretch;background:transparent;color:#fff;border-radius:var(--r-m);padding:8px 22px 6px;box-shadow:inset 0 0 0 2px currentColor}
.hero-card h2{font-size:14px;font-family:"Golos Text",system-ui,sans-serif;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:#A9BDB2;padding:14px 0 6px}
.hc{display:grid;grid-template-columns:1fr auto;align-items:center;gap:2px 12px;padding:13px 0;border-top:1px solid rgba(255,255,255,.22);text-decoration:none;color:inherit}
.hc b{font-size:17px}
.hc span{grid-column:1;font-size:14px;color:#B9CBC1}
.hc i{grid-column:2;grid-row:1/3;font-style:normal;font-size:20px;color:var(--signal)}
.hc:hover b{text-decoration:underline;text-underline-offset:4px}
.hero-card h2+.hc{border-top:0}
.hc.main b{display:inline-block;background:var(--signal);color:var(--signal-ink);padding:9px 16px;border-radius:var(--r-s);font-size:16px}
.hc.main i{display:none}
.hero .actions{display:flex;gap:12px;flex-wrap:wrap}
.waves{position:absolute;right:-260px;top:-330px;width:760px;height:760px;opacity:.45;pointer-events:none}
.waves circle{fill:none;stroke:#3F6A57;stroke-width:1.5}
.waves .pulse{stroke:var(--signal);stroke-width:2;opacity:0;animation:ping 4.5s ease-out 1}
.waves .pulse:nth-of-type(2){animation-delay:.35s}.waves .pulse:nth-of-type(3){animation-delay:.7s}
@keyframes ping{0%{opacity:0}20%{opacity:.9}100%{opacity:0}}
.where{background:var(--white);color:var(--ink);border-radius:var(--r-m);padding:24px 24px 20px}
.where h2{font-size:18px;margin-bottom:6px}
.where p{font-size:15px;color:var(--muted);margin-bottom:14px}
.where ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:2px 16px}
.zona{padding:48px 0 8px}
.zona .where{background:var(--white);padding:32px 32px 28px;box-shadow:0 1px 0 #E3E9E5}
.zona .where h2{font-size:28px;margin-bottom:8px}
.zona .where>p{max-width:64ch}
.zona .dlist{grid-template-columns:repeat(5,1fr);gap:4px 24px;margin-top:6px}
.zona .dlist li{display:flex;align-items:baseline}.zona .dlist li::before{flex:none}
.zona .wl{margin-top:22px;padding:20px 24px}
.zona .wl h3{font-size:18px}
.zona .wl ul{columns:4 170px;max-height:none;overflow:visible}
.zona .wl-static{margin-top:10px;columns:2 300px;column-gap:32px}
@media (max-width:900px){.zona .dlist{grid-template-columns:1fr 1fr}.zona .where{padding:22px 18px}}
.where .dbtn{all:unset;box-sizing:border-box;cursor:pointer;display:inline;font-size:15px;color:var(--ink);text-decoration:underline;text-decoration-color:#B9C7BF;text-underline-offset:4px}
.where .dbtn:hover,.where .dbtn.on{color:var(--taiga);text-decoration-color:var(--signal)}
.where .dbtn:focus-visible{outline:2px solid var(--taiga);outline-offset:3px;border-radius:4px}
.where .dbtn.on{font-weight:700}
.where .dlist[hidden],.where .wl[hidden]{display:none}
.where li:has(.dbtn)::before{margin-right:10px}
.wl{margin-top:16px;padding:14px 16px;border-radius:12px;background:#EEF3F0}
.wl h3{font-size:16px;margin:0 0 8px}
.wl ul{display:block;columns:2 150px;max-height:230px;overflow:auto;margin:0 0 12px;padding:0}
.where .wl li{border:0;padding:3px 0;font-size:14px;break-inside:avoid}.where .wl li::before{display:none}
.wl small{color:var(--muted)}
.wl .btn.sm{padding:9px 14px;font-size:14px}
.wl-close{all:unset;cursor:pointer;margin-left:12px;font-size:14px;color:var(--muted);text-decoration:underline}
.wl-static details{border-bottom:1px solid #E3E9E5;padding:6px 0;font-size:15px}
.wl-static p{font-size:14px;margin:6px 0 0}
.where li{padding:7px 0;border-bottom:1px solid #E3E9E5;font-size:15px}
.where li::before{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--signal);margin-right:10px;vertical-align:1px}

/* page head for tariff pages */
.phead{background:var(--taiga);color:#fff;padding:44px 0 40px}
.phead h1{font-size:clamp(32px,5vw,58px);letter-spacing:-.025em}
.phead p{color:#C9D8CF;margin:14px 0 0}

/* sections */
section{padding:72px 0}
.sec-head{display:flex;justify-content:space-between;align-items:end;gap:24px;flex-wrap:wrap;margin-bottom:28px}
.sec-head p{margin:10px 0 0;color:var(--muted)}

/* service strip */
.strip{background:var(--white);border-bottom:1px solid var(--line);padding:0}
.strip .wrap{display:grid;grid-template-columns:repeat(3,1fr)}
.strip a{display:block;padding:22px 24px;text-decoration:none;border-left:1px solid var(--line)}
.strip a:first-child{border-left:0;padding-left:0}
.strip b{display:block;font-size:17px}
.strip span{font-size:14px;color:var(--muted)}
.strip a:hover b{text-decoration:underline;text-underline-offset:4px}

/* tariff tabs */
.tabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:22px}
.tabs a{padding:9px 15px;border-radius:999px;text-decoration:none;font-size:15px;background:var(--white);box-shadow:inset 0 0 0 1px var(--line)}
.tabs a[aria-current]{background:var(--taiga);color:#fff;box-shadow:none}
.tabs a:not([aria-current]):hover{box-shadow:inset 0 0 0 1px var(--taiga)}

/* tariff table */
.plans{background:var(--white);border-radius:var(--r-m);overflow:hidden}
.plan{display:grid;grid-template-columns:minmax(150px,1fr) 2fr auto;gap:20px;align-items:center;padding:20px 28px;border-top:1px solid #E3E9E5}
.plan:first-child{border-top:0}
.plan .nm{font-family:"Unbounded",sans-serif;font-weight:600;font-size:18px}
.plan .det{font-size:15px;color:var(--muted)}
.plan .det b{color:var(--ink);font-weight:600}
.plan .pr{font-family:"Unbounded",sans-serif;font-weight:600;font-size:24px;white-space:nowrap;text-align:right}
.plan .pr small{display:block;font-family:"Golos Text",system-ui,sans-serif;font-weight:400;font-size:13px;color:var(--muted)}
.bar{height:6px;border-radius:3px;background:#E3E9E5;margin-top:8px;max-width:260px}
.bar i{display:block;height:100%;border-radius:3px;background:var(--taiga-2)}
.plans-cap{font-family:"Unbounded",sans-serif;font-size:17px;font-weight:600;margin:36px 0 12px}

/* conditions */
.dl{background:var(--white);border-radius:var(--r-m);padding:26px 28px;margin-top:20px}
.dl h3{margin-bottom:8px}
.dl .muted{font-size:16px;margin:0 0 16px;max-width:70ch}
.dl-scroll{overflow-x:auto}
.dl table{width:100%;border-collapse:collapse;font-size:16px}
.dl th,.dl td{padding:11px 12px;text-align:right;border-bottom:1px solid var(--line);white-space:nowrap}
.dl thead th{font-size:14px;color:var(--muted);font-weight:600;border-bottom:2px solid var(--ink)}
.dl th:first-child,.dl td:first-child{text-align:left;padding-left:0}
.dl th:last-child,.dl td:last-child{padding-right:0}
.dl tbody th{font-weight:700;color:var(--ink)}
.dl tbody tr:last-child th,.dl tbody tr:last-child td{border-bottom:0}
.dl td:last-child{color:var(--taiga)}
.dl-note{font-size:14px;color:var(--muted);margin:14px 0 0}
@media (max-width:640px){.dl{padding:22px 18px}.dl th:nth-child(2),.dl td:nth-child(2){display:none}.dl th,.dl td{padding:11px 6px;font-size:15px}.dl thead th{font-size:13px;white-space:normal}.dl td:last-child b{white-space:nowrap}}
.cond{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:20px}
.note{background:var(--white);border-radius:var(--r-m);padding:26px 28px}
.note h3{margin-bottom:10px}
.note p{font-size:16px}
.note p:last-child{margin-bottom:0}
.price-big{font-family:"Unbounded",sans-serif;font-weight:700;font-size:40px;line-height:1;margin:6px 0 12px}
.callout{border-left:4px solid var(--signal);background:#FFF8E0;padding:16px 20px;border-radius:0 var(--r-s) var(--r-s) 0;margin-top:20px;font-size:16px}
.callout p{margin:0}

/* faq */
.faq{max-width:840px}
.faq.faq-cols{max-width:none;display:grid;grid-template-columns:1fr 1fr;gap:0 56px;align-items:start}
.faq-col h3{font-size:18px;margin:0 0 10px}
.faq-col details:first-of-type{border-top:1px solid var(--line)}
.faq details{border-top:1px solid var(--line)}
.faq details:last-child{border-bottom:1px solid var(--line)}
.faq summary{cursor:pointer;list-style:none;padding:20px 40px 20px 0;font-weight:600;font-size:18px;position:relative}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"";position:absolute;right:6px;top:50%;width:12px;height:12px;border-right:2px solid var(--ink);border-bottom:2px solid var(--ink);transform:translateY(-70%) rotate(45deg);transition:transform .2s}
.faq details[open] summary::after{transform:translateY(-30%) rotate(-135deg)}
.faq .a{padding:0 0 20px}
.settle-hint{font-size:14px;margin:8px 0 0}
#settle-box[hidden]{display:none}
.faq .a ol,.faq .a ul{padding-left:22px;margin:0 0 1em}
.faq .a li{margin-bottom:6px}
.todo{background:var(--todo);padding:2px 6px;border-radius:4px}

/* reviews */
.reviews{background:var(--taiga);color:#E6EEE9}
.reviews h2{color:#fff}
.rv{columns:2 340px;column-gap:40px;margin-top:28px}
.rv figure{break-inside:avoid;margin:0 0 36px}
.rv blockquote{margin:0;font-size:17px;line-height:1.6}
.rb-row{display:flex;flex-wrap:wrap;gap:14px;align-items:center;margin:18px 0 6px}
.rb{display:inline-flex;align-items:baseline;gap:6px;padding:10px 16px;border-radius:12px;background:rgba(255,255,255,.1);color:inherit;text-decoration:none}
.rb b{font-size:28px;line-height:1}.rb span{color:var(--signal)}.rb small{opacity:.85}
.rb-asof{opacity:.7;flex-basis:100%}
.stars{color:var(--signal);letter-spacing:2px;font-size:16px}.stars i{font-style:normal;opacity:.25}
.rv-top{display:flex;justify-content:space-between;gap:12px;margin-bottom:8px;font-size:14px;opacity:.9}
.rvc{background:rgba(255,255,255,.06);padding:18px 20px;border-radius:14px}
.rv-page{columns:2 360px;column-gap:24px}.rv-page .rvc{margin-bottom:20px;background:var(--mist,#EEF3F0);color:#16231D}
.rv.rv-page figcaption{color:#16231D}.rv.rv-page .rv-src{color:#4D5F56;opacity:1}.rv.rv-page .rv-top{color:#16231D}.rvp .rb{background:#E3ECE7;color:#16231D}.rvp .rb-asof{color:#16231D}
.rv-page blockquote{font-size:16px}
.btn.ghost.dark{color:#16231D}
.rv-src{font-weight:400;opacity:.75}
.rv-links{margin-top:8px;display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.rv-links p{flex-basis:100%;margin:0 0 4px;color:#C9D8CF}
.rv figcaption{margin-top:10px;color:var(--signal);font-weight:600}

/* form */
.apply .wrap{display:grid;grid-template-columns:.9fr 1.1fr;gap:48px;align-items:start}
form{background:var(--white);border-radius:var(--r-m);padding:28px}
label{display:block;font-weight:600;font-size:15px;margin:0 0 6px}
input,textarea,select{width:100%;font:inherit;padding:12px 14px;border:1px solid var(--line);border-radius:var(--r-s);background:#FBFCFB;margin-bottom:16px;color:var(--ink)}
input:focus,textarea:focus,select:focus{outline:2px solid var(--taiga);border-color:var(--taiga)}
textarea{min-height:96px;resize:vertical}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.consent{display:flex;gap:10px;font-weight:400;font-size:14px;color:var(--muted);align-items:flex-start}
.consent input{width:auto;margin:3px 0 0}
.hp{display:none}
.direct{margin-top:22px}
.direct a{font-weight:600}

/* contacts */
.contacts .wrap{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.hours{font-size:15px;color:var(--muted)}
.docs{list-style:none;margin:0;padding:0}
.docs li{border-top:1px solid #E3E9E5;padding:12px 0}
.docs li:first-child{border-top:0;padding-top:0}
.docs a,.docs b.doc{font-weight:600}
.docs span{display:block;font-size:14px;color:var(--muted)}
details.req summary{cursor:pointer;font-weight:600;margin-top:16px}
.req dl{display:grid;grid-template-columns:max-content 1fr;gap:6px 18px;font-size:14px;margin:14px 0 0}
.req dt{color:var(--muted)}.req dd{margin:0}

footer{background:var(--ink);color:#A9B8B0;font-size:14px;padding:32px 0}
footer .wrap{display:flex;gap:16px 32px;flex-wrap:wrap;justify-content:space-between}
footer a{color:#D5E1DA}

@media (max-width:900px){
  .hero .wrap,.apply .wrap,.contacts .wrap,.cond{grid-template-columns:1fr}
  .hero .wrap{gap:28px}
  .faq.faq-cols{grid-template-columns:1fr;gap:32px}
  .hero-statement{max-width:none}
  .waves{width:520px;height:520px;right:-200px;top:-200px}
  .nav{order:3;width:100%;gap:14px}
  .strip .wrap{grid-template-columns:1fr}
  .strip a,.strip a:first-child{border-left:0;border-top:1px solid var(--line);padding:16px 0}
  .strip a:first-child{border-top:0}
}
@media (max-width:640px){
  .wrap{padding:0 16px}
  body{font-size:16px}
  section{padding:52px 0}
  .plan{grid-template-columns:1fr auto;padding:18px 18px;gap:6px 16px}
  .plan .det{grid-column:1/-1;grid-row:2}
  .plan .pr{grid-row:1;grid-column:2}
  .where ul{grid-template-columns:1fr}
  .row2{grid-template-columns:1fr}
  .top .wrap{gap:8px 10px;min-height:0;padding-top:12px;padding-bottom:6px;flex-wrap:wrap}
  .brand-logo{height:30px}
  .top .wrap{padding-left:16px;padding-right:16px}
  .top .wrap{gap:8px 6px}
  .top .btn{padding:10px 9px;font-size:13px}
  .top .tel .ic{width:40px;height:40px;padding:10px}
  .top .tel span{display:none}
  .top .tel .ic{display:block}
  .nav{overflow-x:auto;white-space:nowrap;flex-wrap:nowrap;margin:0 -16px;padding:4px 16px 6px;scrollbar-width:none}
  .nav::-webkit-scrollbar{display:none}
  .nav a{padding:6px 2px;font-size:15px}
  .hero{padding:24px 0 40px}
  .hero-card{padding:6px 18px 4px}
  .req dl{grid-template-columns:1fr}
  .req dd{margin-bottom:6px}
}
"""

CSS += legal.LEGAL_CSS

# ---------- шрифты: только со своего сервера ----------
import glob, shutil
FONTS_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
def font_face():
    """Берёт из папки fonts/ переменные шрифты Golos Text и Unbounded (.woff2, .woff или .ttf).
    Если файлов нет, сайт показывает системный шрифт и ничего не грузит с чужих серверов."""
    css = ""
    fmt = {".woff2": "woff2", ".woff": "woff", ".ttf": "truetype"}
    for family, key in (("Golos Text", "golos"), ("Unbounded", "unbounded")):
        found = [p for p in sorted(glob.glob(os.path.join(FONTS_SRC, "*")))
                 if key in os.path.basename(p).lower() and os.path.splitext(p)[1].lower() in fmt]
        found.sort(key=lambda p: (list(fmt).index(os.path.splitext(p)[1].lower()), "variable" not in p.lower()))
        if not found:
            continue
        p = found[0]
        os.makedirs(os.path.join(OUT, "fonts"), exist_ok=True)
        shutil.copy(p, os.path.join(OUT, "fonts", os.path.basename(p)))
        css += ('@font-face{font-family:"%s";src:url("/fonts/%s") format("%s");font-weight:400 900;font-style:normal;font-display:swap}\n'
                % (family, os.path.basename(p), fmt[os.path.splitext(p)[1].lower()]))
    return css
FONT_FACE = font_face()

def head(title, desc, slug):
    canon = "https://badcom.ru" + ("" if slug == "index" else f"/{slug}")
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#1E3A2F">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="32x32 48x48">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:type" content="website">
<meta name="format-detection" content="telephone=no">
<style>{FONT_FACE}{CSS}</style>
</head>
<body>
<a class="skip" href="#main">Перейти к содержимому</a>
"""

def header(slug):
    pre = "" if slug == "index" else "/"
    return f"""<header class="top">
  <div class="wrap">
    <a class="mark" href="/" aria-label="Плохая Компания — на главную">{BRAND_LOGO}</a>
    <nav class="nav" aria-label="Разделы">
      <a href="{pre}#tarif">Тарифы</a>
      <a href="{pre}#zona">Где работаем</a>
      <a href="{pre}#pay">Как оплатить</a>
      <a href="{pre}#faq">Вопросы</a>
      <a href="#contacts">Контакты</a>
      <a href="{TG}" target="_blank" rel="noopener">Telegram</a>
    </nav>
    <a class="tel" href="tel:{PHONE_TEL}" aria-label="Позвонить: {PHONE}"><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg><span>{PHONE}</span></a>
    <a class="btn" href="{LK}">Личный кабинет</a>
  </div>
</header>
"""

def tabs(current):
    out = ['<nav class="tabs" aria-label="Тарифные зоны">']
    for slug, label in PAGES:
        cur = ' aria-current="page"' if slug == current else ""
        link = "/#tarif" if slug == "index" else href(slug)
        out.append(f'<a href="{link}"{cur}>{label}</a>')
    out.append("</nav>")
    return "\n".join(out)

SPEED_MAX = {"512 Кбит/с": 0.5, "1 Мбит/с": 1, "2 Мбит/с": 2, "5 Мбит/с": 5, "10 Мбит/с": 10, "до 20 Мбит/с": 20}

def unlim_table(rows):
    out = ['<div class="plans">']
    for r in rows:
        w = max(4, SPEED_MAX[r["speed"]] / 20 * 100)
        out.append(f"""<div class="plan">
  <div class="nm">{r['name']}</div>
  <div class="det">Безлимит. Скачивание и отдача — <b>{r['speed']}</b><div class="bar" aria-hidden="true"><i style="width:{w:.0f}%"></i></div></div>
  <div class="pr">{rub(r['price'])}<small>в месяц</small></div>
</div>""")
    out.append("</div>")
    return "\n".join(out)

def _num(x):
    t = f"{x:.3f}".rstrip("0").rstrip(".")
    return t.replace(".", ",")

def _dur(sec):
    sec = round(sec)
    m, c = divmod(sec, 60)
    if m and c:
        return f"{m}\u00a0мин {c}\u00a0с"
    return f"{m}\u00a0мин" if m else f"{c}\u00a0с"

def download_block(rows):
    """Пояснение: за сколько скачивается файл 100 Мбайт на каждом тарифе."""
    body = []
    for r in rows:
        sp = r["speed"]
        upto = sp.startswith("до ")
        v = sp.replace("до ", "")
        num, unit = v.split(" ", 1)
        mbit = float(num) / 1000 if unit.startswith("Кбит") else float(num)
        mbyte = mbit / 8
        sec = 800 / mbit
        a = "до " if upto else ""
        b = "от " if upto else ""
        body.append(f'<tr><th scope="row">{r["name"]}</th><td>{html.escape(v)}</td><td>{a}{_num(mbyte)}</td><td><b>{b}{_dur(sec)}</b></td></tr>')
    return f"""<div class="dl">
  <h3>За сколько скачается файл 100&nbsp;Мбайт</h3>
  <p class="muted">Скорость тарифа указана в мегабитах в секунду, а размер файлов обычно считают в мегабайтах. В одном байте 8&nbsp;бит, поэтому файл скачивается в 8 раз «медленнее», чем кажется по цифре тарифа.</p>
  <div class="dl-scroll"><table>
    <thead><tr><th>Тариф</th><th>Скорость, Мбит/с</th><th>Загрузка, Мбайт/с</th><th>Файл 100&nbsp;Мбайт*</th></tr></thead>
    <tbody>{"".join(body)}</tbody>
  </table></div>
  <p class="dl-note">* Расчёт без накладных расходов. На практике скорость делится между всеми устройствами в доме и зависит от загруженности сайта, с которого вы качаете, поэтому файл может скачиваться дольше.</p>
</div>"""

def vol_table(rows):
    out = ['<div class="plans">']
    for r in rows:
        out.append(f"""<div class="plan">
  <div class="nm">{r['name']}</div>
  <div class="det"><b>{r['volume']}</b> в месяц, скорость {r['speed']}. Сверх пакета — {r['over']} за 1 МБ.</div>
  <div class="pr">{rub(r['price'])}<small>в месяц</small></div>
</div>""")
    out.append("</div>")
    return "\n".join(out)

def surf_table(rows, turbo=True):
    out = ['<div class="plans">']
    for r in rows:
        after = r["after"]
        after_txt = "после суточного лимита — без доступа до следующих суток" if after.startswith("без") else f"после лимита — {after}"
        t = " Можно докупить «Турбо»." if turbo else ""
        out.append(f"""<div class="plan">
  <div class="nm">{r['name']}</div>
  <div class="det"><b>{r['day']} в сутки</b> ({r['month']} в месяц), скорость {r['speed']}; {after_txt}.{t}</div>
  <div class="pr">{rub(r['price'])}<small>в месяц</small></div>
</div>""")
    out.append("</div>")
    return "\n".join(out)

def turbo_table():
    out = ['<div class="plans">']
    for n, p, d in TURBO:
        out.append(f"""<div class="plan">
  <div class="nm">{n}</div>
  <div class="det">{d}</div>
  <div class="pr">{rub(p)}<small>разово</small></div>
</div>""")
    out.append("</div>")
    return "\n".join(out)

COND_PRIVATE = f"""<div class="cond">
  <div class="note">
    <h3>Подключение</h3>
    <div class="price-big">{rub(10000)}</div>
    <p>Оплачивается нашему установщику при подключении. Из них 1000 ₽ сразу зачисляем на ваш баланс — фактически подключение стоит 9000 ₽.</p>
  </div>
  <div class="note">
    <h3>Оборудование</h3>
    <p>Антенну на фасад дома и Wi‑Fi роутер выдаём бесплатно на всё время, пока вы пользуетесь нашим интернетом.</p>
    <p>Если абонент больше трёх месяцев подряд не пользуется нашей связью, мы вправе забрать оборудование.</p>
    <p>Если откажетесь от услуги, оборудование нужно вернуть. Если вернуть невозможно — оплатить его стоимость, 16&nbsp;500 ₽.</p>
  </div>
</div>"""

COND_BIZ_RADIO = f"""<div class="cond">
  <div class="note">
    <h3>Подключение</h3>
    <div class="price-big">{rub(10000)}</div>
    <p>Это стоимость монтажа. Само оборудование — антенну и Wi‑Fi роутер — передаём в безвозмездное пользование на всё время обслуживания. При отказе от услуги оборудование нужно вернуть.</p>
  </div>
  <div class="note">
    <h3>Оплата по счёту</h3>
    <p>Для ООО и ИП действует постоплата: счёт за месяц приходит в начале следующего месяца.</p>
  </div>
</div>
<div class="callout"><p>В сёлах с тарифами «<a href="/tariff_zone2">х2</a>» и «<a href="/tariff_sputnik_biz">Спутник</a>» цену для юрлиц считаем индивидуально — она зависит от удалённости и сложности подключения.</p></div>"""

COND_BIZ_SAT = f"""<div class="cond">
  <div class="note">
    <h3>Подключение</h3>
    <div class="price-big">{rub(10000)}</div>
    <p>Это стоимость оборудования, которое мы устанавливаем. Монтаж — бесплатно.</p>
  </div>
  <div class="note">
    <h3>Оплата по счёту</h3>
    <p>Для ООО и ИП действует постоплата: счёт за месяц приходит в начале следующего месяца.</p>
  </div>
</div>"""

def apply_form(source):
    import json
    settle_json = json.dumps({d: [{"n": s["n"], "t": s["t"], "x": s["x"]} for s in v] for d, v in SETTLEMENTS.items()}, ensure_ascii=False)
    opts = "".join(f"<option>{d} район</option>" for d in DISTRICTS)
    return f"""<section class="apply" id="form">
  <div class="wrap">
    <div>
      <h2>Заявка на подключение</h2>
      <p class="muted" style="margin-top:14px">Напишите, где нужен интернет. Перезвоним, расскажем, какой тариф действует в вашем селе, и договоримся о выезде монтажников.</p>
      <p class="direct">Удобнее голосом — звоните <a href="tel:{PHONE_TEL}">{PHONE}</a></p>
    </div>
    <form name="zayavka" method="POST" action="/api/zayavka">
      <input type="hidden" name="page" value="{source}">
      <p class="hp"><label>Не заполняйте <input name="company_site"></label></p>
      <div class="row2">
        <div><label for="f-name">Как к вам обращаться</label><input id="f-name" name="name" autocomplete="name" required></div>
        <div><label for="f-tel">Телефон</label><input id="f-tel" name="phone" type="tel" autocomplete="tel" inputmode="tel" required placeholder="+7"></div>
      </div>
      <label for="f-dist">Район</label>
      <select id="f-dist" name="district"><option value="">Выберите район</option>{opts}<option>Другой</option></select>
      <div id="settle-box" hidden>
        <label for="f-settle">Населённый пункт</label>
        <select id="f-settle" name="settlement"></select>
        <p class="settle-hint muted" id="settle-hint" aria-live="polite"></p>
      </div>
      <label for="f-addr">Адрес</label>
      <input id="f-addr" name="address" required placeholder="Улица и дом. Если вашего села нет в списке, напишите и его">
      <label for="f-who">Кого подключаем</label>
      <select id="f-who" name="client"><option>Частный дом</option><option>Организацию (ООО, ИП)</option></select>
      <label for="f-msg">Комментарий</label>
      <textarea id="f-msg" name="message" placeholder="Необязательно"></textarea>
      <input type="hidden" name="consent_doc" value="/consent, редакция {legal.CONSENT_VERSION}">
      <input type="hidden" name="consent_time" value="">
      <label class="consent"><input type="checkbox" name="consent" required> <span>Даю <a href="/consent" target="_blank" rel="noopener">согласие на обработку персональных данных</a> для рассмотрения заявки. Ознакомлен(а) с <a href="/privacy" target="_blank" rel="noopener">Политикой обработки персональных данных</a></span></label>
      <p style="margin:18px 0 0"><button class="btn" type="submit">Отправить заявку</button></p>
    </form>
  </div>
  <script>
  (function(){{
    var DATA={settle_json};
    var dist=document.getElementById('f-dist'), box=document.getElementById('settle-box'),
        sel=document.getElementById('f-settle'), hint=document.getElementById('settle-hint');
    if(!dist||!sel)return;
    function fill(){{
      var d=dist.value.replace(/ район$/,''), list=DATA[d];
      hint.innerHTML='';
      if(!list){{box.hidden=true;sel.innerHTML='';return;}}
      var h='<option value="">Выберите населённый пункт ('+list.length+')</option>';
      list.forEach(function(s,i){{h+='<option value="'+i+'">'+s.n+(s.t?', '+s.t:'')+'</option>';}});
      h+='<option value="other">Моего населённого пункта нет в списке</option>';
      sel.innerHTML=h;box.hidden=false;
    }}
    function show(){{
      var d=dist.value.replace(/ район$/,''), list=DATA[d]||[], v=sel.value;
      if(v==='other'){{hint.textContent='Оставьте заявку, мы проверим возможность подключения у вас. Название села напишите в поле «Адрес».';return;}}
      var s=list[Number(v)];
      if(v===''||!s){{hint.textContent='';return;}}
      if(s.x==='Спутник')hint.innerHTML='Здесь подключаем по <a href="/tariff_sputnik">тарифам «Спутник»</a>.';
      else if(s.x==='х2')hint.innerHTML='Здесь действуют <a href="/tariff_zone2">тарифы «х2»</a>.';
      else hint.textContent='';
    }}
    dist.addEventListener('change',fill);sel.addEventListener('change',show);fill();
  }})();
  </script>
</section>
"""

CONTACTS = f"""<section class="contacts" id="contacts">
  <div class="wrap">
    <div class="note">
      <h2 style="font-size:28px;margin-bottom:18px">Контакты</h2>
      <p><b>Телефон:</b> <a href="tel:{PHONE_TEL}">{PHONE}</a><br>
         <b>Почта:</b> <a href="mailto:{EMAIL}">{EMAIL}</a><br>
         <b>Офис:</b> Иркутск, ул. Лермонтова, 134/1, 4 этаж</p>
      <h3 style="margin:22px 0 8px">Техподдержка</h3>
      <p>Телефон: <a href="tel:{PHONE_TEL}">{PHONE}</a><br>
         Telegram и MAX: <a href="tel:{SUPPORT_TEL}">{SUPPORT}</a></p>
      <p class="hours">Будни 8:00–22:00, выходные 9:00–22:00 по иркутскому времени.</p>
      <div class="callout"><p>Интернет пропал сразу после полуночи? Проверьте баланс в <a href="{LK}">личном кабинете</a> — скорее всего, он закончился.</p></div>
    </div>
    <div class="note">
      <h2 style="font-size:28px;margin-bottom:18px">Документы</h2>
      <ul class="docs">
        <li><b class="doc">Лицензия на телематические услуги связи</b><span>№ Л030-00114-77/00061756 (до 01.03.2022 — № 159794). Выдана Роскомнадзором 31.10.2017, действует до 31.10.2027. Лицензиат — ИП Малов Д.С. Территория действия: Российская Федерация. Выписка из реестра от 17.11.2026: действующая.</span></li>
        <li><b class="doc">Лицензия на услуги передачи данных</b><span>№ Л030-00114-77/00073373 (до 01.03.2022 — № 177512). Выдана Роскомнадзором 02.10.2019, действует до 02.10.2029. Лицензиат — ИП Малов Д.С. Территория действия: Российская Федерация. Выписка из реестра от 17.11.2026: действующая.</span></li>
        <li><a href="https://rkn.gov.ru/communication/register/license/" target="_blank" rel="noopener">Реестр лицензий в области связи</a><span>Проверить сведения о лицензиях на сайте Роскомнадзора</span></li>
        <li><a href="/privacy">Политика обработки персональных данных</a><span>Редакция от {legal.REV_DATE}</span></li>
        <li><a href="/consent">Согласие на обработку персональных данных</a><span>Для заявок с сайта</span></li>
        <li><a href="/cookies">Политика использования файлов cookie</a><span>Какие cookie использует сайт и как ими управлять</span></li>
      </ul>
      <details class="req">
        <summary>Реквизиты</summary>
        <dl>
          <dt>Полное название</dt><dd>Индивидуальный предприниматель Малов Дмитрий Сергеевич</dd>
          <dt>ОГРНИП</dt><dd>307381107900070</dd>
          <dt>ИНН</dt><dd>381100000076</dd>
          <dt>Юридический адрес</dt><dd>664023, г. Иркутск, ул. Ядринцева, д. 5, кв. 11</dd>
          <dt>Фактический адрес</dt><dd>664033, г. Иркутск, ул. Лермонтова, д. 134/1, 4 этаж</dd>
          <dt>Почтовый адрес</dt><dd>664033, г. Иркутск, а/я 4</dd>
          <dt>Банк</dt><dd>Филиал «Новосибирский» АО «АЛЬФА-БАНК», г. Новосибирск</dd>
          <dt>Расчётный счёт</dt><dd>40802810823080000518</dd>
          <dt>Корр. счёт</dt><dd>30101810600000000774</dd>
          <dt>БИК</dt><dd>045004774</dd>
          <dt>Реестр операторов ПДн</dt><dd>38-22-008580 (приказ Роскомнадзора № 156 от 30.09.2022)</dd>
        </dl>
      </details>
    </div>
  </div>
</section>
"""

FOOTER = f"""<footer>
  <div class="wrap">
    <span>© ИП Малов Д.С., «Плохая Компания», Иркутск</span>
    <span><a href="{LK}">Личный кабинет</a> &nbsp; <a href="{TG}" target="_blank" rel="noopener">Telegram</a> &nbsp; <a href="{MAX_NEWS}" target="_blank" rel="noopener">MAX</a> &nbsp; <a href="https://yandex.ru/internet/" target="_blank" rel="noopener">Проверить скорость</a></span>
    <span><a href="/privacy">Политика обработки персональных данных</a> &nbsp; <a href="/consent">Согласие на обработку ПДн</a> &nbsp; <a href="/cookies">Файлы cookie</a> &nbsp; <button class="linkbtn" type="button" data-ck-open>Настройки cookie</button></span>
  </div>
</footer>
""" + legal.COOKIE_BANNER + """</body>
</html>
"""

def waves_svg():
    rings = "".join(f'<circle cx="380" cy="380" r="{r}"/>' for r in range(60, 400, 52))
    pulses = "".join(f'<circle class="pulse" cx="380" cy="380" r="{r}"/>' for r in (112, 216, 320))
    return f'<svg class="waves" viewBox="0 0 760 760" aria-hidden="true">{rings}{pulses}<circle cx="380" cy="380" r="7" fill="#F2B705" stroke="none"/></svg>'

# ---------- главная ----------
def faq():
    items = [
        ("Как оставить заявку на подключение?",
         f'<p>Заполните <a href="#form">форму внизу страницы</a> или позвоните по телефону <a href="tel:{PHONE_TEL}">{PHONE}</a>. Мы перезвоним, уточним адрес и расскажем, какой тариф действует в вашем населённом пункте.</p>'),
        ("Почему такое название — «Плохая Компания»?",
         '<p>Потому что нашему руководителю это название показалось запоминающимся и вызывающим улыбку. Если вы улыбнулись, это здорово! А вообще мы делаем хорошую и качественную связь и никогда не бросаем своих абонентов в беде.</p>'),
        ("Сколько стоит подключить интернет домой?",
         '<p>Подключение стоит 10 000 ₽. Вы оплачиваете их нашему установщику при подключении, и 1000 ₽ из них сразу зачисляется на ваш баланс. Антенну на фасад и роутер мы предоставляем бесплатно на всё время, пока вы пользуетесь нашей связью.</p>'
         '<p>Если вы больше трёх месяцев подряд не пользуетесь нашей связью, мы вправе забрать оборудование. При отказе от услуг оборудование нужно вернуть или выкупить, стоимость выкупа указана в договоре безвозмездного пользования оборудованием.</p>'),
        ("Какие тарифы на интернет?",
         '<p>В большинстве сёл действуют <a href="#tarif">базовые безлимитные тарифы</a> от 700 ₽ в месяц. В особо удалённых местах — тарифы <a href="/tariff_zone2">«х2»</a> или <a href="/tariff_sputnik">«Спутник»</a>. Для организаций — <a href="/tariff_biz">отдельные тарифы</a>.</p>'),
        ("Как списывается абонентская плата?",
         '<p>Абонентская плата списывается <b>посуточно</b>. Например, у вас тариф «5 Мегабит» за 1350 ₽, а в месяце 30 дней. Каждый день с баланса списывается 1/30 часть, то есть 45 ₽ за сутки.</p>'
         '<p>Пополнять баланс сразу на всю сумму тарифа не обязательно, можно оплачивать частями в течение месяца. Например, в пятницу положить 135 ₽ (45 ₽ × 3) и пользоваться интернетом все выходные.</p>'
         '<p>Когда деньги на балансе заканчиваются, доступ в интернет автоматически блокируется. Если интернет пропал сразу после полуночи, проверьте баланс: скорее всего, он закончился.</p>'),
        ("Как обстоит дело со скоростью интернета?",
         '<p>Скорость на скачивание и отдачу одинаковая и соответствует тарифу. В отличие от мобильного интернета, скорость которого может сильно падать вечером и при большой нагрузке на базовую станцию, наша скорость стабильна. Мы следим, чтобы абонент получал скорость не ниже той, что указана в тарифе, и мог спокойно смотреть видео без «тормозов».</p>'
         '<p>Проверить скорость можно на <a href="https://yandex.ru/internet/" target="_blank" rel="noopener">yandex.ru/internet</a>: откройте страницу и нажмите жёлтую кнопку «Измерить».</p>'),
        ("Как оплатить интернет?",
         f'<p>Оплатить можно банковской картой в <a href="{LK}">личном кабинете</a>, через приложение «Сбербанк Онлайн», в отделении Почты России или в отделении вашего банка. Вместе с оборудованием мы передаём абоненту подробную инструкцию по оплате.</p>'
         f'<p>Как пополнить баланс картой через личный кабинет:</p>'
         f'<ol><li>В правом нижнем углу бумажного договора напечатаны две группы цифр: это логин и пароль от личного кабинета.</li>'
         f'<li>Откройте <a href="{LK}">lk.badcom.ru</a> и введите логин и пароль.</li>'
         f'<li>Выберите раздел «Баланс» и нажмите «Пополнить счёт».</li>'
         f'<li>Выберите Visa, MasterCard или МИР, введите номер мобильного телефона (электронная почта не обязательна) и сумму. Минимальная сумма пополнения — 50 ₽.</li>'
         f'<li>Нажмите «Пополнить», подтвердите кнопкой «Да», введите данные карты на странице оплаты. Готово, баланс пополнен.</li></ol>'),
        ("Как выбрать первый тариф?",
         '<p>Ориентируйтесь на то, как вы пользуетесь интернетом:</p>'
         '<ul><li><b>512/512</b> — минимум: текстовые сообщения в Viber и WhatsApp.</li>'
         '<li><b>1 Мегабит</b> — одно устройство и спокойное пользование интернетом.</li>'
         '<li><b>2 Мегабита</b> — одно устройство с комфортным видео, страницами, картинками и звонками в мессенджерах. Или 2–3 устройства, которые не работают одновременно и не нагружены.</li>'
         '<li><b>5 Мегабит</b> — комфортная работа с 2–3 устройств одновременно и онлайн-игры.</li>'
         '<li><b>10 Мегабит</b> — максимальный комфорт для 3–4 устройств.</li></ul>'
         '<p>Мы используем технологию <b>BURST</b> («вспышка»). Если средняя нагрузка со стороны абонента небольшая, он получает скорость следующего тарифа: 2 Мегабита вместо 1, 5 вместо 2 и так далее. Если нагрузка на канал большая, скорость будет по вашему тарифу, но не ниже его.</p>'
         '<p>Тариф можно поменять самостоятельно в личном кабинете один раз в месяц, 1 числа. Чаще — по запросу в техподдержку, сколько угодно раз в течение месяца.</p>'),
        ("Как связаться с техподдержкой?",
         f'<p>Звоните на <a href="tel:{PHONE_TEL}">{PHONE}</a> или пишите в Telegram и MAX на <a href="tel:{SUPPORT_TEL}">{SUPPORT}</a>. Работаем в будни с 8:00 до 22:00, в выходные с 9:00 до 22:00 по Иркутску.</p>'),
    ]
    new_prefix = ("Как оставить заявку", "Сколько стоит подключить", "Какие тарифы", "Как выбрать первый", "Почему такое название")
    cols = {"new": [], "old": []}
    for q, a in items:
        did = ' id="pay"' if q.startswith("Как оплатить") else ""
        cols["new" if q.startswith(new_prefix) else "old"].append(
            f"<details{did}><summary>{q}</summary><div class=\"a\">{a}</div></details>")
    assert len(cols["new"]) == len(new_prefix) and len(cols["old"]) == len(items) - len(new_prefix)
    return ('<div class="faq-col"><h3>Хотите подключиться?</h3>' + "\n".join(cols["new"]) + '</div>'
            '<div class="faq-col"><h3>Уже подключены?</h3>' + "\n".join(cols["old"]) + '</div>')

MONTHS = {m: i for i, m in enumerate("января февраля марта апреля мая июня июля августа сентября октября ноября декабря".split(), 1)}
def load_reviews():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "reviews.txt")
    res = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        a, s, d, r, t = [p.strip() for p in line.split("|", 4)]
        dd, mm, yy = d.split()
        res.append({"a": a, "s": s, "d": d, "r": int(r), "t": t, "k": (int(yy), MONTHS[mm], int(dd))})
    res.sort(key=lambda x: x["k"], reverse=True)
    return res
REVIEWS = load_reviews()
# Рейтинги на карточках организаций на 17.11.2026 (обновляются вручную)
REVIEW_RATINGS = [("Яндекс Карты", "4,8", "78 оценок", "yandex"), ("2ГИС", "4,9", "102 оценки", "2gis")]
REVIEWS_AS_OF = "17 ноября 2026 г."
REVIEW_LINKS = {
    "yandex": "https://yandex.ru/maps/org/plokhaya_kompaniya/43187634695/reviews/",
    "2gis": "https://2gis.ru/irkutsk/firm/70000001036377445/tab/reviews",
}

def stars(n):
    return f'<span class="stars" role="img" aria-label="Оценка {n} из 5">' + "★" * n + '<i>' + "★" * (5 - n) + '</i></span>'

def reviews_html(items):
    out = []
    for x in items:
        out.append(
            f'<figure class="rvc"><div class="rv-top">{stars(x["r"])}<span class="rv-date">{html.escape(x["d"])}</span></div>'
            f'<blockquote>{html.escape(x["t"])}</blockquote>'
            f'<figcaption>{html.escape(x["a"])} <span class="rv-src">· {html.escape(x["s"])}</span></figcaption></figure>')
    return "".join(out)

def rating_badges():
    items = "".join(
        f'<a class="rb" href="{REVIEW_LINKS[k]}" target="_blank" rel="noopener noreferrer"><b>{r}</b><span>★</span><small>{html.escape(n)}, {c}</small></a>'
        for n, r, c, k in REVIEW_RATINGS)
    return f'<div class="rb-row">{items}<small class="rb-asof">по данным карточек на {REVIEWS_AS_OF}</small></div>'


def index_page():
    import json as _json
    dist = "".join(f'<li><button type="button" class="dbtn" data-d="{d}" aria-expanded="false" aria-controls="wl-panel">{d}</button></li>' for d in DISTRICTS)
    dist_static = "".join(
        f'<details><summary>{d} район ({len(SETTLEMENTS[d])})</summary><p>' + ", ".join(html.escape(s["n"]) for s in SETTLEMENTS[d]) + '</p></details>'
        for d in DISTRICTS)
    zona_json = _json.dumps({d: [{"n": s["n"], "t": s["t"], "x": s["x"]} for s in v] for d, v in SETTLEMENTS.items()}, ensure_ascii=False)
    rv = reviews_html(REVIEWS[:6])
    body = f"""{header('index')}
<main id="main">
<section class="hero">
  {waves_svg()}
  <div class="wrap">
    <div class="hero-main">
      <h1 class="sr">Плохая Компания — интернет в сёла и посёлки Иркутской области</h1>
      <p class="hero-statement">Интернет в малые и таёжные сёла Иркутской области</p>
      <p class="lede">Работаем там, где сотовая связь слабая или её нет совсем. Наша цель — снизить цифровое неравенство и сделать жизнь в небольших сёлах удобнее.</p>
      <div class="actions">
        <a class="btn" href="#form">Оставить заявку</a>
        <a class="btn ghost" href="#tarif">Посмотреть тарифы</a>
      </div>
    </div>
    <div class="hero-side">
      <aside class="hero-card" aria-label="Для абонентов">
        <h2>Уже подключены?</h2>
        <a class="hc" href="#contacts"><b>{PHONE}</b><span>Техподдержка: будни 8:00–22:00, выходные 9:00–22:00</span><i>→</i></a>
        <a class="hc" href="#pay"><b>Как пополнить баланс</b><span>Картой в кабинете, Сбербанк Онлайн, почта, банк</span><i>→</i></a>
        <a class="hc" href="{MAX_NEWS}" target="_blank" rel="noopener"><b>Работы на линии</b><span>Новости и объявления в MAX</span><i>→</i></a>
      </aside>
    </div>
  </div>
</section>

<section class="zona" id="zona" aria-labelledby="zona-h">
  <div class="wrap">
  <div class="where">
      <h2 id="zona-h">Где мы работаем</h2>
      <p>Подключаем в населённых пунктах этих районов. Нажмите на район, чтобы увидеть список. Не нашли свой — всё равно оставьте заявку, проверим.</p>
      <ul class="dlist" hidden>{dist}</ul>
      <div class="wl" id="wl-panel" hidden aria-live="polite"></div>
      <noscript><div class="wl-static">{dist_static}</div></noscript>
      <script>
      (function(){{
        var DATA={zona_json}, ul=document.querySelector('.where .dlist'), panel=document.getElementById('wl-panel');
        if(!ul||!panel)return; ul.hidden=false;
        function esc(s){{return s.replace(/&/g,'&amp;').replace(/</g,'&lt;');}}
        function close(){{panel.hidden=true;panel.innerHTML='';ul.querySelectorAll('.dbtn').forEach(function(b){{b.setAttribute('aria-expanded','false');b.classList.remove('on');}});}}
        ul.addEventListener('click',function(e){{
          var btn=e.target.closest('.dbtn'); if(!btn)return;
          var d=btn.getAttribute('data-d'), was=btn.getAttribute('aria-expanded')==='true';
          close(); if(was)return;
          btn.setAttribute('aria-expanded','true'); btn.classList.add('on');
          var list=DATA[d]||[], h='<h3>'+d+' район: '+list.length+' '+(list.length%10===1&&list.length%100!==11?'населённый пункт':(list.length%10>=2&&list.length%10<=4&&(list.length%100<10||list.length%100>=20)?'населённых пункта':'населённых пунктов'))+'</h3><ul>';
          list.forEach(function(s){{h+='<li>'+esc(s.n)+(s.t?' <small>'+esc(s.t)+'</small>':'')+(s.x==='Спутник'?' <a href="/tariff_sputnik">Спутник</a>':(s.x==='х2'?' <a href="/tariff_zone2">х2</a>':''))+'</li>';}});
          h+='</ul><a class="btn sm" href="#form" data-pick="'+d+'">Оставить заявку в этом районе</a><button type="button" class="wl-close">Закрыть</button>';
          panel.innerHTML=h; panel.hidden=false;
        }});
        panel.addEventListener('click',function(e){{
          if(e.target.closest('.wl-close')){{close();return;}}
          var a=e.target.closest('[data-pick]'); if(!a)return;
          var sel=document.getElementById('f-dist'); if(!sel)return;
          sel.value=a.getAttribute('data-pick')+' район'; sel.dispatchEvent(new Event('change'));
        }});
      }})();
      </script>
  </div>
  </div>
</section>

<section id="tarif">
  <div class="wrap">
    <div class="sec-head">
      <div><h2>Тарифы</h2><p>Полный безлимит, одинаковая скорость на скачивание и отдачу.</p></div>
    </div>
    {tabs('index')}
    {unlim_table(BASE)}
    {download_block(BASE)}
    {COND_PRIVATE}
    <div class="callout"><p>В особо удалённых сёлах действуют тарифы <a href="/tariff_zone2">«х2»</a> или <a href="/tariff_sputnik">«Спутник»</a>. Перед подключением уточните у нас, какой тариф работает в вашем населённом пункте.</p></div>
  </div>
</section>

<section id="faq" style="padding-top:0">
  <div class="wrap">
    <h2 style="margin-bottom:24px">Вопросы и ответы</h2>
    <div class="faq faq-cols">{faq()}</div>
  </div>
  <script>
  (function(){{
    function openPay(){{var d=document.getElementById('pay');if(d&&location.hash==='#pay'){{d.open=true;}}}}
    openPay();window.addEventListener('hashchange',openPay);
    document.addEventListener('click',function(e){{var a=e.target.closest('a[href="#pay"],a[href="/#pay"]');if(a){{var d=document.getElementById('pay');if(d)d.open=true;}}}});
  }})();
  </script>
</section>

<section class="reviews" id="otzyvy">
  <div class="wrap">
    <h2>Что говорят абоненты</h2>
    {rating_badges()}
    <div class="rv">{rv}</div>
    <div class="rv-links">
      <a class="btn" href="/reviews">Все отзывы ({len(REVIEWS)})</a>
      <p>Оставить свой отзыв можно на картах:</p>
      <a class="btn ghost" href="{REVIEW_LINKS['yandex']}" target="_blank" rel="noopener noreferrer">Отзывы на Яндекс Картах</a>
      <a class="btn ghost" href="{REVIEW_LINKS['2gis']}" target="_blank" rel="noopener noreferrer">Отзывы в 2ГИС</a>
    </div>
  </div>
</section>

{apply_form('Главная')}
{CONTACTS}
</main>
{FOOTER}"""
    title = "Плохая Компания — беспроводной интернет в сёлах Иркутской области"
    desc = "Интернет-провайдер для удалённых и небольших населённых пунктов Иркутской области. Безлимитные тарифы от 700 ₽ в месяц."
    return head(title, desc, "index") + body

def tariff_page(slug, h1, sub, content, title, form_src):
    body = f"""{header(slug)}
<main id="main">
<div class="phead"><div class="wrap"><h1>{h1}</h1><p>{sub}</p></div></div>
<section>
  <div class="wrap">
    {tabs(slug)}
    {content}
  </div>
</section>
{apply_form(form_src)}
{CONTACTS}
</main>
{FOOTER}"""
    desc = "Плохая Компания — беспроводной интернет в сёлах Иркутской области. " + sub
    return head(title, desc, slug) + body

pages = {
    "index": index_page(),
    "tariff_zone2": tariff_page(
        "tariff_zone2", "Тарифная зона «х2»",
        "Для особо удалённых сёл. Полный безлимит, скорость одинаковая в обе стороны.",
        unlim_table(X2) + download_block(X2) + COND_PRIVATE,
        "Тарифная зона «х2» — Плохая Компания", "Зона х2"),
    "tariff_sputnik": tariff_page(
        "tariff_sputnik", "Тарифная зона «Спутник»",
        "Интернет через спутник там, где нет других каналов. Тарифы с пакетом трафика на месяц или на сутки.",
        '<h3 class="plans-cap" style="margin-top:0">Пакет на месяц</h3>' + vol_table(SAT_VOL)
        + '<h3 class="plans-cap">Пакет на сутки — «Серфинг»</h3>' + surf_table(SAT_SURF)
        + '<h3 class="plans-cap">Опции «Турбо»</h3><p class="muted">Докупаются к любому тарифу, когда трафик закончился.</p>' + turbo_table()
        + COND_PRIVATE,
        "Тарифная зона «Спутник» — Плохая Компания", "Спутник"),
    "tariff_biz": tariff_page(
        "tariff_biz", "Тарифы для юрлиц",
        "Для ООО и ИП. Полный безлимит, постоплата по счёту.",
        unlim_table(BIZ) + download_block(BIZ) + COND_BIZ_RADIO,
        "Тарифы для юридических лиц — Плохая Компания", "Юрлица"),
    "tariff_sputnik_biz": tariff_page(
        "tariff_sputnik_biz", "«Спутник» для юрлиц",
        "Спутниковый интернет для ООО и ИП. Пакеты трафика на месяц или на сутки, постоплата по счёту.",
        '<h3 class="plans-cap" style="margin-top:0">Пакет на месяц</h3>' + vol_table(SATB_VOL)
        + '<h3 class="plans-cap">Пакет на сутки — «Серфинг»</h3>' + surf_table(SATB_SURF, turbo=False)
        + COND_BIZ_SAT,
        "Тарифная зона «Спутник» для юридических лиц — Плохая Компания", "Спутник юрлица"),
}

THANKS = head("Заявка отправлена — Плохая Компания", "Заявка на подключение отправлена.", "spasibo") + header("spasibo") + f"""
<main id="main">
<div class="phead"><div class="wrap"><h1>Заявка отправлена</h1><p>Перезвоним в рабочее время: будни 8:00–22:00, выходные 9:00–22:00 по Иркутску.</p></div></div>
<section><div class="wrap"><p>Если вопрос срочный — звоните <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p><p><a class="btn" href="/">На главную</a></p></div></section>
<span id="contacts"></span>
</main>
{FOOTER}"""

def legal_page(slug, h1, sub, content):
    body = f"""{header(slug)}
<main id="main">
<div class="phead"><div class="wrap"><h1>{h1}</h1><p>{sub}</p></div></div>
<section><div class="wrap">{content}</div></section>
{CONTACTS}
</main>
{FOOTER}"""
    return head(h1 + " — Плохая Компания", sub, slug) + body

def reviews_page():
    total = len(REVIEWS)
    low = sum(1 for x in REVIEWS if x["r"] <= 3)
    content = f"""<div class="rvp">{rating_badges()}
<p>Здесь собраны отзывы с карточек «Плохой Компании» на Яндекс Картах и в 2ГИС — {total} шт., в том числе критические ({low}). Тексты приведены без ответов компании, в них исправлены орфография и пунктуация, имена сокращены. Актуальные отзывы и ответы компании — на самих картах, там же можно оставить свой.</p>
<div class="rv rv-page">{reviews_html(REVIEWS)}</div>
<div class="rv-links"><a class="btn ghost dark" href="{REVIEW_LINKS['yandex']}" target="_blank" rel="noopener noreferrer">Отзывы на Яндекс Картах</a>
<a class="btn ghost dark" href="{REVIEW_LINKS['2gis']}" target="_blank" rel="noopener noreferrer">Отзывы в 2ГИС</a></div></div>"""
    return legal_page("reviews", "Отзывы абонентов", "Отзывы с Яндекс Карт и 2ГИС", content)

pages["reviews"] = reviews_page()

for slug, (h1, sub, content) in legal.build_pages(dict(PHONE=PHONE, EMAIL=EMAIL, LK=LK)).items():
    pages[slug] = legal_page(slug, h1, sub, content)

for slug, content in pages.items():
    with open(os.path.join(OUT, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(content)
with open(os.path.join(OUT, "spasibo.html"), "w", encoding="utf-8") as f:
    f.write(THANKS)
print("ok", sorted(os.listdir(OUT)))
