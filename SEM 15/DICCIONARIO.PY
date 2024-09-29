#Agrego informacion de 10 personas
informacion_personal={"daniel":{"edad":34,"ciudad":"ibarra","profesion":"ingeniero"},"maria":{"edad":28,"ciudad":"quito","profesion":"doctora"}, "jose":{"edad":45,"ciudad":"guayaquil","profesion":"abogado"}, "lucia":{"edad":31,"ciudad":"cuenca","profesion":"maestra"}, "pablo":{"edad":25,"ciudad":"ambato","profesion":"estudiante"}, "sandra":{"edad":39,"ciudad":"manta","profesion":"arquitecta"}, "carlos":{"edad":50,"ciudad":"loja","profesion":"comerciante"}, "veronica":{"edad":27,"ciudad":"riobamba","profesion":"diseñadora"}, "javier":{"edad":36,"ciudad":"machala","profesion":"médico"}, "natalia":{"edad":22,"ciudad":"esmeraldas","profesion":"fotógrafa"}, "arturo":{"edad":41,"ciudad":"salinas","profesion":"chef"}}
print("Información original de Arturo:",informacion_personal["arturo"])
#Cambio la informacion de arturo de salinas a QUITO
informacion_personal["arturo"]["ciudad"]="QUITO"
print("Información de Arturo después de cambiar la ciudad:",informacion_personal["arturo"])
# Agregar una nueva clave-valor para la profesión de Arturo
informacion_personal["arturo"]["nueva_profesion"] = "chef ejecutivo"
print("Información de Arturo después de agregar nueva profesión:", informacion_personal["arturo"])
# Verificar existencia de la clave "telefono"
if print("telefono" in informacion_personal["arturo"]) : "False"
informacion_personal["arturo"]["telefono"] = "0991234567"
print("Información de Arturo después de agregar teléfono:", informacion_personal["arturo"])
# Eliminar la clave "edad"
del informacion_personal["arturo"]["edad"]
print("Información de Arturo después de eliminar la edad:", informacion_personal["arturo"])
# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)