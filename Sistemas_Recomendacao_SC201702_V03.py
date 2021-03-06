# -*- coding: utf-8 -*-
"""
Trabalho de Sistemas Colaborativos
Turma 2017-02 

Este é um arquivo de script temporário.
"""
#importação da biblioteca para tratar linguagem natural
import nltk

#importação da biblioteca para cálculo da frequência das palavras 
from nltk import FreqDist

#importação da biblioteca stopwords
from nltk.corpus import stopwords

#importacao da biblioteca estatistica
from statistics import mean

#importação da biblioteca  WordNetLemmatizer para extrair
#a forma não flexionada (canônica ou lemma) de cada palavra
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
lem = WordNetLemmatizer()

#Carregando as stopwords
stop_words = set(stopwords.words('english'))

#instanciando os resumos/produtos de cada artigo
p01 = 'Many methods, models and standards for software process improvement have been developed. However, despite the efforts, they still come up against difficulties in their deployment and the processes are not institutionalized. There is a set of factors that influence the successful deployment of new or modified processes. In this paper we describe the methodology and results from a systematic review of critical success factors in software process improvement and deployment. A total of 28 primary studies were analyzed as a result of the systematic review. Some of the top factors for process improvement and process deployment initiatives are: commitment, alignment with the business strategy and goals, training, communication, resources, skills, improvement management and staff involvement. The obtained results show that is important to take into account organizational, technical and people issues in order to achieve success in improvement initiatives.' 

p02 = 'Large companies like Ericsson increasingly often adopt the principles of Agile and Lean software development and develop large software products in iterative manner – in order to quickly respond to customer needs. In this paper we present the main indicator which is sufficient for a mature software development organization in order to predict the time in weeks to release the product. In our research project we collaborated closely with a large Agile+Lean software development project at Ericsson in Sweden. This large and mature software development project and organization has found this main indicator – release readiness – to be so important that it was used as a key performance indicator and is used in controlling the development of the product and improving organizational performance. The indicator was developed and validated in an action research project at one of the units of Ericsson AB in Sweden in one of its largest projects.'

p03 = 'Research in information systems has rapidly expanded during its relatively brief existence. IT offers organizations a fundamental decision-enhancing environment that extends new opportunities, therefore producing thriving, competitive firms, adding business value and offering valuable products and services to customers. Research within the IT domain has produced several new theories, some of which have been used to help explain and predict end-user use of technologies. We provide a comprehensive overview of the major IT theories and review their theoretical fundamentals'

p04 = 'Within socially driven software development methodologies like Tropos, a new software system could be modeled as a set of collaborating actors pursuing collective and individual goals. These actors could possibly be structured around an organizational pattern. The organizational model could then, within the design of the system, be mapped to the software behavior through the use of logical agents. This paper overviews a set of human organizational styles from organization theory literature and applied here in an original manner to the representation of collaborative learning software systems. The structure-in-5 is indeed applied to a Learning Management System development and the joint venture to a Massive Open Online Course one. Being by nature a network of social interactions, collaborative learning systems are perfectly adequate for agent-oriented software development. Besides, the two above-mentioned organization styles are further represented using the i* modeling language and a formal specification language. A set of non-functional requirements is also identified and these organizational styles are further evaluated in the light of these.'

p05 = 'The general public and politics discuss electric vehicles (EVs) as promising means for achieving clean, carbon-free, and sustainable individual transportation. However, an insufficient charging infrastructure hampers a rapid diffusion of EVs. At the same time, investors have refrained from developing an EV-charging infrastructure on a large scale because of the limited demand for EVs. Against this backdrop, peer-to-peer (P2P) sharing and collaborative consumption (SCC) is a promising strategy with which to address this problem. This article describes the concept of an IT-based P2P SCC service and the research activities needed for its design. We do so by introducing a novel application of the sharing economy. Our primary contribution is to take a step toward finding a solution for a problem in the EV domain that is relevant for society. A second contribution lies in the introduction and discussion of predominantly infrastructure-creating (PIC) P2P SCC services and their characteristics.'

p06 = 'This paper presents a comparative study of three different methods for usability evaluation in Web mobile application: Heuristic Evaluation, Cognitive Walkthrough, and Web Design Perspectives-based Usability Evaluation (WDP). This research aims to evaluate which method presents the best performance on the usability evaluation of web applications for mobile devices. The study was conducted as a class activity for students of Human-Computer Interaction (HCI). The obtained results are very important to help the development of a specific technology that focus on the usability evaluation of mobile applications with the best cost/benefit ratio.'

p07 = 'It is not easy to convince an organization to change its development paradigm to adopt agile methodologies. It necessary planning and execution of coordinate actions. This paper presents a software process improvement initiative regarding the adoption of agile practices on the software development team of a telecom organization. The results include the approximation of the technical and business areas, improvement of communication and activities management, optimization of work capacity, reduction of aversion to change, and management support to deploy process improvement.'

p08 = 'E-government is being promoted by international agencies and G8 nations as a means to obtain efficiency, accountability and transparency in the governance of economically less developed countries. In particular, the model for good governance is the one advocated by new public management: the minimal, service-delivery state. The paper shows, first through the case of Jordan, how e-government is difficult to implement, given the characteristics of the local administration, the socioeconomic context and the dynamics of the technological infrastructure. On the basis of such evidence, it asks more generally whether the marketization of the state, embedded in e-government, makes sense as the paramount approach to improve democracy and foster development. It turns out that the transformation of citizens into customers is problematic, and the correlation between good governance and minimal state with development can hardly be demonstrated historically.If such failures are both pointed out by institutional economics theory and by current practice, the paper explores possible reasons why these projects continue to attract development aid funds. Specifically, the paper puts forward a new interpretation centred on the newly established link between aid and security. In this light, e-government appears to be one of the new tools for the rich metropolitan states to govern ‘at a distance’ (through sophisticated methodologies and technologies) the potentially dangerous, weak, borderland states. But such an approach, as many ICT fixes for the private sector have shown, may also fail and backfire: new ICT applications can drift away from the set targets and global, durable disorder within and between states may sustain intact. New research approaches leading to new practices are desperately needed.'

p09 = 'Technological advances in digital cinema have allowed people to encounter experiences that awaken their imagination and expose them to other realities. Experiencing these realties can be more difficult for the blind or visually impaired, however. In our cinema rooms, visual impairments create barriers that can restrict a person s access to critical information. Therefore, we propose a solution that attempts to eliminate these barriers by using a computational system that is able to automatically generate and distribute accessible audio tracks that describe the digital cinema experience. Using mobile devices to provide the content, visually impaired participants were given the opportunity to partake in an experiment to confirm or reject the viability of the solution presented in this article. The results of the experiment demonstrated that our computational system may be a feasible solution.'

