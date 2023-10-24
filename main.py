from itertools import islice

import instaloader

def infoPerfil(username, password):

        bot = instaloader.Instaloader()
        bot.login(username,password)

        profile = instaloader.Profile.from_username(bot.context, username)

        seguidores = profile.followers
        seguindo = profile.followees
        totalPosts = profile.mediacount

        print(seguidores,seguindo,totalPosts)

        listPosts = list()
        posts = set(islice(profile.get_posts(), 20))

        for post in posts:
            dictPost = dict()

            dictPost['url'] = post.url
            dictPost['caption'] = post.caption
            dictPost['likes'] = post.get_likes()

            listPosts.append(dictPost)
        
        dictProfile = dict()

        dictProfile['seguidores'] = seguidores
        dictProfile['seguindo'] = seguindo
        dictProfile['totalPosts'] = totalPosts
        dictProfile['listPosts'] = listPosts

        return dictProfile

username = ''
password = ''

perfil = infoPerfil(username,password)

# print(perfil)