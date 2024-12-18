PGDMP       
                |            3w_db    16.4    16.4 $   .           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            /           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            0           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            1           1262    17815    3w_db    DATABASE     �   CREATE DATABASE "3w_db" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE "3w_db";
                postgres    false            �            1259    18111    app_gestion_banco    TABLE     �   CREATE TABLE public.app_gestion_banco (
    id bigint NOT NULL,
    cod character varying(4) NOT NULL,
    nombre character varying(50) NOT NULL
);
 %   DROP TABLE public.app_gestion_banco;
       public         heap    postgres    false            �            1259    18110    app_gestion_banco_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_banco_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.app_gestion_banco_id_seq;
       public          postgres    false    253            2           0    0    app_gestion_banco_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.app_gestion_banco_id_seq OWNED BY public.app_gestion_banco.id;
          public          postgres    false    252                       1259    18182    app_gestion_bancodestino    TABLE     �   CREATE TABLE public.app_gestion_bancodestino (
    id bigint NOT NULL,
    cod character varying(4) NOT NULL,
    nombre character varying(50) NOT NULL,
    tipo character varying(15) NOT NULL
);
 ,   DROP TABLE public.app_gestion_bancodestino;
       public         heap    postgres    false                       1259    18181    app_gestion_bancodestino_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_bancodestino_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.app_gestion_bancodestino_id_seq;
       public          postgres    false    261            3           0    0    app_gestion_bancodestino_id_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.app_gestion_bancodestino_id_seq OWNED BY public.app_gestion_bancodestino.id;
          public          postgres    false    260            �            1259    17994    app_gestion_ciudades    TABLE     �   CREATE TABLE public.app_gestion_ciudades (
    id bigint NOT NULL,
    ciudad character varying(40) NOT NULL,
    estado_id bigint NOT NULL
);
 (   DROP TABLE public.app_gestion_ciudades;
       public         heap    postgres    false            �            1259    17993    app_gestion_ciudad_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_ciudad_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.app_gestion_ciudad_id_seq;
       public          postgres    false    239            4           0    0    app_gestion_ciudad_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.app_gestion_ciudad_id_seq OWNED BY public.app_gestion_ciudades.id;
          public          postgres    false    238            �            1259    17979    app_gestion_clientes    TABLE     ^  CREATE TABLE public.app_gestion_clientes (
    id bigint NOT NULL,
    ced_rif character varying(10) NOT NULL,
    nombre character varying(40) NOT NULL,
    creado timestamp with time zone NOT NULL,
    status_id bigint NOT NULL,
    vendedor_id bigint NOT NULL,
    actualizado timestamp with time zone NOT NULL,
    usuario_id integer NOT NULL
);
 (   DROP TABLE public.app_gestion_clientes;
       public         heap    postgres    false            �            1259    17978    app_gestion_cliente_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_cliente_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.app_gestion_cliente_id_seq;
       public          postgres    false    237            5           0    0    app_gestion_cliente_id_seq    SEQUENCE OWNED BY     Z   ALTER SEQUENCE public.app_gestion_cliente_id_seq OWNED BY public.app_gestion_clientes.id;
          public          postgres    false    236                       1259    26677    app_gestion_condicion    TABLE     t   CREATE TABLE public.app_gestion_condicion (
    id bigint NOT NULL,
    condicion character varying(10) NOT NULL
);
 )   DROP TABLE public.app_gestion_condicion;
       public         heap    postgres    false                       1259    26676    app_gestion_condicion_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_condicion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.app_gestion_condicion_id_seq;
       public          postgres    false    271            6           0    0    app_gestion_condicion_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.app_gestion_condicion_id_seq OWNED BY public.app_gestion_condicion.id;
          public          postgres    false    270            �            1259    18102    app_gestion_control    TABLE     e   CREATE TABLE public.app_gestion_control (
    id bigint NOT NULL,
    fecha_control date NOT NULL
);
 '   DROP TABLE public.app_gestion_control;
       public         heap    postgres    false            �            1259    18101    app_gestion_control_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_control_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.app_gestion_control_id_seq;
       public          postgres    false    251            7           0    0    app_gestion_control_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.app_gestion_control_id_seq OWNED BY public.app_gestion_control.id;
          public          postgres    false    250                       1259    26526    app_gestion_credito    TABLE     ^   CREATE TABLE public.app_gestion_credito (
    id bigint NOT NULL,
    dia integer NOT NULL
);
 '   DROP TABLE public.app_gestion_credito;
       public         heap    postgres    false                       1259    26525    app_gestion_credito_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_credito_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.app_gestion_credito_id_seq;
       public          postgres    false    263            8           0    0    app_gestion_credito_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.app_gestion_credito_id_seq OWNED BY public.app_gestion_credito.id;
          public          postgres    false    262            �            1259    18080    app_gestion_dias    TABLE     [   CREATE TABLE public.app_gestion_dias (
    id bigint NOT NULL,
    dia integer NOT NULL
);
 $   DROP TABLE public.app_gestion_dias;
       public         heap    postgres    false            �            1259    18079    app_gestion_dia_id_seq    SEQUENCE        CREATE SEQUENCE public.app_gestion_dia_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.app_gestion_dia_id_seq;
       public          postgres    false    247            9           0    0    app_gestion_dia_id_seq    SEQUENCE OWNED BY     R   ALTER SEQUENCE public.app_gestion_dia_id_seq OWNED BY public.app_gestion_dias.id;
          public          postgres    false    246            �            1259    18053    app_gestion_documentos    TABLE       CREATE TABLE public.app_gestion_documentos (
    id bigint NOT NULL,
    numero character varying(40) NOT NULL,
    fecha date NOT NULL,
    monto numeric(8,2) NOT NULL,
    observacion text,
    cliente_id bigint NOT NULL,
    iva_id bigint NOT NULL,
    vencimiento date NOT NULL,
    abonado numeric(8,2) NOT NULL,
    dias_v integer NOT NULL,
    actualizado timestamp with time zone NOT NULL,
    creado timestamp with time zone NOT NULL,
    usuario_id integer NOT NULL,
    condicion_id bigint NOT NULL,
    credito integer NOT NULL
);
 *   DROP TABLE public.app_gestion_documentos;
       public         heap    postgres    false            �            1259    18052    app_gestion_documentos_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_documentos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.app_gestion_documentos_id_seq;
       public          postgres    false    245            :           0    0    app_gestion_documentos_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.app_gestion_documentos_id_seq OWNED BY public.app_gestion_documentos.id;
          public          postgres    false    244                       1259    26722    app_gestion_estados    TABLE     o   CREATE TABLE public.app_gestion_estados (
    id bigint NOT NULL,
    estado character varying(40) NOT NULL
);
 '   DROP TABLE public.app_gestion_estados;
       public         heap    postgres    false                       1259    26721    app_gestion_estados_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_estados_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.app_gestion_estados_id_seq;
       public          postgres    false    273            ;           0    0    app_gestion_estados_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.app_gestion_estados_id_seq OWNED BY public.app_gestion_estados.id;
          public          postgres    false    272                       1259    26753    app_gestion_excedente    TABLE     f  CREATE TABLE public.app_gestion_excedente (
    id bigint NOT NULL,
    concepto character varying(50),
    monto numeric(9,2) NOT NULL,
    saldo numeric(9,2) NOT NULL,
    creado timestamp with time zone NOT NULL,
    actualizado timestamp with time zone NOT NULL,
    doc_id bigint NOT NULL,
    usuario_id integer NOT NULL,
    cli_id bigint NOT NULL
);
 )   DROP TABLE public.app_gestion_excedente;
       public         heap    postgres    false                       1259    26752    app_gestion_excedente_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_excedente_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.app_gestion_excedente_id_seq;
       public          postgres    false    275            <           0    0    app_gestion_excedente_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.app_gestion_excedente_id_seq OWNED BY public.app_gestion_excedente.id;
          public          postgres    false    274            �            1259    18087    app_gestion_iva    TABLE     h   CREATE TABLE public.app_gestion_iva (
    id bigint NOT NULL,
    iva character varying(10) NOT NULL
);
 #   DROP TABLE public.app_gestion_iva;
       public         heap    postgres    false            �            1259    18086    app_gestion_iva_id_seq    SEQUENCE        CREATE SEQUENCE public.app_gestion_iva_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.app_gestion_iva_id_seq;
       public          postgres    false    249            =           0    0    app_gestion_iva_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.app_gestion_iva_id_seq OWNED BY public.app_gestion_iva.id;
          public          postgres    false    248                       1259    26604    app_gestion_pago_detalle    TABLE     �   CREATE TABLE public.app_gestion_pago_detalle (
    id bigint NOT NULL,
    monto_procesar numeric(8,2) NOT NULL,
    documento_id bigint NOT NULL,
    pago_id bigint NOT NULL
);
 ,   DROP TABLE public.app_gestion_pago_detalle;
       public         heap    postgres    false                       1259    26603    app_gestion_pago_detalle_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_pago_detalle_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.app_gestion_pago_detalle_id_seq;
       public          postgres    false    269            >           0    0    app_gestion_pago_detalle_id_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.app_gestion_pago_detalle_id_seq OWNED BY public.app_gestion_pago_detalle.id;
          public          postgres    false    268            �            1259    18118    app_gestion_pagoforma    TABLE     �   CREATE TABLE public.app_gestion_pagoforma (
    id bigint NOT NULL,
    forma character varying(40) NOT NULL,
    orden integer NOT NULL
);
 )   DROP TABLE public.app_gestion_pagoforma;
       public         heap    postgres    false            �            1259    18117    app_gestion_pagoforma_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_pagoforma_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.app_gestion_pagoforma_id_seq;
       public          postgres    false    255            ?           0    0    app_gestion_pagoforma_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.app_gestion_pagoforma_id_seq OWNED BY public.app_gestion_pagoforma.id;
          public          postgres    false    254                       1259    18153    app_gestion_pagos    TABLE       CREATE TABLE public.app_gestion_pagos (
    id bigint NOT NULL,
    fecha date NOT NULL,
    referencia character varying(30),
    monto numeric(9,2) NOT NULL,
    monto_procesar numeric(8,2) NOT NULL,
    observacion text NOT NULL,
    cliente_id bigint NOT NULL,
    forma_id bigint NOT NULL,
    actualizado timestamp with time zone NOT NULL,
    creado timestamp with time zone NOT NULL,
    banco_destino_id bigint NOT NULL,
    tasa numeric(5,2) NOT NULL,
    usuario_id integer NOT NULL,
    seguimiento text NOT NULL
);
 %   DROP TABLE public.app_gestion_pagos;
       public         heap    postgres    false                       1259    18152    app_gestion_pagos_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_pagos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.app_gestion_pagos_id_seq;
       public          postgres    false    259            @           0    0    app_gestion_pagos_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.app_gestion_pagos_id_seq OWNED BY public.app_gestion_pagos.id;
          public          postgres    false    258            	           1259    26533    app_gestion_prefijo_ced_rif    TABLE     y   CREATE TABLE public.app_gestion_prefijo_ced_rif (
    id bigint NOT NULL,
    prefijo_r character varying(1) NOT NULL
);
 /   DROP TABLE public.app_gestion_prefijo_ced_rif;
       public         heap    postgres    false                       1259    26532 "   app_gestion_prefijo_ced_rif_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_prefijo_ced_rif_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 9   DROP SEQUENCE public.app_gestion_prefijo_ced_rif_id_seq;
       public          postgres    false    265            A           0    0 "   app_gestion_prefijo_ced_rif_id_seq    SEQUENCE OWNED BY     i   ALTER SEQUENCE public.app_gestion_prefijo_ced_rif_id_seq OWNED BY public.app_gestion_prefijo_ced_rif.id;
          public          postgres    false    264                       1259    26541    app_gestion_prefijo_telefono    TABLE     z   CREATE TABLE public.app_gestion_prefijo_telefono (
    id bigint NOT NULL,
    prefijo_t character varying(4) NOT NULL
);
 0   DROP TABLE public.app_gestion_prefijo_telefono;
       public         heap    postgres    false            
           1259    26540 #   app_gestion_prefijo_telefono_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_prefijo_telefono_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 :   DROP SEQUENCE public.app_gestion_prefijo_telefono_id_seq;
       public          postgres    false    267            B           0    0 #   app_gestion_prefijo_telefono_id_seq    SEQUENCE OWNED BY     k   ALTER SEQUENCE public.app_gestion_prefijo_telefono_id_seq OWNED BY public.app_gestion_prefijo_telefono.id;
          public          postgres    false    266            �            1259    18041    app_gestion_siono    TABLE     l   CREATE TABLE public.app_gestion_siono (
    id bigint NOT NULL,
    siono character varying(10) NOT NULL
);
 %   DROP TABLE public.app_gestion_siono;
       public         heap    postgres    false            �            1259    18040    app_gestion_siono_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_siono_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.app_gestion_siono_id_seq;
       public          postgres    false    243            C           0    0    app_gestion_siono_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.app_gestion_siono_id_seq OWNED BY public.app_gestion_siono.id;
          public          postgres    false    242            �            1259    17972    app_gestion_status    TABLE     m   CREATE TABLE public.app_gestion_status (
    id bigint NOT NULL,
    statu character varying(20) NOT NULL
);
 &   DROP TABLE public.app_gestion_status;
       public         heap    postgres    false            �            1259    17971    app_gestion_status_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_status_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.app_gestion_status_id_seq;
       public          postgres    false    235            D           0    0    app_gestion_status_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.app_gestion_status_id_seq OWNED BY public.app_gestion_status.id;
          public          postgres    false    234                       1259    18125    app_gestion_tasa    TABLE       CREATE TABLE public.app_gestion_tasa (
    id bigint NOT NULL,
    fecha date NOT NULL,
    monto numeric(7,2) NOT NULL,
    createdo timestamp with time zone NOT NULL,
    actualizado timestamp with time zone NOT NULL,
    usuario_id integer NOT NULL,
    seguimiento text
);
 $   DROP TABLE public.app_gestion_tasa;
       public         heap    postgres    false                        1259    18124    app_gestion_tasa_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_tasa_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.app_gestion_tasa_id_seq;
       public          postgres    false    257            E           0    0    app_gestion_tasa_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.app_gestion_tasa_id_seq OWNED BY public.app_gestion_tasa.id;
          public          postgres    false    256            �            1259    18015    app_gestion_vendedores    TABLE     \  CREATE TABLE public.app_gestion_vendedores (
    id bigint NOT NULL,
    nombre character varying(40) NOT NULL,
    status_id bigint NOT NULL,
    cedula character varying(9) NOT NULL,
    ciudad_id bigint NOT NULL,
    actualizado timestamp with time zone NOT NULL,
    creado timestamp with time zone NOT NULL,
    usuario_id integer NOT NULL
);
 *   DROP TABLE public.app_gestion_vendedores;
       public         heap    postgres    false            �            1259    18014    app_gestion_vendedor_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_gestion_vendedor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.app_gestion_vendedor_id_seq;
       public          postgres    false    241            F           0    0    app_gestion_vendedor_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.app_gestion_vendedor_id_seq OWNED BY public.app_gestion_vendedores.id;
          public          postgres    false    240            �            1259    17842 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         heap    postgres    false            �            1259    17841    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public          postgres    false    222            G           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
          public          postgres    false    221            �            1259    17851    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         heap    postgres    false            �            1259    17850    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public          postgres    false    224            H           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
          public          postgres    false    223            �            1259    17835    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         heap    postgres    false            �            1259    17834    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public          postgres    false    220            I           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
          public          postgres    false    219            �            1259    17858 	   auth_user    TABLE     �  CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public         heap    postgres    false            �            1259    17867    auth_user_groups    TABLE     ~   CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         heap    postgres    false            �            1259    17866    auth_user_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public          postgres    false    228            J           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;
          public          postgres    false    227            �            1259    17857    auth_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public          postgres    false    226            K           0    0    auth_user_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;
          public          postgres    false    225            �            1259    17874    auth_user_user_permissions    TABLE     �   CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         heap    postgres    false            �            1259    17873 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public          postgres    false    230            L           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;
          public          postgres    false    229            �            1259    17933    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         heap    postgres    false            �            1259    17932    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public          postgres    false    232            M           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
          public          postgres    false    231            �            1259    17826    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         heap    postgres    false            �            1259    17825    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public          postgres    false    218            N           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
          public          postgres    false    217            �            1259    17817    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         heap    postgres    false            �            1259    17816    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public          postgres    false    216            O           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
          public          postgres    false    215            �            1259    17962    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         heap    postgres    false            �           2604    18114    app_gestion_banco id    DEFAULT     |   ALTER TABLE ONLY public.app_gestion_banco ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_banco_id_seq'::regclass);
 C   ALTER TABLE public.app_gestion_banco ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    252    253    253            �           2604    18185    app_gestion_bancodestino id    DEFAULT     �   ALTER TABLE ONLY public.app_gestion_bancodestino ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_bancodestino_id_seq'::regclass);
 J   ALTER TABLE public.app_gestion_bancodestino ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    260    261    261            �           2604    17997    app_gestion_ciudades id    DEFAULT     �   ALTER TABLE ONLY public.app_gestion_ciudades ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_ciudad_id_seq'::regclass);
 F   ALTER TABLE public.app_gestion_ciudades ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    238    239    239            �           2604    17982    app_gestion_clientes id    DEFAULT     �   ALTER TABLE ONLY public.app_gestion_clientes ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_cliente_id_seq'::regclass);
 F   ALTER TABLE public.app_gestion_clientes ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    237    236    237            �           2604    26680    app_gestion_condicion id    DEFAULT     �   ALTER TABLE ONLY public.app_gestion_condicion ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_condicion_id_seq'::regclass);
 G   ALTER TABLE public.app_gestion_condicion ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    271    270    271            �           2604    18105    app_gestion_control id    DEFAULT     �   ALTER TABLE ONLY public.app_gestion_control ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_control_id_seq'::regclass);
 E   ALTER TABLE public.app_gestion_control ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    250    251    251            �           2604    26529    app_gestion_credito id    DEFAULT     �   ALTER TABLE ONLY public.app_gestion_credito ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_credito_id_seq'::regclass);
 E   ALTER TABLE public.app_gestion_credito ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    263    262    263            �           2604    18083    app_gestion_dias id    DEFAULT     y   ALTER TABLE ONLY public.app_gestion_dias ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_dia_id_seq'::regclass);
 B   ALTER TABLE public.app_gestion_dias ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    247    246    247            �           2604    18056    app_gestion_documentos id    DEFAULT     �   ALTER TABLE ONLY public.app_gestion_documentos ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_documentos_id_seq'::regclass);
 H   ALTER TABLE public.app_gestion_documentos ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    244    245    245            �           2604    26725    app_gestion_estados id    DEFAULT     �   ALTER TABLE ONLY public.app_gestion_estados ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_estados_id_seq'::regclass);
 E   ALTER TABLE public.app_gestion_estados ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    272    273    273            �           2604    26756    app_gestion_excedente id    DEFAULT     �   ALTER TABLE ONLY public.app_gestion_excedente ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_excedente_id_seq'::regclass);
 G   ALTER TABLE public.app_gestion_excedente ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    274    275    275            �           2604    18090    app_gestion_iva id    DEFAULT     x   ALTER TABLE ONLY public.app_gestion_iva ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_iva_id_seq'::regclass);
 A   ALTER TABLE public.app_gestion_iva ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    249    248    249            �           2604    26607    app_gestion_pago_detalle id    DEFAULT     �   ALTER TABLE ONLY public.app_gestion_pago_detalle ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_pago_detalle_id_seq'::regclass);
 J   ALTER TABLE public.app_gestion_pago_detalle ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    269    268    269            �           2604    18121    app_gestion_pagoforma id    DEFAULT     �   ALTER TABLE ONLY public.app_gestion_pagoforma ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_pagoforma_id_seq'::regclass);
 G   ALTER TABLE public.app_gestion_pagoforma ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    255    254    255            �           2604    18156    app_gestion_pagos id    DEFAULT     |   ALTER TABLE ONLY public.app_gestion_pagos ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_pagos_id_seq'::regclass);
 C   ALTER TABLE public.app_gestion_pagos ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    258    259    259            �           2604    26536    app_gestion_prefijo_ced_rif id    DEFAULT     �   ALTER TABLE ONLY public.app_gestion_prefijo_ced_rif ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_prefijo_ced_rif_id_seq'::regclass);
 M   ALTER TABLE public.app_gestion_prefijo_ced_rif ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    265    264    265            �           2604    26544    app_gestion_prefijo_telefono id    DEFAULT     �   ALTER TABLE ONLY public.app_gestion_prefijo_telefono ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_prefijo_telefono_id_seq'::regclass);
 N   ALTER TABLE public.app_gestion_prefijo_telefono ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    267    266    267            �           2604    18044    app_gestion_siono id    DEFAULT     |   ALTER TABLE ONLY public.app_gestion_siono ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_siono_id_seq'::regclass);
 C   ALTER TABLE public.app_gestion_siono ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    242    243    243            �           2604    17975    app_gestion_status id    DEFAULT     ~   ALTER TABLE ONLY public.app_gestion_status ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_status_id_seq'::regclass);
 D   ALTER TABLE public.app_gestion_status ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    235    234    235            �           2604    18128    app_gestion_tasa id    DEFAULT     z   ALTER TABLE ONLY public.app_gestion_tasa ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_tasa_id_seq'::regclass);
 B   ALTER TABLE public.app_gestion_tasa ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    257    256    257            �           2604    18018    app_gestion_vendedores id    DEFAULT     �   ALTER TABLE ONLY public.app_gestion_vendedores ALTER COLUMN id SET DEFAULT nextval('public.app_gestion_vendedor_id_seq'::regclass);
 H   ALTER TABLE public.app_gestion_vendedores ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    240    241    241            �           2604    17845    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    222    221    222            �           2604    17854    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    223    224    224            �           2604    17838    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    220    219    220            �           2604    17861    auth_user id    DEFAULT     l   ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    225    226    226            �           2604    17870    auth_user_groups id    DEFAULT     z   ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    228    227    228            �           2604    17877    auth_user_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    230    229    230            �           2604    17936    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    231    232    232            �           2604    17829    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    218    218            �           2604    17820    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    215    216                      0    18111    app_gestion_banco 
   TABLE DATA           <   COPY public.app_gestion_banco (id, cod, nombre) FROM stdin;
    public          postgres    false    253   �                0    18182    app_gestion_bancodestino 
   TABLE DATA           I   COPY public.app_gestion_bancodestino (id, cod, nombre, tipo) FROM stdin;
    public          postgres    false    261   3�                0    17994    app_gestion_ciudades 
   TABLE DATA           E   COPY public.app_gestion_ciudades (id, ciudad, estado_id) FROM stdin;
    public          postgres    false    239   �                0    17979    app_gestion_clientes 
   TABLE DATA           |   COPY public.app_gestion_clientes (id, ced_rif, nombre, creado, status_id, vendedor_id, actualizado, usuario_id) FROM stdin;
    public          postgres    false    237   ��      '          0    26677    app_gestion_condicion 
   TABLE DATA           >   COPY public.app_gestion_condicion (id, condicion) FROM stdin;
    public          postgres    false    271   ��                0    18102    app_gestion_control 
   TABLE DATA           @   COPY public.app_gestion_control (id, fecha_control) FROM stdin;
    public          postgres    false    251   ӌ                0    26526    app_gestion_credito 
   TABLE DATA           6   COPY public.app_gestion_credito (id, dia) FROM stdin;
    public          postgres    false    263   ��                0    18080    app_gestion_dias 
   TABLE DATA           3   COPY public.app_gestion_dias (id, dia) FROM stdin;
    public          postgres    false    247   /�                0    18053    app_gestion_documentos 
   TABLE DATA           �   COPY public.app_gestion_documentos (id, numero, fecha, monto, observacion, cliente_id, iva_id, vencimiento, abonado, dias_v, actualizado, creado, usuario_id, condicion_id, credito) FROM stdin;
    public          postgres    false    245   Q�      )          0    26722    app_gestion_estados 
   TABLE DATA           9   COPY public.app_gestion_estados (id, estado) FROM stdin;
    public          postgres    false    273   ��      +          0    26753    app_gestion_excedente 
   TABLE DATA           |   COPY public.app_gestion_excedente (id, concepto, monto, saldo, creado, actualizado, doc_id, usuario_id, cli_id) FROM stdin;
    public          postgres    false    275   ��                0    18087    app_gestion_iva 
   TABLE DATA           2   COPY public.app_gestion_iva (id, iva) FROM stdin;
    public          postgres    false    249   �      %          0    26604    app_gestion_pago_detalle 
   TABLE DATA           ]   COPY public.app_gestion_pago_detalle (id, monto_procesar, documento_id, pago_id) FROM stdin;
    public          postgres    false    269   �                0    18118    app_gestion_pagoforma 
   TABLE DATA           A   COPY public.app_gestion_pagoforma (id, forma, orden) FROM stdin;
    public          postgres    false    255   ��                0    18153    app_gestion_pagos 
   TABLE DATA           �   COPY public.app_gestion_pagos (id, fecha, referencia, monto, monto_procesar, observacion, cliente_id, forma_id, actualizado, creado, banco_destino_id, tasa, usuario_id, seguimiento) FROM stdin;
    public          postgres    false    259   %�      !          0    26533    app_gestion_prefijo_ced_rif 
   TABLE DATA           D   COPY public.app_gestion_prefijo_ced_rif (id, prefijo_r) FROM stdin;
    public          postgres    false    265   ��      #          0    26541    app_gestion_prefijo_telefono 
   TABLE DATA           E   COPY public.app_gestion_prefijo_telefono (id, prefijo_t) FROM stdin;
    public          postgres    false    267   ��                0    18041    app_gestion_siono 
   TABLE DATA           6   COPY public.app_gestion_siono (id, siono) FROM stdin;
    public          postgres    false    243   �                0    17972    app_gestion_status 
   TABLE DATA           7   COPY public.app_gestion_status (id, statu) FROM stdin;
    public          postgres    false    235   �                0    18125    app_gestion_tasa 
   TABLE DATA           l   COPY public.app_gestion_tasa (id, fecha, monto, createdo, actualizado, usuario_id, seguimiento) FROM stdin;
    public          postgres    false    257   O�      	          0    18015    app_gestion_vendedores 
   TABLE DATA           {   COPY public.app_gestion_vendedores (id, nombre, status_id, cedula, ciudad_id, actualizado, creado, usuario_id) FROM stdin;
    public          postgres    false    241   W�      �          0    17842 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          postgres    false    222   ��      �          0    17851    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          postgres    false    224   �      �          0    17835    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          postgres    false    220   4�      �          0    17858 	   auth_user 
   TABLE DATA           �   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public          postgres    false    226   ��      �          0    17867    auth_user_groups 
   TABLE DATA           A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public          postgres    false    228   Ş      �          0    17874    auth_user_user_permissions 
   TABLE DATA           P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public          postgres    false    230   �                 0    17933    django_admin_log 
   TABLE DATA           �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          postgres    false    232   ��      �          0    17826    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          postgres    false    218   ��      �          0    17817    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          postgres    false    216   ��                0    17962    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          postgres    false    233   �      P           0    0    app_gestion_banco_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.app_gestion_banco_id_seq', 1, false);
          public          postgres    false    252            Q           0    0    app_gestion_bancodestino_id_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.app_gestion_bancodestino_id_seq', 15, true);
          public          postgres    false    260            R           0    0    app_gestion_ciudad_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.app_gestion_ciudad_id_seq', 70, true);
          public          postgres    false    238            S           0    0    app_gestion_cliente_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.app_gestion_cliente_id_seq', 5, true);
          public          postgres    false    236            T           0    0    app_gestion_condicion_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.app_gestion_condicion_id_seq', 2, true);
          public          postgres    false    270            U           0    0    app_gestion_control_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.app_gestion_control_id_seq', 1, true);
          public          postgres    false    250            V           0    0    app_gestion_credito_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.app_gestion_credito_id_seq', 5, true);
          public          postgres    false    262            W           0    0    app_gestion_dia_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.app_gestion_dia_id_seq', 1, true);
          public          postgres    false    246            X           0    0    app_gestion_documentos_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.app_gestion_documentos_id_seq', 18, true);
          public          postgres    false    244            Y           0    0    app_gestion_estados_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.app_gestion_estados_id_seq', 24, true);
          public          postgres    false    272            Z           0    0    app_gestion_excedente_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.app_gestion_excedente_id_seq', 3, true);
          public          postgres    false    274            [           0    0    app_gestion_iva_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.app_gestion_iva_id_seq', 3, true);
          public          postgres    false    248            \           0    0    app_gestion_pago_detalle_id_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.app_gestion_pago_detalle_id_seq', 56, true);
          public          postgres    false    268            ]           0    0    app_gestion_pagoforma_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.app_gestion_pagoforma_id_seq', 5, true);
          public          postgres    false    254            ^           0    0    app_gestion_pagos_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.app_gestion_pagos_id_seq', 16, true);
          public          postgres    false    258            _           0    0 "   app_gestion_prefijo_ced_rif_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.app_gestion_prefijo_ced_rif_id_seq', 2, true);
          public          postgres    false    264            `           0    0 #   app_gestion_prefijo_telefono_id_seq    SEQUENCE SET     R   SELECT pg_catalog.setval('public.app_gestion_prefijo_telefono_id_seq', 11, true);
          public          postgres    false    266            a           0    0    app_gestion_siono_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.app_gestion_siono_id_seq', 3, true);
          public          postgres    false    242            b           0    0    app_gestion_status_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.app_gestion_status_id_seq', 4, true);
          public          postgres    false    234            c           0    0    app_gestion_tasa_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.app_gestion_tasa_id_seq', 5, true);
          public          postgres    false    256            d           0    0    app_gestion_vendedor_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.app_gestion_vendedor_id_seq', 3, true);
          public          postgres    false    240            e           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
          public          postgres    false    221            f           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
          public          postgres    false    223            g           0    0    auth_permission_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_permission_id_seq', 120, true);
          public          postgres    false    219            h           0    0    auth_user_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);
          public          postgres    false    227            i           0    0    auth_user_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.auth_user_id_seq', 2, true);
          public          postgres    false    225            j           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);
          public          postgres    false    229            k           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 27, true);
          public          postgres    false    231            l           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 29, true);
          public          postgres    false    217            m           0    0    django_migrations_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.django_migrations_id_seq', 119, true);
          public          postgres    false    215            !           2606    18116 (   app_gestion_banco app_gestion_banco_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.app_gestion_banco
    ADD CONSTRAINT app_gestion_banco_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.app_gestion_banco DROP CONSTRAINT app_gestion_banco_pkey;
       public            postgres    false    253            .           2606    18187 6   app_gestion_bancodestino app_gestion_bancodestino_pkey 
   CONSTRAINT     t   ALTER TABLE ONLY public.app_gestion_bancodestino
    ADD CONSTRAINT app_gestion_bancodestino_pkey PRIMARY KEY (id);
 `   ALTER TABLE ONLY public.app_gestion_bancodestino DROP CONSTRAINT app_gestion_bancodestino_pkey;
       public            postgres    false    261            �           2606    17977 ,   app_gestion_status app_gestion_c_status_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.app_gestion_status
    ADD CONSTRAINT app_gestion_c_status_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.app_gestion_status DROP CONSTRAINT app_gestion_c_status_pkey;
       public            postgres    false    235                       2606    17999 ,   app_gestion_ciudades app_gestion_ciudad_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.app_gestion_ciudades
    ADD CONSTRAINT app_gestion_ciudad_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.app_gestion_ciudades DROP CONSTRAINT app_gestion_ciudad_pkey;
       public            postgres    false    239                        2606    17986 -   app_gestion_clientes app_gestion_cliente_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.app_gestion_clientes
    ADD CONSTRAINT app_gestion_cliente_pkey PRIMARY KEY (id);
 W   ALTER TABLE ONLY public.app_gestion_clientes DROP CONSTRAINT app_gestion_cliente_pkey;
       public            postgres    false    237            :           2606    26682 0   app_gestion_condicion app_gestion_condicion_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.app_gestion_condicion
    ADD CONSTRAINT app_gestion_condicion_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.app_gestion_condicion DROP CONSTRAINT app_gestion_condicion_pkey;
       public            postgres    false    271                       2606    18107 ,   app_gestion_control app_gestion_control_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.app_gestion_control
    ADD CONSTRAINT app_gestion_control_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.app_gestion_control DROP CONSTRAINT app_gestion_control_pkey;
       public            postgres    false    251            0           2606    26531 ,   app_gestion_credito app_gestion_credito_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.app_gestion_credito
    ADD CONSTRAINT app_gestion_credito_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.app_gestion_credito DROP CONSTRAINT app_gestion_credito_pkey;
       public            postgres    false    263                       2606    18085 %   app_gestion_dias app_gestion_dia_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.app_gestion_dias
    ADD CONSTRAINT app_gestion_dia_pkey PRIMARY KEY (id);
 O   ALTER TABLE ONLY public.app_gestion_dias DROP CONSTRAINT app_gestion_dia_pkey;
       public            postgres    false    247                       2606    26601 B   app_gestion_documentos app_gestion_documentos_numero_910c469a_uniq 
   CONSTRAINT        ALTER TABLE ONLY public.app_gestion_documentos
    ADD CONSTRAINT app_gestion_documentos_numero_910c469a_uniq UNIQUE (numero);
 l   ALTER TABLE ONLY public.app_gestion_documentos DROP CONSTRAINT app_gestion_documentos_numero_910c469a_uniq;
       public            postgres    false    245                       2606    18060 2   app_gestion_documentos app_gestion_documentos_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.app_gestion_documentos
    ADD CONSTRAINT app_gestion_documentos_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.app_gestion_documentos DROP CONSTRAINT app_gestion_documentos_pkey;
       public            postgres    false    245            <           2606    26727 ,   app_gestion_estados app_gestion_estados_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.app_gestion_estados
    ADD CONSTRAINT app_gestion_estados_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.app_gestion_estados DROP CONSTRAINT app_gestion_estados_pkey;
       public            postgres    false    273            @           2606    26758 0   app_gestion_excedente app_gestion_excedente_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.app_gestion_excedente
    ADD CONSTRAINT app_gestion_excedente_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.app_gestion_excedente DROP CONSTRAINT app_gestion_excedente_pkey;
       public            postgres    false    275                       2606    18092 $   app_gestion_iva app_gestion_iva_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.app_gestion_iva
    ADD CONSTRAINT app_gestion_iva_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.app_gestion_iva DROP CONSTRAINT app_gestion_iva_pkey;
       public            postgres    false    249            8           2606    26609 6   app_gestion_pago_detalle app_gestion_pago_detalle_pkey 
   CONSTRAINT     t   ALTER TABLE ONLY public.app_gestion_pago_detalle
    ADD CONSTRAINT app_gestion_pago_detalle_pkey PRIMARY KEY (id);
 `   ALTER TABLE ONLY public.app_gestion_pago_detalle DROP CONSTRAINT app_gestion_pago_detalle_pkey;
       public            postgres    false    269            #           2606    18123 0   app_gestion_pagoforma app_gestion_pagoforma_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.app_gestion_pagoforma
    ADD CONSTRAINT app_gestion_pagoforma_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.app_gestion_pagoforma DROP CONSTRAINT app_gestion_pagoforma_pkey;
       public            postgres    false    255            +           2606    18160 (   app_gestion_pagos app_gestion_pagos_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.app_gestion_pagos
    ADD CONSTRAINT app_gestion_pagos_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.app_gestion_pagos DROP CONSTRAINT app_gestion_pagos_pkey;
       public            postgres    false    259            2           2606    26538 <   app_gestion_prefijo_ced_rif app_gestion_prefijo_ced_rif_pkey 
   CONSTRAINT     z   ALTER TABLE ONLY public.app_gestion_prefijo_ced_rif
    ADD CONSTRAINT app_gestion_prefijo_ced_rif_pkey PRIMARY KEY (id);
 f   ALTER TABLE ONLY public.app_gestion_prefijo_ced_rif DROP CONSTRAINT app_gestion_prefijo_ced_rif_pkey;
       public            postgres    false    265            4           2606    26546 >   app_gestion_prefijo_telefono app_gestion_prefijo_telefono_pkey 
   CONSTRAINT     |   ALTER TABLE ONLY public.app_gestion_prefijo_telefono
    ADD CONSTRAINT app_gestion_prefijo_telefono_pkey PRIMARY KEY (id);
 h   ALTER TABLE ONLY public.app_gestion_prefijo_telefono DROP CONSTRAINT app_gestion_prefijo_telefono_pkey;
       public            postgres    false    267                       2606    18046 (   app_gestion_siono app_gestion_siono_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.app_gestion_siono
    ADD CONSTRAINT app_gestion_siono_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.app_gestion_siono DROP CONSTRAINT app_gestion_siono_pkey;
       public            postgres    false    243            %           2606    18130 &   app_gestion_tasa app_gestion_tasa_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.app_gestion_tasa
    ADD CONSTRAINT app_gestion_tasa_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.app_gestion_tasa DROP CONSTRAINT app_gestion_tasa_pkey;
       public            postgres    false    257                       2606    18020 0   app_gestion_vendedores app_gestion_vendedor_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.app_gestion_vendedores
    ADD CONSTRAINT app_gestion_vendedor_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.app_gestion_vendedores DROP CONSTRAINT app_gestion_vendedor_pkey;
       public            postgres    false    241                       2606    26598 B   app_gestion_vendedores app_gestion_vendedores_cedula_72078c8c_uniq 
   CONSTRAINT        ALTER TABLE ONLY public.app_gestion_vendedores
    ADD CONSTRAINT app_gestion_vendedores_cedula_72078c8c_uniq UNIQUE (cedula);
 l   ALTER TABLE ONLY public.app_gestion_vendedores DROP CONSTRAINT app_gestion_vendedores_cedula_72078c8c_uniq;
       public            postgres    false    241            �           2606    17960    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public            postgres    false    222            �           2606    17890 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public            postgres    false    224    224            �           2606    17856 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public            postgres    false    224            �           2606    17847    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public            postgres    false    222            �           2606    17881 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public            postgres    false    220    220            �           2606    17840 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public            postgres    false    220            �           2606    17872 &   auth_user_groups auth_user_groups_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public            postgres    false    228            �           2606    17905 @   auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
       public            postgres    false    228    228            �           2606    17863    auth_user auth_user_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public            postgres    false    226            �           2606    17879 :   auth_user_user_permissions auth_user_user_permissions_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public            postgres    false    230            �           2606    17919 Y   auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
       public            postgres    false    230    230            �           2606    17955     auth_user auth_user_username_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public            postgres    false    226            �           2606    17941 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public            postgres    false    232            �           2606    17833 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public            postgres    false    218    218            �           2606    17831 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public            postgres    false    218            �           2606    17824 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public            postgres    false    216            �           2606    17968 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public            postgres    false    233                       1259    26732 '   app_gestion_ciudades_estado_id_39eda0a5    INDEX     m   CREATE INDEX app_gestion_ciudades_estado_id_39eda0a5 ON public.app_gestion_ciudades USING btree (estado_id);
 ;   DROP INDEX public.app_gestion_ciudades_estado_id_39eda0a5;
       public            postgres    false    239                       1259    17992 &   app_gestion_cliente_status_id_23703036    INDEX     l   CREATE INDEX app_gestion_cliente_status_id_23703036 ON public.app_gestion_clientes USING btree (status_id);
 :   DROP INDEX public.app_gestion_cliente_status_id_23703036;
       public            postgres    false    237                       1259    18039 )   app_gestion_clientes_Vendedor_id_a1f4b474    INDEX     s   CREATE INDEX "app_gestion_clientes_Vendedor_id_a1f4b474" ON public.app_gestion_clientes USING btree (vendedor_id);
 ?   DROP INDEX public."app_gestion_clientes_Vendedor_id_a1f4b474";
       public            postgres    false    237                       1259    26563 (   app_gestion_clientes_usuario_id_11cc7be4    INDEX     o   CREATE INDEX app_gestion_clientes_usuario_id_11cc7be4 ON public.app_gestion_clientes USING btree (usuario_id);
 <   DROP INDEX public.app_gestion_clientes_usuario_id_11cc7be4;
       public            postgres    false    237                       1259    18071 *   app_gestion_documentos_cliente_id_20316d3e    INDEX     s   CREATE INDEX app_gestion_documentos_cliente_id_20316d3e ON public.app_gestion_documentos USING btree (cliente_id);
 >   DROP INDEX public.app_gestion_documentos_cliente_id_20316d3e;
       public            postgres    false    245                       1259    26695 ,   app_gestion_documentos_condicion_id_f58ae107    INDEX     w   CREATE INDEX app_gestion_documentos_condicion_id_f58ae107 ON public.app_gestion_documentos USING btree (condicion_id);
 @   DROP INDEX public.app_gestion_documentos_condicion_id_f58ae107;
       public            postgres    false    245                       1259    18072 &   app_gestion_documentos_iva_id_58c2ee6c    INDEX     k   CREATE INDEX app_gestion_documentos_iva_id_58c2ee6c ON public.app_gestion_documentos USING btree (iva_id);
 :   DROP INDEX public.app_gestion_documentos_iva_id_58c2ee6c;
       public            postgres    false    245                       1259    26602 +   app_gestion_documentos_numero_910c469a_like    INDEX     �   CREATE INDEX app_gestion_documentos_numero_910c469a_like ON public.app_gestion_documentos USING btree (numero varchar_pattern_ops);
 ?   DROP INDEX public.app_gestion_documentos_numero_910c469a_like;
       public            postgres    false    245                       1259    18279 *   app_gestion_documentos_usuario_id_d8339b15    INDEX     s   CREATE INDEX app_gestion_documentos_usuario_id_d8339b15 ON public.app_gestion_documentos USING btree (usuario_id);
 >   DROP INDEX public.app_gestion_documentos_usuario_id_d8339b15;
       public            postgres    false    245            =           1259    26777 %   app_gestion_excedente_cli_id_59faeb80    INDEX     i   CREATE INDEX app_gestion_excedente_cli_id_59faeb80 ON public.app_gestion_excedente USING btree (cli_id);
 9   DROP INDEX public.app_gestion_excedente_cli_id_59faeb80;
       public            postgres    false    275            >           1259    26769 %   app_gestion_excedente_doc_id_64e5307e    INDEX     i   CREATE INDEX app_gestion_excedente_doc_id_64e5307e ON public.app_gestion_excedente USING btree (doc_id);
 9   DROP INDEX public.app_gestion_excedente_doc_id_64e5307e;
       public            postgres    false    275            A           1259    26770 )   app_gestion_excedente_usuario_id_04d257db    INDEX     q   CREATE INDEX app_gestion_excedente_usuario_id_04d257db ON public.app_gestion_excedente USING btree (usuario_id);
 =   DROP INDEX public.app_gestion_excedente_usuario_id_04d257db;
       public            postgres    false    275            5           1259    26620 .   app_gestion_pago_detalle_documento_id_ce8d0ab9    INDEX     {   CREATE INDEX app_gestion_pago_detalle_documento_id_ce8d0ab9 ON public.app_gestion_pago_detalle USING btree (documento_id);
 B   DROP INDEX public.app_gestion_pago_detalle_documento_id_ce8d0ab9;
       public            postgres    false    269            6           1259    26621 )   app_gestion_pago_detalle_pago_id_6c77f667    INDEX     q   CREATE INDEX app_gestion_pago_detalle_pago_id_6c77f667 ON public.app_gestion_pago_detalle USING btree (pago_id);
 =   DROP INDEX public.app_gestion_pago_detalle_pago_id_6c77f667;
       public            postgres    false    269            '           1259    18193 +   app_gestion_pagos_banco_destino_id_bf2bd759    INDEX     u   CREATE INDEX app_gestion_pagos_banco_destino_id_bf2bd759 ON public.app_gestion_pagos USING btree (banco_destino_id);
 ?   DROP INDEX public.app_gestion_pagos_banco_destino_id_bf2bd759;
       public            postgres    false    259            (           1259    18177 %   app_gestion_pagos_cliente_id_f4376674    INDEX     i   CREATE INDEX app_gestion_pagos_cliente_id_f4376674 ON public.app_gestion_pagos USING btree (cliente_id);
 9   DROP INDEX public.app_gestion_pagos_cliente_id_f4376674;
       public            postgres    false    259            )           1259    18178 #   app_gestion_pagos_forma_id_808265c3    INDEX     e   CREATE INDEX app_gestion_pagos_forma_id_808265c3 ON public.app_gestion_pagos USING btree (forma_id);
 7   DROP INDEX public.app_gestion_pagos_forma_id_808265c3;
       public            postgres    false    259            ,           1259    18222 %   app_gestion_pagos_usuario_id_9d628d73    INDEX     i   CREATE INDEX app_gestion_pagos_usuario_id_9d628d73 ON public.app_gestion_pagos USING btree (usuario_id);
 9   DROP INDEX public.app_gestion_pagos_usuario_id_9d628d73;
       public            postgres    false    259            &           1259    26790 $   app_gestion_tasa_usuario_id_34d63218    INDEX     g   CREATE INDEX app_gestion_tasa_usuario_id_34d63218 ON public.app_gestion_tasa USING btree (usuario_id);
 8   DROP INDEX public.app_gestion_tasa_usuario_id_34d63218;
       public            postgres    false    257            	           1259    18032 '   app_gestion_vendedor_status_id_484b537b    INDEX     o   CREATE INDEX app_gestion_vendedor_status_id_484b537b ON public.app_gestion_vendedores USING btree (status_id);
 ;   DROP INDEX public.app_gestion_vendedor_status_id_484b537b;
       public            postgres    false    241            
           1259    26599 +   app_gestion_vendedores_cedula_72078c8c_like    INDEX     �   CREATE INDEX app_gestion_vendedores_cedula_72078c8c_like ON public.app_gestion_vendedores USING btree (cedula varchar_pattern_ops);
 ?   DROP INDEX public.app_gestion_vendedores_cedula_72078c8c_like;
       public            postgres    false    241                       1259    26630 )   app_gestion_vendedores_ciudad_id_8b17e7b7    INDEX     q   CREATE INDEX app_gestion_vendedores_ciudad_id_8b17e7b7 ON public.app_gestion_vendedores USING btree (ciudad_id);
 =   DROP INDEX public.app_gestion_vendedores_ciudad_id_8b17e7b7;
       public            postgres    false    241                       1259    26751 *   app_gestion_vendedores_usuario_id_9b7dd410    INDEX     s   CREATE INDEX app_gestion_vendedores_usuario_id_9b7dd410 ON public.app_gestion_vendedores USING btree (usuario_id);
 >   DROP INDEX public.app_gestion_vendedores_usuario_id_9b7dd410;
       public            postgres    false    241            �           1259    17961    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public            postgres    false    222            �           1259    17901 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public            postgres    false    224            �           1259    17902 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public            postgres    false    224            �           1259    17887 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public            postgres    false    220            �           1259    17917 "   auth_user_groups_group_id_97559544    INDEX     c   CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
 6   DROP INDEX public.auth_user_groups_group_id_97559544;
       public            postgres    false    228            �           1259    17916 !   auth_user_groups_user_id_6a12ed8b    INDEX     a   CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);
 5   DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
       public            postgres    false    228            �           1259    17931 1   auth_user_user_permissions_permission_id_1fbb5f2c    INDEX     �   CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
       public            postgres    false    230            �           1259    17930 +   auth_user_user_permissions_user_id_a95ead1b    INDEX     u   CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
       public            postgres    false    230            �           1259    17956     auth_user_username_6821ab7c_like    INDEX     n   CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public            postgres    false    226            �           1259    17952 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public            postgres    false    232            �           1259    17953 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public            postgres    false    232            �           1259    17970 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public            postgres    false    233            �           1259    17969 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public            postgres    false    233            N           2606    26733 I   app_gestion_ciudades app_gestion_ciudades_estado_id_39eda0a5_fk_app_gesti    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_ciudades
    ADD CONSTRAINT app_gestion_ciudades_estado_id_39eda0a5_fk_app_gesti FOREIGN KEY (estado_id) REFERENCES public.app_gestion_estados(id) DEFERRABLE INITIALLY DEFERRED;
 s   ALTER TABLE ONLY public.app_gestion_ciudades DROP CONSTRAINT app_gestion_ciudades_estado_id_39eda0a5_fk_app_gesti;
       public          postgres    false    4924    273    239            K           2606    18047 I   app_gestion_clientes app_gestion_clientes_status_id_c72489a0_fk_app_gesti    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_clientes
    ADD CONSTRAINT app_gestion_clientes_status_id_c72489a0_fk_app_gesti FOREIGN KEY (status_id) REFERENCES public.app_gestion_status(id) DEFERRABLE INITIALLY DEFERRED;
 s   ALTER TABLE ONLY public.app_gestion_clientes DROP CONSTRAINT app_gestion_clientes_status_id_c72489a0_fk_app_gesti;
       public          postgres    false    235    237    4862            L           2606    26558 M   app_gestion_clientes app_gestion_clientes_usuario_id_11cc7be4_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_clientes
    ADD CONSTRAINT app_gestion_clientes_usuario_id_11cc7be4_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 w   ALTER TABLE ONLY public.app_gestion_clientes DROP CONSTRAINT app_gestion_clientes_usuario_id_11cc7be4_fk_auth_user_id;
       public          postgres    false    237    226    4837            M           2606    18073 K   app_gestion_clientes app_gestion_clientes_vendedor_id_3d4a172d_fk_app_gesti    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_clientes
    ADD CONSTRAINT app_gestion_clientes_vendedor_id_3d4a172d_fk_app_gesti FOREIGN KEY (vendedor_id) REFERENCES public.app_gestion_vendedores(id) DEFERRABLE INITIALLY DEFERRED;
 u   ALTER TABLE ONLY public.app_gestion_clientes DROP CONSTRAINT app_gestion_clientes_vendedor_id_3d4a172d_fk_app_gesti;
       public          postgres    false    241    237    4872            R           2606    18061 L   app_gestion_documentos app_gestion_document_cliente_id_20316d3e_fk_app_gesti    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_documentos
    ADD CONSTRAINT app_gestion_document_cliente_id_20316d3e_fk_app_gesti FOREIGN KEY (cliente_id) REFERENCES public.app_gestion_clientes(id) DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public.app_gestion_documentos DROP CONSTRAINT app_gestion_document_cliente_id_20316d3e_fk_app_gesti;
       public          postgres    false    4864    245    237            S           2606    26690 N   app_gestion_documentos app_gestion_document_condicion_id_f58ae107_fk_app_gesti    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_documentos
    ADD CONSTRAINT app_gestion_document_condicion_id_f58ae107_fk_app_gesti FOREIGN KEY (condicion_id) REFERENCES public.app_gestion_condicion(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.app_gestion_documentos DROP CONSTRAINT app_gestion_document_condicion_id_f58ae107_fk_app_gesti;
       public          postgres    false    271    4922    245            T           2606    26703 S   app_gestion_documentos app_gestion_documentos_iva_id_58c2ee6c_fk_app_gestion_iva_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_documentos
    ADD CONSTRAINT app_gestion_documentos_iva_id_58c2ee6c_fk_app_gestion_iva_id FOREIGN KEY (iva_id) REFERENCES public.app_gestion_iva(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.app_gestion_documentos DROP CONSTRAINT app_gestion_documentos_iva_id_58c2ee6c_fk_app_gestion_iva_id;
       public          postgres    false    249    245    4893            U           2606    18274 Q   app_gestion_documentos app_gestion_documentos_usuario_id_d8339b15_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_documentos
    ADD CONSTRAINT app_gestion_documentos_usuario_id_d8339b15_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 {   ALTER TABLE ONLY public.app_gestion_documentos DROP CONSTRAINT app_gestion_documentos_usuario_id_d8339b15_fk_auth_user_id;
       public          postgres    false    4837    245    226            ]           2606    26772 G   app_gestion_excedente app_gestion_excedent_cli_id_59faeb80_fk_app_gesti    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_excedente
    ADD CONSTRAINT app_gestion_excedent_cli_id_59faeb80_fk_app_gesti FOREIGN KEY (cli_id) REFERENCES public.app_gestion_clientes(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.app_gestion_excedente DROP CONSTRAINT app_gestion_excedent_cli_id_59faeb80_fk_app_gesti;
       public          postgres    false    237    4864    275            ^           2606    26759 G   app_gestion_excedente app_gestion_excedent_doc_id_64e5307e_fk_app_gesti    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_excedente
    ADD CONSTRAINT app_gestion_excedent_doc_id_64e5307e_fk_app_gesti FOREIGN KEY (doc_id) REFERENCES public.app_gestion_documentos(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.app_gestion_excedente DROP CONSTRAINT app_gestion_excedent_doc_id_64e5307e_fk_app_gesti;
       public          postgres    false    4888    245    275            _           2606    26764 O   app_gestion_excedente app_gestion_excedente_usuario_id_04d257db_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_excedente
    ADD CONSTRAINT app_gestion_excedente_usuario_id_04d257db_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.app_gestion_excedente DROP CONSTRAINT app_gestion_excedente_usuario_id_04d257db_fk_auth_user_id;
       public          postgres    false    4837    275    226            [           2606    26610 P   app_gestion_pago_detalle app_gestion_pago_det_documento_id_ce8d0ab9_fk_app_gesti    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_pago_detalle
    ADD CONSTRAINT app_gestion_pago_det_documento_id_ce8d0ab9_fk_app_gesti FOREIGN KEY (documento_id) REFERENCES public.app_gestion_documentos(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.app_gestion_pago_detalle DROP CONSTRAINT app_gestion_pago_det_documento_id_ce8d0ab9_fk_app_gesti;
       public          postgres    false    269    4888    245            \           2606    26615 K   app_gestion_pago_detalle app_gestion_pago_det_pago_id_6c77f667_fk_app_gesti    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_pago_detalle
    ADD CONSTRAINT app_gestion_pago_det_pago_id_6c77f667_fk_app_gesti FOREIGN KEY (pago_id) REFERENCES public.app_gestion_pagos(id) DEFERRABLE INITIALLY DEFERRED;
 u   ALTER TABLE ONLY public.app_gestion_pago_detalle DROP CONSTRAINT app_gestion_pago_det_pago_id_6c77f667_fk_app_gesti;
       public          postgres    false    259    269    4907            W           2606    18211 J   app_gestion_pagos app_gestion_pagos_banco_destino_id_bf2bd759_fk_app_gesti    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_pagos
    ADD CONSTRAINT app_gestion_pagos_banco_destino_id_bf2bd759_fk_app_gesti FOREIGN KEY (banco_destino_id) REFERENCES public.app_gestion_bancodestino(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.app_gestion_pagos DROP CONSTRAINT app_gestion_pagos_banco_destino_id_bf2bd759_fk_app_gesti;
       public          postgres    false    259    4910    261            X           2606    18166 D   app_gestion_pagos app_gestion_pagos_cliente_id_f4376674_fk_app_gesti    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_pagos
    ADD CONSTRAINT app_gestion_pagos_cliente_id_f4376674_fk_app_gesti FOREIGN KEY (cliente_id) REFERENCES public.app_gestion_clientes(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.app_gestion_pagos DROP CONSTRAINT app_gestion_pagos_cliente_id_f4376674_fk_app_gesti;
       public          postgres    false    237    4864    259            Y           2606    18204 Q   app_gestion_pagos app_gestion_pagos_forma_id_808265c3_fk_app_gestion_pagoforma_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_pagos
    ADD CONSTRAINT app_gestion_pagos_forma_id_808265c3_fk_app_gestion_pagoforma_id FOREIGN KEY (forma_id) REFERENCES public.app_gestion_pagoforma(id) DEFERRABLE INITIALLY DEFERRED;
 {   ALTER TABLE ONLY public.app_gestion_pagos DROP CONSTRAINT app_gestion_pagos_forma_id_808265c3_fk_app_gestion_pagoforma_id;
       public          postgres    false    4899    259    255            Z           2606    18217 G   app_gestion_pagos app_gestion_pagos_usuario_id_9d628d73_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_pagos
    ADD CONSTRAINT app_gestion_pagos_usuario_id_9d628d73_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.app_gestion_pagos DROP CONSTRAINT app_gestion_pagos_usuario_id_9d628d73_fk_auth_user_id;
       public          postgres    false    226    259    4837            V           2606    26785 E   app_gestion_tasa app_gestion_tasa_usuario_id_34d63218_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_tasa
    ADD CONSTRAINT app_gestion_tasa_usuario_id_34d63218_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.app_gestion_tasa DROP CONSTRAINT app_gestion_tasa_usuario_id_34d63218_fk_auth_user_id;
       public          postgres    false    257    226    4837            O           2606    26625 K   app_gestion_vendedores app_gestion_vendedor_ciudad_id_8b17e7b7_fk_app_gesti    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_vendedores
    ADD CONSTRAINT app_gestion_vendedor_ciudad_id_8b17e7b7_fk_app_gesti FOREIGN KEY (ciudad_id) REFERENCES public.app_gestion_ciudades(id) DEFERRABLE INITIALLY DEFERRED;
 u   ALTER TABLE ONLY public.app_gestion_vendedores DROP CONSTRAINT app_gestion_vendedor_ciudad_id_8b17e7b7_fk_app_gesti;
       public          postgres    false    239    4869    241            P           2606    18026 K   app_gestion_vendedores app_gestion_vendedor_status_id_484b537b_fk_app_gesti    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_vendedores
    ADD CONSTRAINT app_gestion_vendedor_status_id_484b537b_fk_app_gesti FOREIGN KEY (status_id) REFERENCES public.app_gestion_status(id) DEFERRABLE INITIALLY DEFERRED;
 u   ALTER TABLE ONLY public.app_gestion_vendedores DROP CONSTRAINT app_gestion_vendedor_status_id_484b537b_fk_app_gesti;
       public          postgres    false    235    241    4862            Q           2606    26746 Q   app_gestion_vendedores app_gestion_vendedores_usuario_id_9b7dd410_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_gestion_vendedores
    ADD CONSTRAINT app_gestion_vendedores_usuario_id_9b7dd410_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 {   ALTER TABLE ONLY public.app_gestion_vendedores DROP CONSTRAINT app_gestion_vendedores_usuario_id_9b7dd410_fk_auth_user_id;
       public          postgres    false    226    241    4837            C           2606    17896 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public          postgres    false    224    220    4824            D           2606    17891 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public          postgres    false    224    4829    222            B           2606    17882 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public          postgres    false    218    220    4819            E           2606    17911 D   auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
       public          postgres    false    4829    222    228            F           2606    17906 B   auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
       public          postgres    false    228    226    4837            G           2606    17925 S   auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
       public          postgres    false    230    4824    220            H           2606    17920 V   auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
       public          postgres    false    230    4837    226            I           2606    17942 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public          postgres    false    218    4819    232            J           2606    17947 B   django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
       public          postgres    false    232    4837    226                  x������ � �         �   x�]�A�0������E�ݠѐ��ͤ�[S���$�v����@��B�zi�R[�I�=��r��=���y���k{�m��Y�l���|^cI�0�,��G��X���6-��x���LJ8�x��im�i����{�X�m���_ZƦ���mX�         �  x�5S�n�@<s�B_Ph�����(��m� z�关��uV� ���؃O����:\�CC��p8�i�]�8r�'GZe��u���nط�s=��K�v�@y�㒓Ƈ7��kh5��B5���;;:�Ռ~q���s�u��$�C@�\ͩ�]`*�Ne��^�&�x��輍����s�G9��s�w��Np!FN~�1��~o�Ɋmױ�m���ZV�=T*z�u��C ٰ�mr���ʞ*��� �:2dAL˒-(Q����v7�3�r�j/��O��uNb%=rg��Ɗ*�Ӱ��@3�մ��`�x�d�t�2t�Kk��hݣ�}>4*;޸7@�1����`wtO��"�\8t&f8Y����(DL���|:Wy����	����z��׆�vF?��8�\����B)�O�ݞ�>a3���KUd�L�?s��9��B�h����%�Y��`��ڰG=��p����eh#�f8��t�IW��G�5g���8o1�G��kUjZ9�1D�a��w�iX�������gq��Rh�|AQ����=��������=��+i���c�e�*紞޽ݰ�*�8��S3�*Mk��Kf�T������:{���UU�o��kOj��7+TU]��lp	�P�}�Qb�����m#��'x�NCcu��_I�L�����3�E�         �   x���1O�0���
������b��RI�&<j���1A%��t����]�x�@X��������!�;uR�
I|�����a�Jj+�Hh��$nL%�ϱ�)�|�!pʿK480��ek	�r�զ��8朾�u��e� K�uu4�A@��ޮ�F<�s�Ӹ��ѫ��0{�q�@Z�i��ܤ�&��,+.??rB?qL}VϾ��-��j�mI@u�oh��|-���bsv�      '   !   x�3�t��+IL��2�t.JM�,������ _Y�            x�3�4202�54"�=... �         $   x�3�41�2�4�2�4�2�44�2�46������ 6"�            x�3�41����� TV         ,  x��T;��0��S�II~$H�9�6�ժ�&)��?�JkS�&�G�l ���H�G���C�6N������s���i��˼\��<N�}��m��;��N�9ߚ����|������vL�v��ްW3_.G��ba=Ct��}�#��X#L �=�?�v��q�٢C\�ib�HA�y~�E�*��R�鉊�dD�Pj����Tn��=(q
�^@[,-U>���)pI����
�C5m��iX���K�)�r�
��|�z�6X�B�6�#�{d�c>:OU8���	�^��k.��}:�42�rv�&U�,>�7��sJ���t�iU��q�dSz�JN {��׸8��¼#V�J�rf:�3V)!S�.Oq�V}�&9�O*Q����P9����FP���+��K�=&'���oPj5>�|F��vU�H�/m�Hk��++M��,��G���x61Һ)��v���n
����'�6��%�v�Wn�ŕ�;P�+m���� W@�`T�^��Q��Zqm�u����\��i7�[��!��Iϖ j��ҳ�-���c6L      )   �   x��=N�@��S��e��_�8�&AHDHD4ge6Z��x'��K
*���1���|��(��[��B�^�8$׈��N�a%S#�SX�8�U���P�1#.��gwr=.a�B�L͵pD3������:�(�1�D��Z462�kEsتM���I�v�����tj����]({�;⤷�DN҈�-�Uj�o'���Sh�Y�>��������-e!�����k�F[�A�'�x@��B\�      +   E   x�3�t�HNMI�+IU�4�35�FF&��F��
�V&�V��z&�&��&�&d-89��b���� �.q         &   x�3���2�H�K�L�+I�2�HLOL������ v��      %   �   x�=��C!C�V1�@/鿎��$@O�4����GF#�m[܈��<��h_���	�I����i�pZ~�K
��G7b~� ������'�A����Bq���wC�fb]r����5���D7��V�!�/�~�#�         a   x�e�;
�0 �99E.��]���%�
!�F<����7��آH˕ia��s�n�0��+7	��H���0���A��
�8��Z�_�1A	�_� &         Q  x��Xۊ�F}��BOy�{��W1d�B�%�E�j'&��`���	��TK�X�e�'�B0�ut��t��\F@z��A�6( ��!�LF�5��B;�'�н�MAP蠜#�Wmf4���+/���Ip��bht�}���;lOO��c��Ny�T>��S},rX�=s@�l���x�?���;�R���cu� X�qzg�~�&��,�n��?I��D@a|�Aq��n��f�0��4���L�� 1j���&¿��5�u�0�����o�6�x�>U��ۗ��Sy��]���T�䳐����j���מt7��Vd��e���,� _R�X@�f!��5�����юA	����=�f���\ĵusX6+bD,Z�k���d�s��T�.[�Ʃ�U�m�=�󉩌AI�)��o�~[v��7��<T�]ݞ�Ϯ;��2b] *�N���EE(@̔�"JR4E���W�L�^MM��5`�V9���cq��f���z�4l�k�0:��E�S��n|�r'۫���vcW��]y(�����������gԹ��}�����?U�?��ew_"�:���%�*��<��}dLE�ى���\2S|%6
�H�ѽ�������sZ�kt"R�>0����kBN�dC����4�~�<�y�7 ��m�>T��Dɳ���=�p�[��xSP}��e�CK��s�m�4l���k��Z8�W�'�1���Ƃ�ćƑ6~vd��,v����A� 9��V�	�6�hK2��t�6�2�:���[��tˮ��)�~
���o��i1��c:p<iQ,o�\�<0��1j��Iyu`\Ά[���A�˲�0��<?�b$�ܣ�ߣ�v�~=2��髑G�Ro���7��Epo��<<�?�?�؎��c�T����)����.��s� ��mq�-G}h��X^W=��lW㻧2&h��@^�ZrЗ���VN�C�3nu����q�}N��ʨIzL��D�q�H<-o�H��)���8���9�	/o����<~R�W�쵗w��x���]�r=��u~���G�t���B��F����L��<=3A�n����� ��X��z`z=��G���j�����H      !      x�3���2������ ��      #   *   x�3�4014� RF&\� ����6�24	�q��qqq �d            x�3����2��O�/�2������� @��         +   x�3�tL.�,��2���K�0M�L�����|.#N(#F��� ���         �   x���Mj�0���)��*��H��$�7�F76	%���)�`=B/V�!4.j�]	i������pE�"*\��Ń"�l��0�U��C*ڡ����C�5�:5Nٶ�v����p|R�Ӯ���^�u�"�fxg�g�e:S7���
�7�q�����W�8�G��E�� sۅ�\������o9���0Y-'��V��OZ�����l�.&�,��4�d�|�f#6d�֐�_���N����tY��〺�      	   �   x���A
�0�����@C��4���B\�	���B�EJ)���{O�<�ul�_jk�����T)qd퀎�C
�"9��k�.�
:�yZ������~�lq��H�CȖr�-~\�nu���?��f�){EK� b���Ʈ�=�s�#�=|      �      x������ � �      �      x������ � �      �   e  x�m�ˎ�8E��W�����I��`V���(p[�$�$?�uK��:e^��XvY|jn���6��uo���(�4��q�*#����ES�2��k�=HS�3�����LtPe�8��������l"Q�Y�'��Xlm�5wV�����,0��I�u1R�&AX#�I ���N<�8�,`��=��Q^���� /N����p^��']�ns������CV�S�L(k��Y��Ϩkų>䫭�\�Y�cKU=E��c̣P9��:sn7��)^7(�RĜ�^���Sq�3�a��́��S�y@95����q)d�n�}:�X�$�Fa�n��̹�0%8� �$����]�g�a����aȹ^!�8_����rZ|e����^�� B���dd���Cas�?���n���,*�y��̈�#���dMF����Ҍ2WO.����b�!읡�"�yY9"b��J�Q��yho�D	�.��D88;���XV,ڑY!p���}S��D��	gh��%��qѱ�������9��{
Q���S�ٗ��j�;�r�W]�G0.G�9f�]��q��u�4G�Y��Sd�98�����!3�ֹ��b�	��pt^�0�!�9U�A�T�Y Eͥ��uؼ�[B�EYf�D89�zR~��|�a��c0գ�{�@s�ͭMf�����ܪ kc�9V���V������fꩨ��0���b-�9'�z����@eMʘ���+���_���%�j�f!�B>��^O��f�7Ms�Ī��P?\�xa�r�po����)��1��Sq��Oc��t���-�� @�2���큢�As�}�/������2�/EE��j:�]<I�k_��x�'fX�A�<�"��sNv5�oY:h�wے�p����V���a�jk�Yn�7��nw�V���Ź�^cQ�&e.���]E�Rv��S�j!e��XL�2��������)}NAW���D��WA�'�) 5%
C=��o�?���j�H�`}Q"i[a_�[�V�Qi�
Z�~I����jK1��J����@�X�bPpeQ�X}�ߩ����z�N$̕�#E���,ƿ�%�
��+��?�/�_      �     x�m�KO�@ ���+z��@��+ibԴ"��R�m��E
-�e]�b���ћN�8�|����;r��`�c��&^u��2��4.���\m'eR�摺���;��YDw���m��Ї�H�d��������SmsP-:� 1�� !'`, ��e̳ 5��qE����wN���)KKM�«�l(��>쳔�~�\����̸���X
������뎠 7`��(#��c#�v\��!K��9����j��m���"�þ�{�0�/�n]n      �      x������ � �      �      x������ � �          ~  x����n�0���S���.�y,� -��h�^�hKM$"@�y�.E��-)Ex2����]
*�(/�_pQ��Jy�V�.+��)>�)�
���uh��Y����嶒��75��+˜��0��R؅ng�℠<�L�ZHc�:�M������E�P�G�%g��f������]�w�C���7�o�}��®��������{���\HQ�����K����%��H��Xas����������C�&���6�G��(&%����mJqR�m��S��Q�jLv��ބD��e'�;�Hj2g:wg����C�4�! Q��K�
��>��=�/��``ʡr �	�~�=�c:Fx7��L:
ˍ�����3Y/�z����b�j��A,���s͔Ss��\��z��r�V�{3�kZ�X�(D}FT�2�ܸ�h���9O�	������}�в�,��k=m��!�բ80sZ��n����B��͠���gĆq�҈��u=�a*�-:Ir�(��d
9������� �yO��1�M}���4���Ao��]GnU�m�B3;�@� �
y.�2
��M���!��9�MG��X,�!�E�q�P����J����f��_l�Z��	�|      �   
  x�m��n� ����L�&��.�"N� �Z�~N�Is����H��~��BZ0�r�lo�*cY�VJ�e)�gE�X`T.��cힱ�-�*����^��yZ�6���^�7�R���U����A��x��ѧZK3?h#D�\_�8n�e�,�AHtci���� �"�f+[e�l�4��rC�~���x�k+����	}��[�xF⹂��m$\.8�W����f���0�]�)&�͆�`��)���|K�����D��z�Kv��\�/�� ?���      �   :
  x��Z[��:�NV�DE���k�*�b�;�q[}e;��� iI��t&7Uݾrx������x������{�d��v8��;~B���Wc��ߑ�!5�z����g��]/�?^L��d���ކ�,�&�%�,��8���ӯv���}���mw8<���gC݂a^�v��0�ڗc��Þ=���+X~�.�YS�h��Խ�����Ŭ0���x����ކ�YL���[��=��W�[����^��e+���?��n8~��KQPҌBk����/Oܓ��f�pk�cw���>����ң�CF�ųw�������V���:d�g����á���9�~?M�Ծ��s����I���.>��n��.� hJ�R�����B�N����`l��x��0�^��C}�>�?���=���̀�S�ӟˡ�������]?�[g
k����-_�������h�\#�wy%���p=t�v�t}�_���sА��A��`�������5J�!�5Ѻ���Xم��|�.�s�U�\>�8�)~��(6�0�J̶�&�z�'0~�R��j$��a.ݷc�@�� c#�b�� 7��>+ƨ���N��m�6����%���7�z����O��0NwK�Q;!�4��vw��*,kw��IY�,؛1\�v�0�a��k��`k��qf���ONKA�a��mX�ֱHp��ۖ��^�4���;	;0;c�=C>��2�[�*>� ��Φ�;O�Z&0�d�G>`��$�#����7u�����ǜ3��H���j����z�f�71y\�ܖKL�ƃI�c��ځ���nU�Y�zh0E��� �Ïe�/F6��h�$R�u isF����L���\��h=���ӌ$L�;��D[�Ӓ@Xat��Sw����ڒ Isq��~=�?�!�:�s(Q1�4�q	�\e^����!V��X	9ɖbWS)�=�x\�i�[=�O�|�yj,E*�#Mpt������u|����Й��|�B 9��;��8�'��$�r��=��^�Q��>���d.��:�e��Ũ�S�8���kM	��ٍ��y?�9fe�Al�^n����9W��2�T�����(plmhL�6��EZ֔�8ȓ�jy�善)ΤD��#M{;g�l�r��c�}pڌ��KO	]�wZ���n��Y.���>�9-k��>���uk%��2��l4.o�ci�6f��P�v��ppu���B��L��')�I��-��ꮖ/����$=�,[���.�fW�Ɇ�p=_�i�;8Wd!,6L�,�"�q����u���9H�B9�k�ഄl�[p}�i�DC�ZPd~s���&�-*�!8�I�J��Z6�Bn�n�n���X�o�4+ظ3�`��b�W㵒�VT���?�ʛ��r����dnz�*r5_,�O��h�W�΄�����Z_���⼓0F��uൌ(��(�����"y-$�7C~���6��@�^k��՗�r0��H�6!���@ܶ�R��5J�.��L�2q�I�ee���K�6&hy��<�zCK3�.128�]��}Vq`�α��9*A.h��m��է�u�X�8蠧�����轀��s�S�d�Tv�b�ܴ���Hņ�I>�k��[��,P���܂Y�H�H�^�渋e!s�`Ʋw��.!h��3|+A/�M&9A+�)��z�͵��� ����%��o����_h��eA��k�%F��3����2�F��d��D��5j�[:�5�a����SA*A�ŷZ4j=x�1�ˆ��u@�����*j���3��̽�
u�5߽����8;4���)�Q��$Ӛ\W0P�w���q;g)�|��z��>�մ�f��퓶O��g�X	�� ��4j��<I��o,��K1W<Q�8�FI'�=��ˀ�I,�RJ��o��;Αd2!-���ĉ�Ǭ����J�
�8|�$� �Xoє��Ձ�,�N+�Ӈ�,�
(\aʁo����@��nu	�1�ف4��/A&�A?�H���<��\�C��������2'Skt��m��I�=���?�`C�eI�:̃RY�;0aQ�&D��L3;���ܫo*��AI�����2h�i����h�G�$�c������l���1��e*�y��Ur��h:��# }7��-���0P5K3>��
�����)�R �Ѥ��}O0�p����/����5�2-,0In���9,sY0��1l�G�pLxN��,�j�f|��-�D��Ҍ:�R}�f�&b�e�^a8Ig\�Ɛ*��B2�@+܏��ʖ2�1��	lV�'��Op�Q~��e�����"��U��OXW��c��9�А�谠i�'�Pu=W[j��=��Ib��o�t��\��Dm��é�j^�&�4R�$�lh$�,m. ��Đ������i���a�mV#G��\�;.�|_z��B� ��%��Z�N|.S��ϲ:�#��Mє�@k!�|��k�/�]� WX��KS>=���չ>�� D�����A��e��;�ӊ]��O`�(@Ʈ�sa=oҰ0'+�W9����71�k��� 7�ܐg�5�?�a`[3         ;  x���Gn�H ���)t	��N䎔��@QY2�9'�����gж�U6����v�2ʺ~k���;��[n������a����{.Q�\�%����DS�R+��'켵���=c"a��3t���]oy�+/������9�à����qv׉�չ�p��/�=w��t]Ý�WquiL[�22Uk�y���n:�u`t������ۧ�H�n�#�Q雼�n��5 ��;�)�q���K�?o����J�����!�AQT|!`N	��G� -A������\$E?YS��#yE�q�`��5맹�QS�v���FY�Ǣ��E�}�u\� �6?D��� ]P"�MD-u����'�y�
���ö±�_��i	�ǥPMj���ֻ�_إ�\��˧��j��� �}���w����"ʀ�E$�V�$�.g��x��(�@�8)�W$�P�Z�5o�ȝZ�}(��x5�Y0@��m-v�����i��Cg�JH�|!N�Qo�I3ʪ�`���@"n5�P���D��Zh�����`�쟹�n:��h��2-�@��4=;�s��"���g������"��nO!F�Y�EYDQ�d(+��+����/�6�c߅��n>%��w�����q{M6Ԫj�����9�3�%L$". ��~��%=�e�������rhƲ�W��V�]6R�'p0��_I����n�l:ɤ�Ʀ����3?}$�TD��/�r�I`�Q���1뛪	p��Dz�Ci�����⍶M���+��i�N"��G�|���P����_w�D�������������8��     