p10 = 'The work presented in this paper aims at investigating how semiotic engineering and meta-design could be combined to support the development of socio-technical environments that enable End-User Development (EUD). In particular, I investigate the relationships existing between domain experts, playing the role of end-user developers, and meta-designers, mediated by EUD environments, and between end users and end-user developers mediated by EUD products. To this end, three case studies are considered, which belong to the recent research experience in EUD of the author. The case studies are concerned with three different application domains, namely physical prototyping of social products, accumulation and sharing of territory knowledge for first aid intervention, development of e-government services for the citizens of a municipality. The analysis is carried out both on the design process, by adopting a meta-design perspective, and on the product developed in each project, according to a semiotic engineering perspective. The analysis allows to shed light on the human and technical actors involved in EUD and on their communication processes, in order to understand which kinds of interaction visual languages and social conditions should be defined to encourage a continuous user-system co-evolution. As a result, the paper finally proposes some operative indications for the design of systems enabling EUD, which capitalize on semiotic engineering and meta-design ideas.'

p11 = 'In distributed, heterogeneous and network-connected collaborative environments where resources are provided to diverse unknown users for their applications, it is necessary to define access control for resources. Access control for such systems is defined as the ability to authorise or repudiate access to resources by a particular user. Traditional access control solutions are inherently inadequate for collaborative systems because they are effective only in situations where the system knows in advance which users are going to access the resources and what are their access rights so that they can be predefined by the developers or security administrators, but in collaborative systems the number of users as well as their usage on resources is not static. Targeting collaborative systems, a fine grained, flexible, persistent trust-based model for protecting the access and usage of digital resources is defined in this paper using radial basis function neural network (RBFNN). RBFNN classifies the users requesting the resources as trustworthy and non-trustworthy based on their attributes. RBFNN is used for classification because of its ability to generalise well for even unseen data and non-iterative method employed in its training. A proof of concept implementation backed by extensive set of tests on the real data collected for one such collaborative systems, i.e. Enabling Grids for E-Science grid demonstrated that the design is sound for collaborative systems where access of resources are provided to large and unknown users with their variant set of requirements.'

p12 = 'The special issue on Modeling and Performance Analysis of Networking and Collaborative Systems by leveraging current networks and collaborative applications. In addition, the incorporation of the latest and powerful technologies, based on distributed infrastructure, is also explored for the enhancement of these applications, resulting in complex and entangled systems that pose new issues and challenges, in terms of efficiency, security, mobility, and so on. The goal is to respond to the need for methods and tools for performance analysis and evaluation of current complex collaborative and networking systems and applications. To this direction, this special issue provides latest research on modeling and performance analysis of networking and collaborative systems from different perspectives.'

p13 = 'Currently, consumers are not passive, highly connected and linked to businesses. For this reason, some companies take advantage of these characteristics to innovate products from the contributions of customers. Co-creation as a collaborative model for innovation is characterized by being divided into related stages, in order to appropriately capture the contributions of customers. The ability to value and classify the contributions of the agents involved in this collaborative process is a task of crucial importance for organizations. The present article proposes a diffuse system that allows to value the contributions of the agents who participate in a collaborative way in the co-creation of products and services.'

p14 = 'The article describes and analyzes three social bookmarking tools and two reference management systems aimed at the academic environment in its objective and subjective aspects. It highlights the metadata marking scheme as support for infometric studies and discusses the motivational conditions for the use of such systems, as well as potential discursive zoning resulting from the analysis of descriptor tags. It raises speculations about other relationships that can be found in the formal structures of these tools, especially those concerning the function of language and the potential composition of discursive communities in virtual collaborative environments.' 

p15 = 'This article addresses the management of product information as one of the critical elements in the development of relationships in the supply chain, particularly those associated with e-business, collaborative processes and chain monitoring. The management of product information is a very recent issue and currently only a few companies have systems of this nature. Focusing on the return of information technology investments by enterprises and the development of integrated support capabilities by corporate solution providers are increasing attention to the issue. Due to this context, the article adopts a methodology of conceptual approach based on literature review and authors proposals. The article discusses how companies can effectively develop their product information management skills and suggests models relevant to e-business, collaborative processes, and supply chain monitoring.'

p16 = 'Social media treats all users the same: trusted friend or total stranger, with little or nothing in between. In reality, relationships fall everywhere along this spectrum, a topic social science has investigated for decades under the theme of tie strength. Our work bridges this gap between theory and practice. In this paper, we present a predictive model that maps social media data to tie strength. The model builds on a dataset of over 2,000 social media ties and performs quite well, distinguishing between strong and weak ties with over 85% accuracy. We complement these quantitative findings with interviews that unpack the relationships we could not predict. The paper concludes by illustrating how modeling tie strength can improve social media design elements, including privacy controls, message routing, friend introductions and information prioritization.'

p17 = 'In 2010 the popular paper by Kwak et al. [11] presented the first comprehensive study of Twitter as it appeared in 2009, using most of the Twitter network at the time. Since then, Twitter’s popularity and usage has exploded, experiencing a 10-fold increase. As of 2015, it has more than 500 million users, out of which 316 million are active, i.e. logging into the service at least once a month.1 In this study we revisit the network observed by Kwak et al. to examine the changes exhibited in both the graph and the behavior of the users in it. Our results conclude to a denser network, showing an increase in the number of reciprocal edges, despite the fact that around 12.5% of the 2009 users have now left Twitter. However, the network’s largest strongly connected component seems to be significantly decreasing, suggesting a movement of edges towards popular users. Furthermore, we observe numerous changes in the lists of influential Twitter users, having several accounts that where not popular in the past securing a position in the top-20 list as new entries.'

p18 = 'The Internet has become a rich and large repository of information about us as individuals. Anything from the links and text on a homepage of user to the mailing lists the user subscribes to are reflections of social interactions a user has in the real world. In this paper we devise techniques to mine this information in order to predict relationships between individuals. Further we show that some pieces of information are better indicators of social connections than others, and that these indicators vary between user populations and provide a glimpse into the social lives of individuals in different communities. Our techniques provide potential applications in automatically inferring real-world connections and discovering, labeling, and characterizing communities.'

