# Research Updates

## 2019-07-21

### Arya  

- I looked into time-delay differential equations, their benefits and their vices. Upon further research, DDEs seem very promising. The added complexity is much lower than face value, and they do add an extra level of precision. The main downside at this point is the buttload of extra parameters that it will require.
- I looked into different ways of representing the light variable in the optogenetic circuits. As of right now, the most promising measurement seems to be photon flux, measured in number of photons per area-second.

### Claris  

* I researched into reinforcement learning models. These models involve creating multiple models and simulations based on real time data. However, I am not sure if this would be considered a  mathematical model because the    code that we would write would not be a model but would create mathematical models in time intervals, I think.
* I also did more research into types of gradient based models. It seems that these involve PDEs and ODEs and have been largely used in bioreactor modeling

### Hari  

* I learned about the Box-Behnken design for optimizing parameters through a smaller number of designed experiments. This seems very borderline software, but could be used with known parameters in models to see what hardware changes effect them.  
* I also researched bubble column reactors, which is the kind of design hardware is going with. These bioreactors have been used in the past to produce bacterial cellulose, and their models are simpler than those of internal loop airlift bioreactors (though they are structured similarly).

### Keerthana  

### Vrishab

* As per my task on todoist, I delved into finding which genetic circuits we actually need to model. Planting a list of pros and cons enabled me to outline our options, and from there, we can decide as a team as to which method we will approach

* I also looked into what the time delay differential equation modeling would look like. The mathematics involved were quite complex, but I have learned what distinguishes it from the typical PDE/ODE modeling --> I hope to learn more about this during today's meeting.

## 2019-07-28

### Arya

- I looked further into DDEs vs ODEs, finding that DDEs wouldn't be so hard to pull of; however, they would require a significant amount of additional parameters (including mRNA concentrations) that may be  hard to obtain
- I looked into how we could model light in our genetic circuits. I came across three different methods:
  1. Implement a boolean-type system where Cph8 production would be zero if there were red light
  2. Model Cph8 production as inversely proportional to photon flux
  3. Use this really complex mathematical formula as formulated by this paper: <https://drive.google.com/file/d/1XQLTFC-Wgr7cZnodB3M1nFAt0R0jweVD/view?usp=sharing>
- The issue with (1) and (2) is that this isn't really how the light works
- I also added to a doc about different model types, which is now obsolete (because we know that we will be using a dynamic model)

### Claris

* I eliminated two of our previous bioreactor model options - the reinforcement model and the control feedback model - due to various reasons.
* I also did extensive research into the four remaining possible bioreactor models -- a metabolic control analysis model, gradient modelling, tank-in series modelling, and gradient modelling
* After doing this research, I analyzed each model, writing down pros and cons for each model. It seems seems that the best options would be a mca model or gradient modelling.

### Hari

### Keerthana

### Vrishab

## 2019-08-04

### Arya

- This past week, I focused on finding parameters and modifying the model
- I was able to find quite a few parameters which are deposited in the "model math" doc

### Claris

* This past week, I mainly worked on the bioreactor model write up
* I did any relevant research into the four models

### Hari

### Keerthana

### Vrishab

## 2019-08-11

### Arya

- This past week, I focused on finding parameters and modifying the model
- After my success on finding parameters last week, I couldn't really find anything else
- I mostly focused on wetlab this week 

### Claris

### Hari

* I researched ways to experimentally determine the degradation of the GFP + dCBD fusion protein.  
I found a possible method that uses the biobrick characterization of the OmpC promoter and assumes the fusion protein has the same maturation time as sfGFP, to interpret our experimental data as a degradation rate.  
* I searched for a few parameters involved in the axial dispersion gradient model, and added them to the parameter list.

### Keerthana

### Vrishab

## 2019-08-18

### Arya

- This past week, I found a kit called HiBiT that we could use to quantify Cph8 production and degredation rate
- I also looked at the molecular biology "bible", but found nothing of use
- I also attended th PNW iGEM meetup

### Claris

### Hari

### Keerthana

### Vrishab