p19 = 'We conduct a study of the spatio-temporal dynamics of Twitter hashtags through a sample of 2 billion geo-tagged tweets. In our analysis, we (i) examine the impact of location, time, and distance on the adoption of hashtags, which is important for understanding meme diffusion and infor mation propagation; (ii) examine the spatial propagation of hashtags through their focus, entropy, and spread; and (iii) present two methods that leverage the spatio-temporal propagation of hashtags to characterize locations. Based on this study, we find that although hashtags are a global phenomenon, the physical distance between locations is a strong constraint on the adoption of hashtags, both in terms of the hashtags shared between locations and in the timing of when these hashtags are adopted. We find both spatial and temporal locality as most hashtags spread over small geographical areas but at high speeds. We also find that hashtags are mostly a local phenomenon with long-tailed life spans.These (and other) findings have important implications for a variety of systems and applications, including targeted advertising, location-based services, social media search, and content delivery networks.'

p20 = 'Twitter, a microblogging service less than three years old, commands more than 41 million users as of July 2009 and is growing fast. Twitter users tweet about any topic within the 140-character limit and follow others to receive their tweets. The goal of this paper is to study the topological characteristics of Twitter and its power as a new medium of information sharing. We have crawled the entire Twitter site and obtained 41:7 million user profiles, 1:47 billion social relations, 4; 262 trending topics, and 106 million tweets. In its follower-following topology analysis we have found a non-power-law follower distribution, a short effective diameter, and low reciprocity, which all mark a deviation from known characteristics of human social networks [28]. In order to identify influentials on Twitter, we have ranked users by the number of followers and by PageRank and found two rankings to be similar. Ranking by retweets differs from the previous two rankings, indicating a gap in influence inferred from the number of followers and that from the popularity of one’s tweets. We have analyzed the tweets of top trending topics and reported on their temporal behavior and user participation. We have classified the trending topics based on the active period and the tweets and show that the majority (over 85%) of topics are headline news or persistent news in nature. A closer look at retweets reveals that any retweeted tweet is to reach an average of 1; 000 users no matter what the number of followers is of the original tweet. Once retweeted, a tweet gets retweeted almost instantly on next hops, signifying fast diffusion of information after the 1st retweet. To the best of our knowledge this work is the first quantitative study on the entire Twittersphere and information diffusion on it.'

p21 = 'User requirements elicitation is a complex process that requires stakeholders in teams to collaborate, go through decision-making processes and, finally, to arrive at consensus. During the user requirements elicitation processes, stakeholders who have different backgrounds, view points and understandings, need to clarify, capture and uncover user requirements in an efficient and effective manner. Many industry experts have admitted that collaboration among stakeholders in a facilitated workshop, aimed at defining and articulating user requirements, is one of the most difficult tasks in  oftware development. In this research we present   collaborative process for user requirements elicitation. We used the principles of the Collaboration Engineering (CE) to design the process, which consists of ThinkLets, as process building blocks. We designed the process to predictably guide the stakeholders through decisionmaking processes in a collaborative manner. The process is evaluated in a case-study within an industrial IT firm in China.'

p22 = 'Business Process Modeling is an important activity in organizations that document processes currently being performed or it may represent a design of a new process that should be implemented. Process models are used to analyze processes in order to improve, implement or just register them in order to document the process for new staff which should learn how to perform them. As in software engineering, there are methodologies guiding the business process elicitation activity. Accordingly, there have been also works proposing agile and lightweight methodologies for carrying out this activity. In this paper we present a tool which was especially developed for supporting an agile business process elicitation. It is based on requirements which can be derived from the description of the agile methodologies described in the literature. Two important characteristics of this tool are mobility and collaboration. We also report about an initial testing of the tool which has shown further advantages of using mobile technology in this scenario.'

p23 = 'The paper presents a collaborative ethnography approach for cognitive requirements elicitation of work teams in complex environments. It discusses the concepts of cognitive systems and their requirements, and presents a review of methods commonly used in the elicitation of requirements both in the case of traditional systems and complex systems. Then, it points to some advantages of a collaborative approach in comparison to other approaches. An evaluation plan of the approach based on experimentation and the development of a groupware to support the proposed methodology is also presented. The groupware aims to stimulate collaboration and an organization in the elicitation process of cognitive requirements.'

p24 = 'Requirements is the formal expression of user’s needs. Also, requirements elicitation is the process of activity focusing on requirements collection. Traditional acquisition methods, such as interview, observation and prototype, are unsuited for the service-oriented software development featuring in the distributed stakeholders, collective intelligence and behavioral emergence. In this paper, a collaborative requirements elicitation approach based on social intelligence for networked software is put forward, and requirements-semantics concept is defined as the formal requirements description generated by collective participation. Furthermore, semantic wikis technology is chosen as requirements authoring platform to adapt the distributed and collaborative features. Faced to the wide-area distributed Internet, it combines with the Web 2.0 and the semantic web to revise the experts requirements-semantics model through the social classification. At the same time, instantiation of requirements model is finished with semantic tagging and validation. Apart from the traditional documentary specification, requirements-semantics artifacts will be exported from the elicitation process to the subsequent software production process, i.e. services aggregation and services resource customization. Experiment and prototype have proved the feasibility and effectiveness of the proposed approach.'

p25 = 'Software development tends more and more to be a distributed or global process where participants are geographically dispersed. This scenario requires paying attention to three aspects identified as physical distance, temporal distance and cultural distance. It is acceptable to argue that these new features will impact the software process, especially in those phases where there are demands for greater communication and collaboration among team members. This paper presents a controlled experiment carried out in a university setting which tries to acquire a better knowledge elicitation stage distributed software requirements, as well as analyzes the use of university settings to perform these validations.'

p26 = 'The development of solutions known as "smart homes" has been explored to provide accessible resources to aid in the daily lives of disabled people. In particular, the growth in the development of open-source home automation applications based on Internet of Things (IoT) controlled by mobile devices presents numerous opportunities to boost the development of such aids. However, there is little research into how accessible the interfaces of such mobile applications are to people with visual disabilities. This paper presents an evaluation of six open-source mobile systems for home automation using IoT - Domoticz, Freedomotic, Home Assistant, HomeGenie, Mister House and openHAB. The evaluation was performed by means of expert review of accessibility guidelines using smartphones. The results showed that all the applications evaluated had accessibility problems that could prevent visually disabled users from using them, such as inaccessible controls, vision-dependent features, and lack of textual descriptions of images. The paper points out important adjustments that need to be carried out in order for IoT-based smart home applications to fully accomplish their potential of helping visually-disabled users lead more independent lives at home.'

p27 = 'The global impact of the digital revolution in the cultural sector worldwide brings about the need to ensure the accessibility of physical exhibits, interactive digital exhibits, digital media and digital content for disabled people. The paper addresses the accessibility of CH resources, and the need for a new approach to accessible user interaction with CH exhibits. '

p28 = 'This paper presents spazioD, a design case around the topic of dyslexia. Building on selected contributions from the literature on infrastructuring in participatory design and publics, it proposes that digital platforms are artefacts that can help infrastructuring the formation of publics and study their biography. The paper then unfolds describing the context in which the case was situated, presenting a specific digital platform (i.e. Facebook) and how it was enacted. The contribution of the paper is threefold: it provides a practice-based instance of the activities entangled in the infrastructuring of publics; building on this description, it shows how a digital platform can contribute to infrastructuring; and, finally, it articulates how the analytical tool embedded in the digital platform contribute to and influence the interpretation of an infrastructuring process and their limitations.'

p29 = 'Amateurs are found in arts, sports, or entertainment, where they are linked with professional counterparts and inspired by celebrities. Despite the growing number of CSCW studies in amateur and professional domains, little is known about how technologies facilitate collaboration between these groups. Drawing from a 1.5-year field study in the domain of bodybuilding, this paper describes the collaboration between and within amateurs, professionals, and celebrities on social network sites. Social network sites help individuals to improve their performance in competitions, extend their support network, and gain recognition for their achievements. The findings show that amateurs benefit the most from online collaboration, whereas collaboration shifts from social network sites to offline settings as individuals develop further in their professional careers. This shift from online to offline settings constitutes a novel finding, which extends previous work on social network sites that has looked at groups of amateurs and professionals in isolation. As a contribution to practice, we highlight design factors that address this shift to offline settings and foster collaboration between and within groups.'

p30 = 'In recent years, social media have increased the resources that individuals and organizations are able to mobilize for the development of socially innovative practices. In this article, we engage with a naturally occurring development in a Trentinian neighbourhood to examine the cooperative interactions amongst members of a local community. The first author and local residents of the neighbourhood participated in online discussions, decision making, and physical activities that led to material changes in the area. The interventions are motivated by and based on the concept of Social Street that combines online interactions in a closed Facebook group with face-to-face meetings seeking to practically engage the collective in accomplishing certain immediate or ongoing needs. Over the course of two years, we studied this local instantiation of Social Street in Trento, Italy by way of an action-oriented (digital) ethnography. Through this work, we demonstrate how urban neighbourhoods might benefit from hybrid forms of community engagement that are enacted through a constant back and forth between online and face-to-face interactions. We further argue that the infrastructuring of local urban collectives should follow strategies that pay attention to the multiple issues in urban neighbourhoods and people’s attachments to them. Overall, the paper reflects upon the challenges and configurations of participation that this form of community-work entails.'

p31 = 'In this paper, we explore blind people’s motivations, challenges, interactions, and experiences with visual content on Social Networking Services (SNSs). We present findings from an interview study of 11 individuals and a survey study of 60 individuals, all with little to no functional vision. Compared to sighted SNS users, our blind participants faced profound accessibility challenges, including the prevalence of photos without sufficient text descriptions. To overcome the challenges, they developed creative strategies, including using a variety of methods to access SNS features (e.g., opening the mobile site on a desktop browser), and inferring photo content from textual cues and social interactions. When strategies failed, participants reached out for help from trusted friends, or avoided certain features. We discuss our findings in the context of CSCW research and SNS accessibility as a design value. We highlight the social significance of photo interactions for blind people and suggest design practices.'

p32 = 'Lean as a business strategy is used to improve quality and service, eliminate waste, reduce time and costs, and enhance overall organizational effectiveness. Heightening challenges in competition in recent years have prompted many small and medium-sized enterprises (SMEs) to adopt lean to enhance firms competitiveness. This paper attempts to present an all-inclusive study and it examines various factors associated with the implementation of lean in SMEs in the U.S. The findings suggest that most of SMEs have a relatively accurate understanding of lean concept and philosophy. The primary reasons to implement lean are mainly internal, including reduce cost, improve profit margin, improve utilization of plant/facility, and maintain competitive position. A hierarchical cluster analysis was conducted to investigate lean status. It was discovered that both advanced adopters and beginners of lean are discovered. ANOVA test results show that there exist quite significant differences in terms of the degrees of lean implementation in SMEs. Varied lean tools and programs have been applied and they are positively related with firms performance. Lastly, the paper provides evidences that major lean barriers are encountered by SMEs regarding management or people related factors as well as key knowledge and know-how.'

p33 = 'We present the first formal study of crowdworkers who have disabilities via in-depth open-ended interviews of 17 people (disabled crowdworkers and job coaches for people with disabilities) and a survey of 631 adults with disabilities. Our findings establish that people with a variety of disabilities currently participate in the crowd labor marketplace, despite challenges such as crowdsourcing workflow designs that inadvertently prohibit participation by, and may negatively affect the worker reputations of, people with disabilities. Despite such challenges, we find that crowdwork potentially offers different opportunities for people with disabilities relative to the normative office environment, such as job flexibility and lack of a need to rely on public transit. We close by identifying several ways in which crowd labor platform operators and/or individual task requestors could improve the accessibility of this increasingly important form of employment.'

p34 = 'The author reflects on the state of accessibility in the field of computer science. He states that creating computer programs that are can be adapted and accessed by a diverse demographic is necessary due to the population of people who may have vision, hearing, or physical limitations. Other topics covered include modifications to user interfaces, computer-based services and applications, and general-purpose tools.'

p35 = 'There has been an increase in recent years in the number of in-depth case studies which focus on human actions and interpretations surrounding the development and use of computer-based information systems (IS). This paper addresses philosophical and theoretical issues concerning the nature of such interpretive case studies, and methodological issues on the conduct and reporting of this type of research. The paper aims to provide a useful reference point for researchers who wish to work in the interpretive tradition, and more generally to encourage careful work on the conceptualisation and execution of case studies in the information systems field.'

p36 = 'Valid measurement scales for predicting user acceptance of computers are in short supply. Most subjective measures used in practice are unvalidated, and their relationship to system usage is unknown. The present research develops and validates new scales for two specific variables, perceived usefulness and perceived ease of use, which are hypothesized to be fundamental determinants of user acceptance. Definitions for these two variables were used to develop scale items that were pretested for content validity and then tested for reliability and construct validity in two studies involving a total of 152 users and four application programs. The measures were refined and stream-lined, resulting in two six-item scales with reliabilities of.98 for usefulness and.94 for ease of use. The scales exhibited high convergent, discriminant, and factorial validity. Perceived usefulness was significantly correlated with both self-reported current usage (r=.63, Study 1) and self-predicted future usage (r=.85, Study 2). Perceived ease of use was also significantly correlated with current usage (r=.45, Study 1) and future usage (r=.59, Study 2). In both studies, usefulness had a significantly greater correlation with usage behavior than did ease of use. Regression analyses suggest that perceived ease of use may actually be a causal antecedent to perceived usefulness, as opposed to a parallel, direct determinant of system usage. Implications are drawn for future research on user acceptance.'

p37 = 'Developing computer-based information systems necessarily involves making a number of implicit and explicit assumptions. The authors examine four different approaches to information systems development.'

p38 = 'In traditional electronic government GIS (E-gov GIS), spatial data evaluation, examination and approval are dealt with by individuals, and the results are shared among collaborators in asynchronous mode. In order to improve the collaborative ability of E-gov GIS, a message-based synchronized cooperative GIS system (MSCGIS) is proposed in this paper. MSCGIS abstracts collaborators GIS operations and encapsulates them into GIS command messages. And then the GIS command messages are passed and executed among related collaborators. Based on messaging, MSCGIS can realize the GIS synchronized cooperation of group. Some key issues are investigated in detail, such as the design scheme of MSCGIS, the encoding specification of GIS command message based on XML, and the interface and the collaborative process of prototype system. In a word, the construction idea of MSCGIS is sharing the GIS functions through passing collaborators operations, rather than sharing spatial data among collaborators in traditional modes.'

p39 = 'Governments around the world are tapping on the potential of information and communication technologies (ICT) to transform the public sector, a phenomenon broadly known as e-government. Deployment of ICT in overnment is expected to improve internal efficiency and provide citizens with better information and services. The increasing interest in e-government is evident in the rising public expenditure on ICT. As an indicator, IDC  estimates that e-government spending in the Asia-Pacific region will exceed U.S. $31 billion by the end of 2010.6 As e-government efforts mature, the exploitation of ICT is being extended to the realm of democracy such as, in enhancing citizen participation in policy-making. The use of ICT for facilitating citizen participation, or e-Participation initiatives, refers to governments’ efforts in employing ICT for disseminating policy planning information and soliciting citizens’ inputs in planning. E-Participation initiatives have been referred to variously as e-Consultation,12 Web-based citizen input, and online public engagement '

p40 = 'This article examines the relationship between electronic participation (e-participation) and trust in local government by focusing on five dimensions of the e-participationprocess: (1) satisfaction with e-participation applications, (2) satisfaction with government responsiveness to e-participants, (3) e-participants’ development through the participation, (4) perceived influence on decision making, and (5) assessment of government transparency. Using data from the 2009 E-Participation Survey in Seoul Metropolitan Government, this article finds that e-participants’ satisfaction with e-participation applications is directly associated with their development and their assessment of government transparency. The findings reveal that e-participants’ satisfaction with government responsiveness is positively associated with their perceptions of influencing government decision making. Furthermore, there is a positive association between e-participants’ perception of influencing government decision making and their assessment of government transparency. Finally, the article finds that there is a positive association between e-participants’ assessment of government transparency and their trust in the local government providing the e-participation program.'

p41 = 'Fashion blogs are a staple of contemporary media landscape; a personal and informal guide to fashion knowledge, goods and brands. This article focuses on understanding what type of influence fashion blogs have on customers buying decisions. Findings shown in this paper are the results of Usability Tests and interviews with readers of fashion blogs. The main objectives are the comprehension of how navigation flow affects buying decisions and how bloggers outfits, photos and posts influence on readers consumption. It was possible to report that fashion blogs have special impact on social classes B and C in Brazil; informing and guiding readers social dress codes and, thereafter, influencing purchases. Usability tests showed that navigation problems frustrate readers, especially when it involves lack of outfit information or when navigation was disfavored over companies advertising interests. The discussion developed in this paper is the result of an exploratory research with a qualitative approach.'

p42 = 'Head-mounted displays (HMDs) are advertised as a solution to increase the sensation of immersion of users in virtual environments. Historically, however, research has found that technological limitations of those devices caused poor experiences and discomfort on users, limiting their applicability. We evaluated a device of the current generation of low-cost, high-performance HMDs in the context of a ball sports training application to find out if those problems remain. The results indicate that, while users reported increased immersion with the HMD, their performance in the test varied only slightly.'

p43 = 'This project has as purpose to propose an adequate method for the assessment of the emotional answer after an interaction with a social and emotional robot. A lottery game application has been developed for playing with the robot Nao, and through an experimental scenario the empathy towards a robot has been demonstrated. As a result, the Emocards are presented as a promising assessment method for the emotional answer of the users.'

p44 = 'The goal was to search for an alternative to mediate communication between people who are Deaf or Hard of Hearing (D/HH) and hearing individuals, in which the major motivation was to provide empowerment for D/HH students, using technology to provide them with more autonomy in inclusive classrooms. With that in mind, a systematic literature review was conducted to elucidate requirements for a mobile application that includes a Speech-To-Text (STT) system, as well as an opinion research accomplished with D/HH participants to know potential  priorities of users among the elucidated requirements. As a result, the preference to communicate in Libras (Brazilian Sing Language) prevails, although users consider important to use a mobile application as the one proposed.'

p45 = 'Brazilian senescent population can grow three times the actual number in the next 20 years [18], being over 88 million people in 2035. This senescent growing number brings new challenges on quality of life for Brazilian society. How to promote digital inclusion to this profile of user is still a challenge in the literature. We believe that a social network focused on senescent users can enhance the digital inclusion for them. However, its essential that the social network be designed for senescent users. This study aims to create a project with this characteristics. We analyzed a successful social network (WhatsApp) in order to propose a new one (Florch) for senescent users. We developed a high fidelity prototype of Florch and tested it. Our findings show usability and accessibility problems faced on the projects development. In addition, a Hierarchical Task Analysis of our social network showed that it has less and simpler tasks than the successful social network (WhatsApp).'

p46 = 'In today’s world, online social media plays a vital role during real world events, especially crisis events. There areboth positive and negative effects of social media coverage of events, it can be used by authorities for effective disaster management or by malicious entities to spread rumors and fake news. The aim of this paper, is to highlight the role of Twitter, during Hurricane Sandy (2012) to spread fake images about the disaster. We identified 10,350 unique tweets containing fake images that were circulated on Twitter, during to understand the temporal, social reputation and influence patterns for the spread of fake images. Eighty six percent of tweets spreading the fake images were retweets, hence very few were original tweets. Our results showed that top thirty users out of 10,215 users (0.3%) resulted in 90% of the retweets of fake images; also network links such as follower relationships of Twitter, contributed very less (only11%) to the spread of these fake photos URLs. Next, we used classification models, to distinguish fake images from real images of Hurricane Sandy. Best results were obtained from Decision Tree classifier, we got 97% accuracy in predicting fake images from real. Also, tweet based features were very effective in distinguishing fake images tweets from real, while the performance of user based features was very poor. Our results, showed that, automated techniques can be used in identifying real images from fake images posted on Twitter.'

p47 = 'We model the spread of news as a social learning game on a network. Agents can either endorse or oppose a claim made in a piece of news, which itself may be either true or false. Agents base their decision on a private signal and their neighbors’ past actions. Given these inputs, agents follow strategies derived via multi-agent deep reinforcement learning and receive utility from acting in accordance with the veracity of claims. Our framework yields strategies with agent utility close to a theoretical, Bayes optimal benchmark, while remaining flexible tomodel re-specification. Optimized strategies allow agents to correctly identify most false claims,when all agents receive unbiased private signals. However, an adversary’s attempt to spread fake news by targeting a subset of agents with a biased private signal can be successful. Even more so when the adversary has information about  network of aggents position or private signal. When agents are aware of the presence of an adversary they re-optimize their strategies in the training stage and the adversary’s attack is less effective. Hence, exposing agents to the possibility of fake news can be an effective way to curtail the spread of fake news in social networks. Our results also highlight that information about the private of users beliefs and their social network structure can be extremely valuable to adversaries and should be well protected.'

p48 = 'Social media for news consumption is a double-edged sword. On the one hand, its low cost, easy access, and rapid dissemination of information lead people to seek out and consume news from social media. On the other hand, it enables the wide spread of \fake news", i.e., low quality news with intentionallyfalse information. The extensive spread of fake news has the potential for extremely negative impacts on individuals and society. Therefore, fake news detection on social media has recently become an emerging research that is attracting tremendous attention. Fake news detection on social media presents unique haracteristics and challenges that make existing detection algorithms from traditional news media ine ective or not applicable. First, fake news is intentionally written to mislead readers to believe false information, which makes it di cult and nontrivial to detect based on news content; therefore, we need to include auxiliary information, such as user social engagements on social media, to help make a determination. Second, exploiting this auxiliary information is challenging in and of itself as users social engagements with fake news produce data that is big, incomplete, unstructured, and noisy. Because the issue of fake news detection on social media is both challenging and relevant, we conducted this survey to further facilitate research on the problem. In this survey, we present a comprehensive review of detecting fake news onsocial media, including fake news characterizations on psychology and social theories, existing algorithms from a data mining perspective, evaluation metrics and representative datasets. We also discuss related research areas, open problems, and future research directions for fake news detection on social media.' 

p49 = 'Twitter has received much attention recently. An important characteristic of Twitter is its real-time nature. We investigate the real-time interaction of events such as earthquakes in Twitter and propose an algorithm to monitor tweets and to detect a target event. To detect a target event, we devise a classifier of tweets based on features such as the keywords in a tweet, the number of words, and their context. Subsequently, we produce a probabilistic spatiotemporal model for the target event that can find the center of the event location. We regard each Twitter user as a sensor and apply particle filtering, which are widely used for location estimation. The particle filter works better than other comparable methods for estimating the locations of target events. As an application, we develop an earthquake reporting system for use in Japan. Because of the numerous earthquakes and the large number of Twitter users throughout the country, we can detect an earthquake with high probability (93 percent of earthquakes of Japan Meteorological Agency (JMA) seismic intensity scale 3 or more are detected) merely by monitoring tweets. Our system detects earthquakes promptlyand notification is delivered much faster than JMA broadcast announcements.'

p50 = 'Social network spam increases explosively with the rapid development and wide usage of various social networks on the Internet. To timely detect spam in large social network sites, it is desirable to discover unsupervised schemes that can save the training cost of supervised schemes. In this work, we first show several limitations of existing unsupervised detection schemes. The main reason behind the limitations is that existing schemes heavily rely on spamming patterns that are constantly changing to avoid detection. Motivated by our observations, we first propose a sybil defense based spam detection scheme SD2 that remarkably outperforms existing schemes by taking the social network relationship into consideration. In order to make it highly robust in facing an increased level of spam attacks, we further design an unsupervised spam detection scheme, called UNIK. Instead of detecting spammers directly, UNIK works by deliberatelyremoving non-spammers from the network, leveraging both the social graph and the user-link graph. The underpinning of UNIK is that while spammers constantly change their patterns to evade detection, non-spammers do not have to do so and thus have a relatively non-volatile pattern. UNIK has comparable performance to SD2 when it is applied to a large social network site, and outperforms SD2 significantly when the level of spam attacks increases. Based on detection results of UNIK, we further analyze several identified spam campaigns in this social network site. The result shows that different spammer clusters demonstrate distinct characteristics, implying the volatility of spamming patterns and the ability of UNIK to automatically extract spam signatures.'

p51 = 'The recommender systems are recently becoming more significant in the age of rapid development of the Internet technology due to their ability in making a decision to users on appropriate choices. Collaborative filtering (CF) is the most successful and most applied technique in the design of recommender systems where items to an active user will be recommended based on the past rating records from like-minded users. Unfortunately, CF may lead to the poor recommendation when user ratings on items are very sparse in comparison with the huge number of users and items in user-item matrix. To overcome this problem, this research applies the users’ implicit interaction records with items to efficiently process massive data by employing association rules mining. It captures the multiple purchases per transaction in association rules, rather than just counting total purchases made. To do this, a modified preprocessing is implemented to discover similar interest patterns among users based on multiple purchases done. In addition, the clustering technique has been employed in our technique to reduce the size of data and dimensionality of the item space as the performance of association rules mining. Then, similarities between items based on their features were computed to make recommendations. The experiments were conducted and the results were compared with basic CF and other extended version of CF techniques including K-Means clustering, hybrid representation, and probabilistic learning by using public dataset, namely, Million Song dataset. The experimental results demonstrated that our technique achieves the better performance when compared to the basic CF and other extended version of CF techniques in terms of Precision, Recall metrics, even when the data is very sparse.'

p52 = 'Maximum Margin Matrix Factorization (MMMF) has been a successful learning method in collaborative filtering research. For a partially observed ordinal rating matrix, the focus is on determining low-norm latent factor matrices U (of users) and V (of items) so as to simultaneously approximate the observed entries under some loss measure and predict the unobserved entries. When the rating matrix contains only two levels ( ±1), rows of V can be viewed as points in k -dimensional space and rows of U as decision hyperplanes in this space separating +1 entries from −1 entries. When hinge/smooth hinge loss is the loss function, the hyperplanes act as maximum-margin separator. In MMMF, rating matrix with multiple discrete values is treated by specially extending hinge loss function to suit multiple levels. We view this process as analogous to extending two-class classifier to a unified multi-class classifier. Alternatively, multi-class classifier can be built by arranging multiple two-class classifiers in a hierarchical manner. In this paper, we investigate this aspect for collaborative filtering and propose an efficient and novel framework of multiple bi-level MMMFs. There is substantial saving in computational overhead. We compare our method with nine well-known algorithms on two benchmark datasets and show that our method outperforms these methods on NMAE measure. We also show that our method yields latent factors of lower ranks and the trade-offbetween empirical and generalization error is low.'

p53 = 'This article proposes a new technique for Privacy Preserving Collaborative Filtering (PPCF) based on microaggregation, which provides accurate recommendations estimated from perturbed data whilst guaranteeing user k-anonymity. The experimental results presented in this article show the effectiveness of the proposed technique in protecting users’ privacy without compromising the quality of the recommendations. In this sense, the proposed approach perturbs data in a much more efficient way than other well-known methods such as Gaussian Noise Addition (GNA).'

p54 = 'In this paper, we study the problem of retrieving a ranked list of top-N items to a target user in recommender systems. We first develop a novel preference model by distinguish- ing different rating patterns of users, and then apply it to existing collaborative filtering ( CF ) algorithms. Our preference model, which is inspired by a voting method, is well- suited for representing qualitative user preferences. In particular, it can be easily imple- mented with less than 100 lines of codes on top of existing CF algorithms such as user- based, item-based, and matrix-factorization-based algorithms. When our preference model is combined to three kinds of CF algorithms, experimental results demonstrate that the preference model can improve the accuracy of all existing CF algorithms such as ATOP and NDCG@25 by 3–24% and 6–98%, respectively.'

p55 = 'Even though a large amount of content is shared on Facebook, what makes Facebook users share content has not been thoroughly addressed in previous studies. Rather than treating Facebook as just another online social media, this study focused on Facebook psychological of users incentives for content sharing and examined how users social capital focus and content types influenced the effect of incentives. Using both qualitative (focus group interview) and quantitative (online survey) methods, we obtained several findings. Both self-interest and communal incentive could drive Facebook users content-sharing intention, but their effects depended on the content types. Further, the effects of self-interest incentives were found only among the users who focus on their close friends (bonding-focus), but not among those who focus on the distant friends (bridging-focus). Brand marketers can utilize these results to post content on Facebook effectively.'

#inclusão dos resumos/produtos numa lista
listaResumos = []
listaResumos.append(p01)
listaResumos.append(p02)
listaResumos.append(p03)
listaResumos.append(p04)
listaResumos.append(p05)
listaResumos.append(p06)
listaResumos.append(p07)
listaResumos.append(p08)
listaResumos.append(p09)
listaResumos.append(p10)
listaResumos.append(p11)
listaResumos.append(p12)
listaResumos.append(p13)
listaResumos.append(p14)
listaResumos.append(p15)
listaResumos.append(p16)
listaResumos.append(p17)
listaResumos.append(p18)
listaResumos.append(p19)
listaResumos.append(p20)
listaResumos.append(p21)
listaResumos.append(p22)
listaResumos.append(p23)
listaResumos.append(p24)
listaResumos.append(p25)
listaResumos.append(p26)
listaResumos.append(p27)
listaResumos.append(p28)
listaResumos.append(p29)
listaResumos.append(p30)
listaResumos.append(p31)
listaResumos.append(p32)
listaResumos.append(p33)
listaResumos.append(p34)
listaResumos.append(p35)
listaResumos.append(p36)
listaResumos.append(p37)
listaResumos.append(p38)
listaResumos.append(p39)
listaResumos.append(p40)
listaResumos.append(p41)
listaResumos.append(p42)
listaResumos.append(p43)
listaResumos.append(p44)
listaResumos.append(p45)
listaResumos.append(p46)
listaResumos.append(p47)
listaResumos.append(p48)
listaResumos.append(p49)
listaResumos.append(p50)
listaResumos.append(p51)
listaResumos.append(p52)
listaResumos.append(p53)
listaResumos.append(p54)
listaResumos.append(p55)

#notas dos usuários para cada artigo
bruno =[5,4,4,4,4,0,0,0,0,0,0,0,4,0,0,5,0,0,0,0,0,0,0,0,0,5,5,5,4,4,0,0,0,0,0,4,4,4,3,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
edenildo = [0,0,0,0,0,3,4,4,4,5,4,3,4,3,3,4,4,4,5,4,4,3,0,3,3,5,5,5,4,4,5,4,5,5,5,3,4,5,5,4,5,5,4,4,3,3,3,2,2,4,3,0,0,4,5]
fernando = [0,0,0,0,0,4,3,5,0,0,0,0,4,4,4,4,4,0,5,4,4,4,5,3,3,5,4,5,0,4,5,4,5,4,5,0,0,0,0,0,3,3,4,5,5,4,4,4,2,4,4,5,4,4,5]
gabriel = [4,5,5,4,4,3,3,4,4,5,0,0,0,0,0,5,3,4,3,4,4,4,3,5,5,4,4,4,4,4,4,4,5,4,3,5,4,3,4,5,5,4,4,4,4,3,5,4,1,3,4,3,0,5,5]
jackson = [4,4,3,4,3,2,2,3,2,3,2,4,5,3,4,5,4,5,4,5,3,3,5,4,4,5,0,4,3,0,2,2,2,2,2,4,4,3,3,3,4,3,4,5,5,2,3,3,2,3,4,5,4,5,3]
leonardo = [4,4,4,4,4,4,5,4,3,4,5,3,4,4,4,5,4,4,5,3,0,0,0,0,0,4,4,3,3,4,4,4,5,4,4,5,3,0,3,4,4,4,4,5,5,3,3,4,3,3,4,3,5,3,5]
paulo = [5,0,0,0,0,0,0,0,5,0,0,0,3,4,0,5,4,0,3,4,4,4,4,3,5,0,0,0,0,0,5,0,0,0,0,0,0,0,0,5,4,4,5,5,5,4,3,4,3,4,4,4,4,3,4]
rafael  = [5,3,2,5,0,5,4,3,4,0,0,0,4,5,3,0,0,0,0,0,5,3,4,2,3,5,5,4,4,0,5,0,0,0,0,0,4,0,0,0,5,5,4,3,4,4,4,3,4,2,0,0,0,0,4]
thiago = [4,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,5,0,4,0,4,4,5,0,3,4,0,4,5,0,0,4,0,0,0,4,4,5,0,4,5,4,5,4,4,3,5,4,5,3,0,4,5,3,0]
jose=[0,0,0,0,0,0,5,5,4,5,3,2,0,3,3,5,0,5,0,4,0,4,4,3,3,4,3,5,5,5,4,5,0,0,4,5,0,0,0,0,4,4,5,5,4,4,3,4,4,3,4,2,4,0,4]

#função media de avaliacao
#def media_avaliacao(usuario):
 #   return mean(usuario)

def media_avaliacao(usuario):
    qtde = 0
    valor = 0
    for item in usuario:
        if item > 0:
            valor = valor + item
            qtde = qtde + 1
    return (valor/qtde)


#pré-processamento das palavras de todo o conjunto dos resumos
listaResumosMesclada = []
i = 0
while i < len(listaResumos):
    #Tokeninzação
    #Extração todas as palavras do resumo
    palavras = nltk.word_tokenize(listaResumos[i])
    
    #exclusão das palavras com tamanho = 1
    palavras = [palavra for palavra in palavras if len(palavra) > 1]
    
    #Limpeza do texto a partir das stopwords e aplicando a lemmatização
    palavras = [lem.lemmatize(palavra) for palavra in palavras if palavra.lower() not in stop_words]
    
    #Atualização da lista de palavras já tratadas 
    listaResumos[i] = palavras
    
    #mesclagem para uma lista a afim de obter as features
    listaResumosMesclada.extend(palavras)
  

#calculo da frequencia: foram selecionadas 20 palavras mais frequentes no texto
frequencia  = FreqDist(listaResumosMesclada)

#Obtenção das features e ordenação
features = [palavra[0] for palavra in frequencia.most_common(20)]
features_ordenadas = sorted(features)

#Criação da Matriz
resultado = []

#loop dos resumos
for item in listaResumos:
    linha = []
    #loop das features
    for feature in features_ordenadas:
        #verifica se a feature se encontra no conjunto de palavras 
        if feature in item:
            linha.append(1)
        else: linha.append(0) 
        #insere a linha com os matchs
        #atualiza a matriz
    resultado.append(linha)



#notas dos usuários para cada artigo
bruno =[5,4,4,4,4,0,0,0,0,0,0,0,4,0,0,5,0,0,0,0,0,0,0,0,0,5,5,5,4,4,0,0,0,0,0,4,4,4,3,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
edenildo = [0,0,0,0,0,3,4,4,4,5,4,3,4,3,3,4,4,4,5,4,4,3,0,3,3,5,5,5,4,4,5,4,5,5,5,3,4,5,5,4,5,5,4,4,3,3,3,2,2,4,3,0,0,4,5]
fernando = [0,0,0,0,0,4,3,5,0,0,0,0,4,4,4,4,4,0,5,4,4,4,5,3,3,5,4,5,0,4,5,4,5,4,5,0,0,0,0,0,3,3,4,5,5,4,4,4,2,4,4,5,4,4,5]
gabriel = [4,5,5,4,4,3,3,4,4,5,0,0,0,0,0,5,3,4,3,4,4,4,3,5,5,4,4,4,4,4,4,4,5,4,3,5,4,3,4,5,5,4,4,4,4,3,5,4,1,3,4,3,0,5,5]
jackson = [4,4,3,4,3,2,2,3,2,3,2,4,5,3,4,5,4,5,4,5,3,3,5,4,4,5,0,4,3,0,2,2,2,2,2,4,4,3,3,3,4,3,4,5,5,2,3,3,2,3,4,5,4,5,3]
leonardo = [4,4,4,4,4,4,5,4,3,4,5,3,4,4,4,5,4,4,5,3,0,0,0,0,0,4,4,3,3,4,4,4,5,4,4,5,3,0,3,4,4,4,4,5,5,3,3,4,3,3,4,3,5,3,5]
paulo = [5,0,0,0,0,0,0,0,5,0,0,0,3,4,0,5,4,0,3,4,4,4,4,3,5,0,0,0,0,0,5,0,0,0,0,0,0,0,0,5,4,4,5,5,5,4,3,4,3,4,4,4,4,3,4]
rafael  = [5,3,2,5,0,5,4,3,4,0,0,0,4,5,3,0,0,0,0,0,5,3,4,2,3,5,5,4,4,0,5,0,0,0,0,0,4,0,0,0,5,5,4,3,4,4,4,3,4,2,0,0,0,0,4]
thiago = [4,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,5,0,4,0,4,4,5,0,3,4,0,4,5,0,0,4,0,0,0,4,4,5,0,4,5,4,5,4,4,3,5,4,5,3,0,4,5,3,0]
jose=[0,0,0,0,0,0,5,5,4,5,3,2,0,3,3,5,0,5,0,4,0,4,4,3,3,4,3,5,5,5,4,5,0,0,4,5,0,0,0,0,4,4,5,5,4,4,3,4,4,3,4,2,4,0,4]

#inicio do Calculo
#Seleciona o usuário
usuarioCorrente = edenildo

#calcula mediea 
valorMediaAvaliacao = media_avaliacao(usuarioCorrente)

#normalização do vertor de notas do usuário corrente com a media - Frequência Relativa
vetorNormalizado = []
vetorItemNaoAvaliados = []
for i in range(len(usuarioCorrente)):
    if usuarioCorrente[i] == 0:
        vetorNormalizado.append(0)
        vetorItemNaoAvaliados.append(i)
    else: vetorNormalizado.append(usuarioCorrente[i] - valorMediaAvaliacao)
    
#aplicacao dos pesos produto do vetorNormalizado do Ususário pelo vetorem de cada Feature
vetorPesos = []
totalItemFeature = 0
valor = 0
for j in range(20):
    totalItemFeature = 0
    valor = 0
    for i in range((len(resultado))):
        if i not in (vetorItemNaoAvaliados):
            valor = valor + (vetorNormalizado[i] * resultado[i][j])
            totalItemFeature = totalItemFeature + resultado[i][j]
      
    vetorPesos.append(valor)
     
    
    
    
   

    






#Grafico da frequencia das features
frequencia.plot(20)   

 




